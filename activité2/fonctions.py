from dispositifs import maison

def allumer_tout():
    for dispositif in leds + suspension + rubans:
        dispositif.on()

def allumer_piece(nom_piece):
    if nom_piece in maison:
        for ampoule in maison[nom_piece]:
            ampoule.on()
            
            
def eteindre_tout():
    for dispositif in leds + suspension + rubans:
        dispositif.off()

def allumer_groupe(groupe):
    for dispositif in groupe:
        dispositif.on()

def eteindre_groupe(groupe):
    for dispositif in groupe:
        dispositif.off()


#allumer_piece("Cuisine")
#etat_maison()
#eteindre_piece("Séjour")
#allumer_maison()

