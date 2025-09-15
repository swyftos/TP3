from dispositifs import *

def allumer_tout():
    for dispositif in leds + suspension + rubans:
        dispositif.on()

def eteindre_tout():
    for dispositif in leds + suspension + rubans:
        dispositif.off()

def allumer_groupe(groupe):
    for dispositif in groupe:
        dispositif.on()

def eteindre_groupe(groupe):
    for dispositif in groupe:
        dispositif.off()
