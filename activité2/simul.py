from fonctions import *
from dispositifs import maison
from activite_2 import *
from etat_lum_piece1 import *
import time

def simulation():
    print(" Simulation de gestion des luminaires\n")

    print("Allumage de la Cuisine")
    allumer_piece("Cuisine")
    sauvegarder_etat_csv()
    sauvegarder_etat_pickle()
    time.sleep(1)

    print(" Extinction de la Salle à Manger")
    eteindre_piece("Salle à Manger")
    sauvegarder_etat_csv()
    sauvegarder_etat_pickle()
    time.sleep(1)

    print("Allumage du Séjour")
    allumer_piece("Séjour")
    sauvegarder_etat_csv()
    sauvegarder_etat_pickle()
    time.sleep(1)

    print("Simulation terminée.")

if __name__ == "__main__":
    simulation()
