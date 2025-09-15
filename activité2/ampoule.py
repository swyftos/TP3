
#définition de l'objet Ampoule
class Ampoule:
    def __init__(self,id):
        self.id=id
        self.etat='OFF'
        self.OFF=True
        self.ON=False

    def on(self):
        print(f'Dispositif {self.id} allumée')
        self.etat='ON'
        self.ON=True
        self.OFF=False
        self.etat='ON'

    def off(self):
        print(f'Dispositif {self.id} éteinte')
        self.etat='OFF'
        self.OFF=True
        self.ON=False
        self.etat='OFF'