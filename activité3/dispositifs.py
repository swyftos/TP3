#****************
#   Cuisine      *
#****************
ac1 = Ampoule('ac1')
ac2 = Ampoule('ac2')
ac3 = Ampoule('ac3')
ac4 = Ampoule('ac4')
cuisine = [ac1, ac2, ac3, ac4]

#****************
# Salle à Manger *
#****************
am1 = Ampoule('am1')
am2 = Ampoule('am2')
am3 = Ampoule('am3')
am4 = Ampoule('am4')
am5 = Ampoule('am5')
salle_a_manger = [am1, am2, am3, am4, am5]

#****************
#   Séjour       *
#****************
leds_droite = [led1, led2, led3]
leds_gauche = [led4, led5, led6]
suspension = [ampoule1, ampoule2, ampoule3, ampoule4, ampoule5]
rubans = [ruban1, ruban2, ruban3]
leds = leds_droite + leds_gauche
sejour = leds + suspension + rubans

maison = {
    "Cuisine": cuisine,
    "Salle à Manger": salle_a_manger,
    "Séjour": sejour
}

