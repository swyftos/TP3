from fonctions import allumer_piece
from dispositifs import maison
import datetime as dt
import csv

def sauvegarder_etat_csv():
    horodatage = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    lignes = []
    for piece in maison.values():
        for ampoule in piece:
            lignes.append([horodatage, ampoule.id, ampoule.etat])
    with open("etat_lum_piece1.txt", mode="a", newline="") as fichier:
        writer = csv.writer(fichier, delimiter=",")
        writer.writerows(lignes)

# Test
allumer_piece("Cuisine")
sauvegarder_etat_csv()
