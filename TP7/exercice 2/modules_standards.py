import os
import math
from datetime import datetime

# 1.lister les fichiers du rep courant
fichiers = os.listdir('.')
print(fichiers)
# 2. Afficher le répertoire courant
current_directory = os.getcwd()
print(f"Répertoire courant : {current_directory}")

#calcule de racine carre
number = float(input("Entrez un nombre : "))
resultat = math.sqrt(number)
print(resultat)

#obtenir la date et l'heure actuelles
maintenant = datetime.now()
print(maintenant)

#format de date
date_format = maintenant.strftime("%Y-%m-%d %H:%M:%S")
print(date_format)
