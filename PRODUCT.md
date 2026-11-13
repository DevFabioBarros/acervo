# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Uma pessoa usando o Acervo localmente para guardar documentação e consultá-la depois. Uso pessoal confirmado pelo usuário.

## Product Purpose

O Acervo captura páginas de sites em coleções e permite fazer perguntas sobre o conteúdo coletado.

## Positioning

O usuário escolhe quais sites formam cada coleção; a conversa responde com base nesses documentos.

## Operating Context

Aplicativo Streamlit de uso pessoal. O usuário alterna entre capturar páginas e conversar com uma coleção existente.

## Capabilities and Constraints

- Captura páginas de um site e salva arquivos Markdown em `data/collections`.
- Carrega os documentos da coleção selecionada para consulta por RAG.
- Mantém os fluxos simples: capturar conteúdo e perguntar sobre ele.
- A captura depende do serviço Firecrawl; as respostas dependem da API Groq e do modelo de embeddings configurado.

## Brand Commitments

- Nome: Acervo.
- Interface em português, natural e minimalista.
- Evitar aparência genérica de template e preservar simplicidade funcional.

## Evidence on Hand

- Interface Streamlit: `app.py`, `presentation/chat.py` e `presentation/scrapping.py`.
- Coleção existente: `data/collections/oh_my_posh`.
- Marca vetorial existente: `assets/acervo.svg`.

## Product Principles

- Tornar claro qual coleção está ativa.
- Manter captura e consulta fáceis de encontrar.
- Responder com base nos documentos coletados.
