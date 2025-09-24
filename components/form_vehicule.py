import streamlit as st
import json
import os

def load_vehicles_db():
    """Charge la base de données des véhicules"""
    try:
        with open('data/vehicules.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Base de données véhicules introuvable")
        return {}

def render_form_vehicule():
    """Formulaire de saisie des informations véhicule avec vraie base de données"""
    st.subheader("Informations sur votre véhicule")
    
    vehicles_db = load_vehicles_db()
    
    col1, col2 = st.columns(2)

    with col1:
        marques_list = ["Choisir..."] + sorted(list(vehicles_db.keys()))
        marque = st.selectbox("Marque", marques_list)

        annee = st.selectbox(
            "Année du véhicule",
            ["Choisir..."] + [str(i) for i in range(2024, 1990, -1)]
        )

    with col2:
        if marque != "Choisir..." and marque in vehicles_db:
            modeles_list = ["Choisir..."] + sorted(list(vehicles_db[marque].keys()))
            modele = st.selectbox("Modèle", modeles_list)
        else:
            modele = st.selectbox("Modèle", ["Choisir..."])

        carburant = st.selectbox(
            "Carburant",
            ["Choisir...", "Essence", "Diesel", "Hybride", "Électrique", "GPL"]
        )

    vehicle_data = {
        'marque': marque if marque != "Choisir..." else None,
        'modele': modele if modele != "Choisir..." else None,
        'annee': annee if annee != "Choisir..." else None,
        'carburant': carburant if carburant != "Choisir..." else None
    }
    
    if (vehicle_data['marque'] and vehicle_data['modele'] and 
        vehicle_data['marque'] in vehicles_db and 
        vehicle_data['modele'] in vehicles_db[vehicle_data['marque']]):
        
        vehicle_info = vehicles_db[vehicle_data['marque']][vehicle_data['modele']]
        vehicle_data.update({
            'coeff_base': vehicle_info['coeff_base'],
            'categorie': vehicle_info['categorie'],
            'puissance_fiscale': vehicle_info['puissance_fiscale']
        })

    return vehicle_data
