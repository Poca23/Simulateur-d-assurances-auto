import streamlit as st
from components.header import render_header
from components.form_vehicule import render_form_vehicule

# Configuration page
st.set_page_config(
    page_title="Simulateur Auto - Saint-Pierre Assurances",
    page_icon="🚗",
    layout="wide"
)

# Affichage header
render_header()

# Formulaire véhicule
vehicule_data = render_form_vehicule()

# Debug (temporaire)
if any(vehicule_data.values()):
    st.success("✅ Données véhicule saisies !")
    st.json(vehicule_data)
