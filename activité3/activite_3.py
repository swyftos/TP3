from dispositifs import maison

def allumer_piece(nom_piece):
    if nom_piece in maison:
        for ampoule in maison[nom_piece]:
            ampoule.on()

def eteindre_piece(nom_piece):
    if nom_piece in maison:
        for ampoule in maison[nom_piece]:
            ampoule.off()

def allumer_maison():
    for piece in maison.values():
        for ampoule in piece:
            ampoule.on()

def eteindre_maison():
    for piece in maison.values():
        for ampoule in piece:
            ampoule.off()

def etat_maison():
    print("État des luminaires par pièce :")
    for nom_piece, ampoules in maison.items():
        print(f"\n{nom_piece} :")
        for ampoule in ampoules:
            print(f"  {ampoule.id} : {ampoule.etat}")

