import pickle
import datetime as dt
from dispositifs import maison

def sauvegarder_etat_pickle():
    horodatage = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    etat_lum = []

    for piece, ampoules in maison.items():
        for ampoule in ampoules:
            etat_lum.append({
                "horodatage": horodatage,
                "piece": piece,
                "id": ampoule.id,
                "etat": ampoule.etat
            })

    with open("etat_lum_piece1", "ab") as fichier:  # "ab" = append binary
        pickle.dump(etat_lum, fichier)

def charger_etat_pickle():
    with open("etat_lum_piece1", "rb") as fichier:
        try:
            while True:
                etat = pickle.load(fichier)
                print(etat)
        except EOFError:
            pass
