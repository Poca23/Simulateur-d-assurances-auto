import streamlit as st
from components.header import render_header
from components.form_vehicule import render_form_vehicule
from components.form_conducteur import render_form_conducteur
from components.contact_form import render_contact_form
from utils.calcul_tarif import calculate_quote

st.set_page_config(
    page_title="Simulateur Auto - Saint-Pierre Assurances",
    page_icon="🚗",
    layout="wide"
)

render_header()

vehicule_data = render_form_vehicule()
conducteur_data = render_form_conducteur()

data_ready = (vehicule_data.get('marque') and 
              vehicule_data.get('annee') and 
              conducteur_data.get('permis_depuis'))

if data_ready:
    st.divider()
    if st.button("🧮 **Calculer mon devis**", type="primary", use_container_width=True):
        with st.spinner("Calcul en cours..."):
            import time
            time.sleep(1)

            resultat = calculate_quote(vehicule_data, conducteur_data)

            st.success("✅ **Votre devis personnalisé**")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("💰 Tarif annuel", f"{resultat['tarif_annuel']} €")
            with col2:
                st.metric("📅 Tarif mensuel", f"{resultat['tarif_mensuel']} €/mois")
            with col3:
                st.metric("🎯 Économie", "Jusqu'à 30%", delta="vs concurrence")

            quote_data = {
                'vehicule': f"{vehicule_data.get('marque')} {vehicule_data.get('modele')}",
                'age': conducteur_data.get('age'),
                'tarif': resultat['tarif_mensuel'],
                'bonus': conducteur_data.get('bonus_malus')
            }
            render_contact_form(quote_data)

else:
    st.info("ℹ️ Remplissez les informations minimum (marque, année, expérience permis) pour calculer votre devis")
