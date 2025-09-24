import streamlit as st
from components.header import render_header

# Configuration page
st.set_page_config(
    page_title="Simulateur Auto - Saint-Pierre Assurances",
    page_icon="🚗",
    layout="wide"
)

# Affichage header
render_header()

st.write("🚧 Application en construction...")
