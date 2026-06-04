from abc import *
from personnage import *
from random import randint



class Evenement(ABC):
    def __init  (self):
        pass

    def appliquer(self, perso: Personnage):
        pass


class Incendie(Evenement):
    def __init(self):
        Evenement.__init__()

    def appliquer(self, perso):
        perso.rem_pv(randint(0, 5))

class Soin(Evenement):
    def __init(self):
        Evenement.__init__()

    def appliquer(self, perso):
        heal = randint(1, 10)
        if  perso.PV - heal < 0:
            perso.rem_pv(perso.PV)
        elif perso.PV + heal > perso.__pv_init :
            perso.add_pv(perso.PVMAX)
        else : perso.rem_pv(heal)   

class Tornade(Evenement):
    def __init__(self):
        Evenement.__init__()

    def appliquer(self, perso):
            perso.rem(perso.PV-1)
        
