# Acervo

Aplicativo pessoal para guardar páginas da web em coleções e consultar o conteúdo em uma conversa. A interface usa Streamlit; a captura usa Firecrawl; a busca semântica usa embeddings locais e FAISS; as respostas usam a API Groq.

## O que faz

- Captura páginas de um site e salva o conteúdo em Markdown.
- Organiza páginas por coleção.
- Responde perguntas com base nos documentos da coleção selecionada.
- Oferece interface em português, temas claro e escuro.

## Requisitos

- Python 3.11.
- Uma chave de API do [Firecrawl](https://www.firecrawl.dev/) e uma instância acessível para capturar sites.
- Uma chave de API do [Groq](https://console.groq.com/) para conversar com os documentos.
- Acesso à internet na primeira execução para baixar o modelo de embeddings `all-MiniLM-L6-v2`.

## Instalação

No Windows PowerShell, a partir da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edite `.env` e informe suas chaves:

```env
FIRECRAWL_API_KEY=sua_chave_firecrawl
FIRECRAWL_API_URL=https://api.firecrawl.dev
GROQ_API_KEY=sua_chave_groq
```

Para Firecrawl auto-hospedado, troque `FIRECRAWL_API_URL` pelo endereço da sua instância.

Inicie o aplicativo:

```powershell
streamlit run app.py
```

## Dados e privacidade

As páginas capturadas ficam em `data/collections/<nome-da-coleção>/`. Essa pasta é ignorada pelo Git para não publicar conteúdo coletado localmente. Faça suas próprias capturas depois de configurar o Firecrawl.

O índice FAISS é criado em memória ao carregar a coleção; o projeto não grava um banco vetorial persistente. O modelo de embeddings roda localmente após o download inicial. As perguntas e o contexto enviado ao modelo são processados pela API Groq.

## Configuração

| Variável | Uso |
| --- | --- |
| `FIRECRAWL_API_KEY` | Autentica a captura de páginas. |
| `FIRECRAWL_API_URL` | Endereço base da API Firecrawl. |
| `GROQ_API_KEY` | Autentica respostas do chat. |

Não publique seu arquivo `.env`. O `.gitignore` já bloqueia esse arquivo; `.env.example` contém somente nomes e valores de exemplo.

## Licença

O repositório ainda não declara uma licença para o código do projeto. Os arquivos da fonte IBM Plex incluem sua licença própria em `assets/fonts/OFL.txt`.
