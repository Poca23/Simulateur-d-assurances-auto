import streamlit as st

def render_form_vehicule():
    """Vehicle information form"""
    st.subheader("🚗 Vehicle Information")

    col1, col2 = st.columns(2)

    with col1:
        marque = st.selectbox(
            "Brand",
            ["Choose...", "Peugeot", "Citroën", "Renault", "Volkswagen", "BMW", "Audi", "Mercedes", "Toyota", "Other"]
        )

        annee = st.selectbox(
            "Vehicle Year",
            ["Choose..."] + [str(i) for i in range(2024, 1990, -1)]
        )

    with col2:
        modele = st.text_input("Model", placeholder="Ex: 308, C4, Clio...")

        carburant = st.selectbox(
            "Fuel Type",
            ["Choose...", "Gasoline", "Diesel", "Hybrid", "Electric", "LPG"]
        )

    return {
        'marque': marque if marque != "Choose..." else None,
        'modele': modele if modele else None,
        'annee': annee if annee != "Choose..." else None,
        'carburant': carburant if carburant != "Choose..." else None
    }
