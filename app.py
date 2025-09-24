import streamlit as st
from components.header import render_header
from components.form_vehicule import render_form_vehicule
from components.form_conducteur import render_form_conducteur
from utils.calcul_tarif import calculate_quote

st.set_page_config(
    page_title="Auto Simulator - Saint-Pierre Insurance",
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
    if st.button("🧮 **Calculate Quote**", type="primary", use_container_width=True):
        with st.spinner("Calculating..."):
            import time
            time.sleep(1)
            
            resultat = calculate_quote(vehicule_data, conducteur_data)
            
            st.success("✅ **Your personalized quote**")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("💰 Annual Premium", f"{resultat['tarif_annuel']} €")
            with col2:
                st.metric("📅 Monthly Premium", f"{resultat['tarif_mensuel']} €/month")
            with col3:
                st.metric("🎯 Savings", "Up to 30%", delta="vs competition")
            
            st.info("📞 **Contact Saint-Pierre Assurances** to finalize your quote and get personalized advice!")
else:
    st.info("ℹ️ Fill minimum information (brand, year, license experience) to calculate your quote")
