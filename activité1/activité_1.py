from fonctions import *
from dispositifs import *


allumer_tout()


eteindre_tout()


allumer_groupe(rubans)


eteindre_groupe(leds_gauche)


def etat_all():
    print("État des luminaires :")
    for dispositif in leds + suspension + rubans:
        print(f"{dispositif.id} : {dispositif.etat}")

etat_all()

