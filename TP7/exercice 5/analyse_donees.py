
# analyse_donnees.py
import pandas as pd

# 1. Lire le fichier CSV
file_path = 'contacts.csv'  # Assure-toi que le fichier est dans le bon répertoire
data = pd.read_csv(file_path)

# 2. Afficher les cinq premières lignes du fichier
print("Les cinq premières lignes du fichier CSV:")
print(data.head())

# 3. Calculer et afficher la moyenne d'un champ numérique (ici, l'âge)
moyenne_age = data['age'].mean()
print(f"\nLa moyenne d'âge des employés est: {moyenne_age}")
