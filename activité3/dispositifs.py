from ampoule import Ampoule

# Initialisation des dispositifs
led1 = Ampoule('led1')
led2 = Ampoule('led2')
led3 = Ampoule('led3')
led4 = Ampoule('led4')
led5 = Ampoule('led5')
led6 = Ampoule('led6')

ampoule1 = Ampoule('ampoule1')
ampoule2 = Ampoule('ampoule2')
ampoule3 = Ampoule('ampoule3')
ampoule4 = Ampoule('ampoule4')
ampoule5 = Ampoule('ampoule5')

ruban1 = Ampoule('ruban1')
ruban2 = Ampoule('ruban2')
ruban3 = Ampoule('ruban3')

# Groupes pour le séjour
leds_droite = [led1, led2, led3]
leds_gauche = [led4, led5, led6]
suspension = [ampoule1, ampoule2, ampoule3, ampoule4, ampoule5]
rubans = [ruban1, ruban2, ruban3]
leds = leds_droite + leds_gauche
sejour = leds + suspension + rubans

# Cuisine
ac1 = Ampoule('ac1')
ac2 = Ampoule('ac2')
ac3 = Ampoule('ac3')
ac4 = Ampoule('ac4')
cuisine = [ac1, ac2, ac3, ac4]

# Salle à manger
am1 = Ampoule('am1')
am2 = Ampoule('am2')
am3 = Ampoule('am3')
am4 = Ampoule('am4')
am5 = Ampoule('am5')
salle_a_manger = [am1, am2, am3, am4, am5]

# Dictionnaire global
maison = {
    "Cuisine": cuisine,
    "Salle à Manger": salle_a_manger,
    "Séjour": sejour
}
