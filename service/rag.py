import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate


class RAGService:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="openai/gpt-oss-20b"
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        self.vector_store = None
        self.qa_chain = None

    def load_collections(self, collection_name):

        collection_path = f"data/collections/{collection_name}"

        loader = DirectoryLoader(
            collection_path,
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={'encoding': 'utf-8'}
        )

        documents = loader.load()

        if not documents:
            return False

        texts = self.text_splitter.split_documents(documents)

        self.vector_store = FAISS.from_documents(texts, self.embeddings)

        template = """
            Use os seguintes documentos para responder à pergunta.
            Se as respostas não estiverem nos documentos, diga que não sabe.

            {context}

            Pergunta: {question}
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(search_kwargs={"k":3}),
            chain_type_kwargs={"prompt":prompt}
        )

        return True

    def ask_question(self, question):
        if not self.qa_chain:
            return "Nenhuma coleção carregada."

        try:
            result = self.qa_chain.run(question)
            return result
        except Exception as e:
            return f"Erro ao processar pergunta: {str(e)}"
