import streamlit as st

def render_contact_form(quote_data):
    """
    Affiche le formulaire de contact avec les données pré-remplies
    Args:
        quote_data: dict contenant les infos de devis
    """
    st.markdown("---")
    st.markdown("### 📞 **Intéressé(e) par cette offre ?**")
    st.markdown("**Notre expert vous recontacte sous 24h !**")
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            nom = st.text_input("👤 Nom *", placeholder="Votre nom")
            email = st.text_input("📧 Email *", placeholder="votre.email@exemple.fr")
            
        with col2:
            prenom = st.text_input("👤 Prénom *", placeholder="Votre prénom")
            telephone = st.text_input("📱 Téléphone *", placeholder="06 12 34 56 78")
    
    message = st.text_area(
        "💬 Message (optionnel)", 
        placeholder="Questions particulières, besoins spécifiques...",
        height=80
    )
    
    if quote_data:
        with st.expander("📋 Résumé de votre simulation", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Véhicule :** {quote_data.get('vehicule', 'N/A')}")
                st.write(f"**Conducteur :** {quote_data.get('age', 'N/A')} ans")
            with col2:
                st.write(f"**Tarif estimé :** {quote_data.get('tarif', 'N/A')}€/mois")
                st.write(f"**Bonus/Malus :** {quote_data.get('bonus', 'N/A')}")
    
    if st.button("📤 **Demander un rendez-vous**", type="primary", use_container_width=True):
        if nom and prenom and email and telephone:
            st.success("✅ **Demande envoyée avec succès !**")
            st.info("📞 **Notre conseiller vous contactera dans les 24h**")
            st.balloons()
        else:
            st.error("⚠️ Veuillez remplir tous les champs obligatoires (*)")
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("📞 **02 47 XX XX XX**")
    with col2:
        st.markdown("📧 **contact@saint-pierre-assurances.fr**")
    with col3:
        st.markdown("📍 **Tours Centre**")
