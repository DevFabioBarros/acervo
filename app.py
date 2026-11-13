import os
from base64 import b64encode
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from presentation import chat, scrapping

load_dotenv()
st.set_page_config(page_title="Acervo", page_icon="assets/acervo.svg", layout="wide")

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "collection" not in st.session_state:
    st.session_state.collection = None
if "mode" not in st.session_state:
    st.session_state.mode = "Conversar"
if st.session_state.mode == "Adicionar conteúdo":
    st.session_state.mode = "Capturar site"
if "messages" not in st.session_state:
    st.session_state.messages = []

with open("assets/acervo.css", encoding="utf-8") as stylesheet:
    css = stylesheet.read()
for weight in (400, 500, 600):
    font_path = Path(f"assets/fonts/ibm-plex-sans-{weight}-latin.woff2")
    font_data = b64encode(font_path.read_bytes()).decode("ascii")
    css = f"@font-face{{font-family:'IBM Plex Sans';font-style:normal;font-weight:{weight};font-display:swap;src:url(data:font/woff2;base64,{font_data}) format('woff2');}}\n" + css
if st.session_state.dark_mode:
    css += "\n:root { --ink:#eeece4; --muted:#c1beb4; --paper:#191a18; --side:#22231f; --surface:#242521; --line:#494840; --accent:#e46a58; --accent-hover:#f07b68; --accent-ink:#211915; --soft:#34332d; --placeholder:#c2bfb4; color-scheme:dark; }"
else:
    css += "\n:root { color-scheme:light; }"
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

collections_dir = "data/collections"
collections = sorted(
    name for name in os.listdir(collections_dir)
    if os.path.isdir(os.path.join(collections_dir, name))
) if os.path.exists(collections_dir) else []
if st.session_state.collection not in collections:
    st.session_state.collection = None

with st.sidebar:
    brand_mark, brand_name = st.columns([0.18, 0.82], gap="small", vertical_alignment="center")
    with brand_mark:
        st.image("assets/acervo.svg", width=34)
    with brand_name:
        st.markdown("### Acervo")
    st.caption("Biblioteca pessoal")

    st.markdown("**Seção**")
    if st.button("Conversar", key="nav_chat", type="primary" if st.session_state.mode == "Conversar" else "secondary", width="stretch"):
        st.session_state.mode = "Conversar"
        st.rerun()
    if st.button("Capturar site", key="nav_capture", type="primary" if st.session_state.mode == "Capturar site" else "secondary", width="stretch"):
        st.session_state.mode = "Capturar site"
        st.rerun()

    st.divider()
    st.markdown("**Coleções**")
    if collections:
        for name in collections:
            if st.button(name, key=f"collection_{name}", type="primary" if name == st.session_state.collection else "secondary", width="stretch"):
                st.session_state.collection = name
                st.rerun()
    else:
        st.caption("Capture um site para criar sua primeira coleção.")
    st.divider()
    st.toggle("Modo escuro", key="dark_mode")

if st.session_state.mode == "Capturar site":
    scrapping.show()
else:
    chat.show(collections)
