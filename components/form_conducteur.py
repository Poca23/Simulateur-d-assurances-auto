import streamlit as st

def render_form_conducteur():
    """Formulaire de saisie des informations conducteur"""
    st.subheader("Informations sur le conducteur principal")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Âge du conducteur", 
            min_value=18, 
            max_value=85, 
            value=30,
            help="Âge au moment de la souscription"
        )
        
        permis_depuis = st.selectbox(
            "Permis obtenu depuis",
            ["Choisir...", "Moins de 1 an", "1 à 2 ans", "2 à 5 ans", "5 à 10 ans", "Plus de 10 ans"]
        )
    
    with col2:
        bonus_malus = st.selectbox(
            "Coefficient bonus/malus",
            ["Choisir...", "0.50 (50% bonus)", "0.60", "0.70", "0.80", "0.90", "1.00 (référence)", "1.10", "1.25", "1.50", "2.00+"]
        )
        
        sinistres = st.selectbox(
            "Sinistres responsables (5 dernières années)",
            ["0 sinistre", "1 sinistre", "2 sinistres", "3 sinistres ou plus"]
        )
    
    return {
        'age': age,
        'permis_depuis': permis_depuis if permis_depuis != "Choisir..." else None,
        'bonus_malus': bonus_malus if bonus_malus != "Choisir..." else None,
        'sinistres': sinistres
    }
