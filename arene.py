from ..personnage import *
from evenement import *
from abc import ABC
from random import randint




class Arène():
    def __init__(self, nb_tours_max):
        self.__personnages = []
        self.__evenements = []
        self.__nb_tours_max = nb_tours_max
        self.__nb_tours = 0
        self.__evenement_courant = Evenement



    def ajouter_personnage(self, perso: Personnage):
        self.__personnages.append(perso)   

    def ajouter_evenement(self, evenement : Evenement):
        self.__evenements.append(evenement)

    def personnage_aleatoire(self):
        return self.__personnages[randint(0,len(self.__personnages)-1)]

    def selectionner_evenement(self):
        event = self.__evenements[randint(0,len(self.__evenements)-1)]
        self.__evenement_courant = event

    def appliquer_evenement(self):
        for perso in self.__personnages:
            self.__evenement_courant.appliquer(perso)
    
    def tour(self):
        self.appliquer_evenement()
        combattants = self.__personnages
        attaquant = self.personnage_aleatoire
        combattants.pop(attaquant)
        cible = self.personnage_aleatoire
        attaquant.combattre(cible)

    def gagnant(self): #départage les gaganant attends qu'il y en ai que un seul
        nbgagnant=0  
        gagnant = None
        for perso in self.__personnages:
            if (perso.PV > 0):
                gagnant = perso
                nbgagnant +=1
        if nbgagnant == 1 :
            return gagnant        
        
    def combat(self):
        while(self.gagnant == None or self.__nb_tours == self.__nb_tours_max):
            self.tour()    


          

