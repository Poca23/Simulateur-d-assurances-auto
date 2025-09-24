# README - Simulateur d'Assurance Auto

## Description

Application web de simulation de devis d'assurance automobile. Cette solution permet aux clients de générer rapidement des estimations tarifaires personnalisées et de comparer différentes formules d'assurance.

## Fonctionnalités

- Formulaire interactif de saisie des données véhicule et conducteur
- Calcul automatique des tarifs selon le profil de risque
- Comparaison visuelle des offres avec graphiques
- Recommandations personnalisées selon le profil client
- Interface responsive adaptée mobile et desktop
- Système de bonus/malus intégré

## Technologies utilisées

- **Python 3.11+**
- **Streamlit** : Interface utilisateur web
- **Pandas** : Traitement et analyse des données
- **Plotly** : Visualisations graphiques interactives

## Installation

### Prérequis
- Python 3.11 ou version supérieure
- Git

### Étapes d'installation

```bash
# Cloner le repository
git clone https://github.com/Poca23/Simulateur-d-assurances-auto.git
cd simulateur_assurance

# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

### Démarrage de l'application
```bash
streamlit run app.py
```

L'application sera accessible à l'adresse : http://localhost:8501

### Navigation
1. Renseigner les informations du véhicule
2. Saisir le profil du conducteur
3. Préciser la localisation
4. Consulter les résultats et recommandations
5. Utiliser le formulaire de contact pour finaliser

## Structure du projet

```
simulateur_assurance/
├── app.py                     # Point d'entrée principal
├── components/                # Composants interface utilisateur
├── data/                      # Données de référence
├── utils/                     # Logique métier et calculs
├── styles/                    # Styles et design
├── config/                    # Configuration application
└── requirements.txt           # Dépendances Python
```

## Développement

### Ajout de nouvelles fonctionnalités
- Chaque composant est modulaire et indépendant
- Les fichiers de données sont au format JSON pour faciliter les modifications
- La logique de calcul est centralisée dans le dossier utils/

### Tests locaux
```bash
# Vérifier le bon fonctionnement
streamlit run app.py

# Tester les composants individuellement
python -m pytest tests/ (si implémenté)
```

## Contribution

Pour contribuer au projet :
1. Créer une branche feature depuis main
2. Développer la fonctionnalité
3. Tester localement
4. Créer une pull request

## Support

Pour toute question technique ou demande d'évolution, contacter l'équipe de développement.

## Licence

Proprietary software

---

**Version actuelle :** 1.0.0  
**Dernière mise à jour :** Septembre 2025

---