import streamlit as st

def render_form_vehicule():
    """Formulaire de saisie des informations véhicule"""
    st.subheader("🚗 Informations sur votre véhicule")
    
    col1, col2 = st.columns(2)
    
    with col1:
        marque = st.selectbox(
            "Marque",
            ["Choisir...", "Peugeot", "Citroën", "Renault", "Volkswagen", "BMW", "Audi", "Mercedes", "Toyota", "Autre"]
        )
        
        annee = st.selectbox(
            "Année du véhicule",
            ["Choisir..."] + [str(i) for i in range(2024, 1990, -1)]
        )
    
    with col2:
        modele = st.text_input("Modèle", placeholder="Ex: 308, C4, Clio...")
        
        carburant = st.selectbox(
            "Carburant",
            ["Choisir...", "Essence", "Diesel", "Hybride", "Électrique", "GPL"]
        )
    
    return {
        'marque': marque if marque != "Choisir..." else None,
        'modele': modele if modele else None,
        'annee': annee if annee != "Choisir..." else None,
        'carburant': carburant if carburant != "Choisir..." else None
    }
