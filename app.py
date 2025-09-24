import streamlit as st
from components.header import render_header
from components.form_vehicule import render_form_vehicule
from components.form_conducteur import render_form_conducteur

# Configuration page
st.set_page_config(
    page_title="Simulateur Auto - Saint-Pierre Assurances",
    page_icon="🚗",
    layout="wide"
)

# Affichage header
render_header()

# Formulaires
vehicule_data = render_form_vehicule()
conducteur_data = render_form_conducteur()

# Debug (temporaire)
if any(vehicule_data.values()) and any(conducteur_data.values()):
    st.success("✅ Données complètes saisies !")
    col1, col2 = st.columns(2)
    with col1:
        st.json(vehicule_data)
    with col2:
        st.json(conducteur_data)
