import streamlit as st

def calculate_quote(vehicule_data, conducteur_data):
    """Calcul précis de tarif assurance auto avec base de données véhicules"""
    
    tarif_base = 450
    
    coeff_vehicule_base = vehicule_data.get('coeff_base', 1.0)
    
    if vehicule_data.get('annee'):
        age_vehicule = 2024 - int(vehicule_data.get('annee'))
        if age_vehicule <= 2:
            coeff_age_vehicule = 1.3
        elif age_vehicule <= 5:
            coeff_age_vehicule = 1.15
        elif age_vehicule <= 10:
            coeff_age_vehicule = 1.0
        else:
            coeff_age_vehicule = 0.85
    else:
        coeff_age_vehicule = 1.0
    
    age = conducteur_data.get('age', 30)
    if age < 25:
        coeff_age_conducteur = 1.6
    elif age < 35:
        coeff_age_conducteur = 1.2
    elif age < 65:
        coeff_age_conducteur = 1.0
    else:
        coeff_age_conducteur = 1.15
    
    bonus_text = conducteur_data.get('bonus_malus', '1.00')
    if '0.50' in bonus_text:
        coeff_bonus = 0.50
    elif '0.60' in bonus_text:
        coeff_bonus = 0.60
    elif '0.70' in bonus_text:
        coeff_bonus = 0.70
    elif '0.80' in bonus_text:
        coeff_bonus = 0.80
    elif '0.85' in bonus_text:
        coeff_bonus = 0.85
    elif '0.90' in bonus_text:
        coeff_bonus = 0.90
    elif '0.95' in bonus_text:
        coeff_bonus = 0.95
    elif '1.00' in bonus_text:
        coeff_bonus = 1.00
    else:
        coeff_bonus = 1.25
    
    tarif_final = (tarif_base * 
                   coeff_vehicule_base * 
                   coeff_age_vehicule * 
                   coeff_age_conducteur * 
                   coeff_bonus)
    
    vehicule_info = ""
    if vehicule_data.get('marque') and vehicule_data.get('modele'):
        categorie = vehicule_data.get('categorie', 'N/A')
        vehicule_info = f"{vehicule_data['marque']} {vehicule_data['modele']} ({categorie.title()})"
    
    return {
        'tarif_annuel': round(tarif_final),
        'tarif_mensuel': round(tarif_final / 12),
        'vehicule_info': vehicule_info,
        'details': {
            'base': tarif_base,
            'coeff_vehicule': coeff_vehicule_base,
            'coeff_age_vehicule': coeff_age_vehicule,
            'coeff_age_conducteur': coeff_age_conducteur,
            'coeff_bonus': coeff_bonus
        }
    }

def display_quote_results(quote_data):
    """Affichage amélioré des résultats de devis"""
    if quote_data:
        st.success("🎯 **Votre devis personnalisé**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "**Tarif annuel**", 
                f"{quote_data['tarif_annuel']}€",
                help="Prix total pour une année d'assurance"
            )
        
        with col2:
            st.metric(
                "**Tarif mensuel**", 
                f"{quote_data['tarif_mensuel']}€",
                help="Prix mensuel (paiement en 12 fois)"
            )
        
        if quote_data.get('vehicule_info'):
            st.info(f"🚗 **Véhicule** : {quote_data['vehicule_info']}")
        
        with st.expander("🔍 Voir le détail du calcul"):
            details = quote_data['details']
            st.write(f"• **Base tarifaire** : {details['base']}€")
            st.write(f"• **Coefficient véhicule** : {details['coeff_vehicule']}")
            st.write(f"• **Coefficient âge véhicule** : {details['coeff_age_vehicule']}")
            st.write(f"• **Coefficient âge conducteur** : {details['coeff_age_conducteur']}")
            st.write(f"• **Bonus/Malus** : {details['coeff_bonus']}")
