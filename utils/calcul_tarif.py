def calculate_quote(vehicule_data, conducteur_data):
    """Calcul simple de tarif assurance auto"""
    
    # Tarif de base
    tarif_base = 400
    
    # Coefficients véhicule
    coeff_marque = {
        'Peugeot': 1.0, 'Citroën': 1.0, 'Renault': 1.0,
        'Volkswagen': 1.1, 'Toyota': 1.05,
        'BMW': 1.3, 'Audi': 1.25, 'Mercedes': 1.4
    }
    
    coeff_age_vehicule = 2024 - int(vehicule_data.get('annee', 2020))
    if coeff_age_vehicule <= 3:
        coeff_vehicule = 1.2
    elif coeff_age_vehicule <= 10:
        coeff_vehicule = 1.0
    else:
        coeff_vehicule = 0.8
    
    # Coefficients conducteur
    age = conducteur_data.get('age', 30)
    if age < 25:
        coeff_age = 1.5
    elif age < 65:
        coeff_age = 1.0
    else:
        coeff_age = 1.1
    
    # Bonus/malus simplifié
    bonus_text = conducteur_data.get('bonus_malus', '1.00')
    if '0.50' in bonus_text:
        coeff_bonus = 0.50
    elif '0.60' in bonus_text:
        coeff_bonus = 0.60
    elif '1.00' in bonus_text:
        coeff_bonus = 1.00
    else:
        coeff_bonus = 1.00
    
    # Calcul final
    marque = vehicule_data.get('marque', 'Peugeot')
    tarif_final = (tarif_base * 
                   coeff_marque.get(marque, 1.0) * 
                   coeff_vehicule * 
                   coeff_age * 
                   coeff_bonus)
    
    return {
        'tarif_annuel': round(tarif_final),
        'tarif_mensuel': round(tarif_final / 12),
        'details': {
            'base': tarif_base,
            'coeff_marque': coeff_marque.get(marque, 1.0),
            'coeff_vehicule': coeff_vehicule,
            'coeff_age': coeff_age,
            'coeff_bonus': coeff_bonus
        }
    }
