from personnage import Personnage, Paladin, Combattant, Soigneur, Clerc, Draconien, Berserk, Healer, IA_TET, Fou_Furieux, Guerrier
from arene import *
from evenement import *


Oblivion = Arène(10) 

P1 = Guerrier("Jaaj", 20, 5)
P2 = Clerc("BAPTOU", 15, 13, 10)
P3 = Healer("DERRICK", 5, 15)
P4 = Fou_Furieux("BOM", 5, 5, 0)

Oblivion.ajouter_personnage(P1)
Oblivion.ajouter_personnage(P2)
Oblivion.ajouter_personnage(P3)
Oblivion.ajouter_personnage(P4)

feu_sa_mère = Incendie()
caribe = Tornade()
le_carry = Soin()


Oblivion.appliquer_evenement(feu_sa_mère)
Oblivion.appliquer_evenement(caribe)
Oblivion.appliquer_evenement(le_carry)

Oblivion.combat()




