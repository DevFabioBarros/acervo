import streamlit as st
from service.rag import RAGService


def show(collections=None):
    st.title("Conversa")

    collection = st.session_state.collection
    if not collection:
        st.markdown("""<section class="library-empty"><h2>Escolha uma coleção</h2><p>Abra uma coleção para conversar com as páginas guardadas.</p></section>""", unsafe_allow_html=True)
        for name in collections or []:
            if st.button(f"Abrir {name}", key=f"main_collection_{name}"):
                st.session_state.collection = name
                st.rerun()
        return

    st.caption(f"Coleção: {collection}")

    if "rag_service" not in st.session_state:
        st.session_state.rag_service = RAGService()

    if st.session_state.get("current_collection") != collection:
        with st.spinner("Carregando páginas..."):
            success = st.session_state.rag_service.load_collections(collection)
            if success:
                st.session_state.current_collection = collection
            else:
                st.error("Não encontrei páginas nesta coleção.")
                return

    if st.session_state.messages:
        if st.button("Limpar conversa", key="clear_chat"):
            st.session_state.messages = []
            st.rerun()

    if not st.session_state.messages:
        st.markdown("""<section class="empty-chat"><h2>Sua conversa começa aqui</h2><p>Faça uma pergunta sobre as páginas desta coleção.</p></section>""", unsafe_allow_html=True)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Pergunte sobre esta coleção..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Consultando as páginas..."):
                response = st.session_state.rag_service.ask_question(prompt)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
