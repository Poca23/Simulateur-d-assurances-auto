# components/header.py
import streamlit as st

def render_header():
    """Affiche l'en-tête Saint-Pierre Assurances"""
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='color: #1f4e79; margin-bottom: 0;'>
            🏢 Saint-Pierre Assurances
        </h1>
        <h3 style='color: #4a90a4; margin: 0;'>
            Simulateur Assurance Auto
        </h3>
        <p style='color: #666; font-style: italic;'>
            Obtenez votre devis personnalisé en 3 minutes
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
