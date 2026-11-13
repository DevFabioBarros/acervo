import streamlit as st
from service.scrapping import ScrappingService


def show():
    st.title("Capturar páginas")
    st.caption("Informe o endereço do site e o nome da coleção onde guardar as páginas.")

    scraper = ScrappingService()

    with st.form("scrapping_form", border=False):
        url = st.text_input("Endereço do site", placeholder="https://exemplo.com/documentacao")
        collection_name = st.text_input("Nome da coleção", placeholder="minha-colecao")
        submitted = st.form_submit_button("Capturar páginas", type="primary")

    if submitted:
        if not url.strip() or not collection_name.strip():
            st.error("Preencha o endereço do site e o nome da coleção.")
            return

        with st.spinner("Capturando páginas..."):
            result = scraper.scrap_website(url.strip(), collection_name.strip())

        if result["success"]:
            st.success(f"Coleção pronta: {result['files']} páginas adicionadas.")
        else:
            st.error(f"Não foi possível capturar o site: {result['error']}")
