from jeu421.interface import Interface
from jeu421.combinaison import *
from jeu421.joueur import Joueur


class Partie:
    """
    Classe représentant une partie de 421. Une partie a les attributs suivants:
    - nb_joueurs: le nombre de joueurs dans la partie
    - joueurs: la liste des joueurs de la partie
    - nb_jetons_du_pot: le nombre de jetons dans le pot de la partie
    - nb_maximum_lancer: le nombre maximum de lancés permis pendant la décharge
    - premier: l'indice du premier joueur pour le tour courant, donc change possiblement
    """
    interface = Interface()


    def __init__(self, nb_joueurs):
        """
        Constructeur de la classe. Vous devez initialisez les attributs
        :param nb_joueurs: le nombre de joueur de la partie
        """
        self.nb_joueurs = nb_joueurs

        self.joueurs = [] #liste qui contient des instancesdelaclasseJoueur,lenombred'élémentsdanslaliste doit en tout temps correspondre à l’attribut nb_joueurs.
        for i in range(self.nb_joueurs):
            self.joueurs.append(Joueur(i))

        self.nb_jetons_du_pot = 21

        self.nb_maximum_lancer = 3

        self.premier = self.determiner_premier_lanceur() #l'indice du premier joueur pour le tour courant, le premier joueur à chaque tour change possiblement en fonction du résultat du tour précédent (le perdant du tour courant devient le premier du tour suivant).



    def determiner_premier_lanceur(self):
        """
        Cette méthode permet de déterminer le premier joueur qui lancera dans la partie.
        Tous les joueurs sont sensé lancer un dé et c'est celui qui a le plus petit nombre qui jouera plus tard le
        premier tour.
        En cas d'égalité, les joueurs concernés répètent l'opération
        L'attribut premier de la classe est initialisé à l'appel de cette méthode
        :return:
        """
        self.interface.afficher("---- DÉTERMINER LE PREMIER LANCEUR ----")
        self.interface.afficher("Joueur --- résultat")
        lancer = []
        for i in range(self.nb_joueurs):
            lancer.append(self.joueurs[i].lancer_des(1))            #Liste des lancers de chaque joueur
        minimum = min(lancer)
        occurence = lancer.count(minimum)                   #Nb d'occurence du minimum dans la liste
        index = lancer.index(minimum)                       #Si une seule occurence du minimum on prend sa valeur d'index (sinon la valeur d'index changera dans le while)
        for element in range(len(self.joueurs)):
            print("Joueur", self.joueurs[element].nom, ":", lancer[element])

        liste_min1 = []
        for i, x in enumerate(lancer):
            if x == minimum:
                liste_min1.append(i)        # Liste contenant les index originals des joueurs qui ont tiré la valeur min

        while occurence > 1:
            self.interface.afficher('\n')
            lancer = []
            for element in liste_min1:
                lancer.append(self.joueurs[element].lancer_des(1))        #Liste du résultat de l'autre lancer
                print("Joueur", self.joueurs[element].nom, ":", lancer[len(lancer)-1])
            minimum = min(lancer)
            occurence = lancer.count(minimum)
            liste_min2 = []
            for i, x in enumerate(lancer):
                if x == minimum:
                    liste_min2.append(i)             #Liste contenant les index qui ont tiré la valeur min au lancé subséquent
            index = []

            for element in liste_min2:
                index.append(liste_min1[element])

        if type(index) is list:             #Pour que la méthode retourne un integer au lieu d'une liste si il a fallu passer par la boucle
            index = int(index[0])
        print("Le premier lanceur de la charge sera le joueur", index)
        return index


    def jouer_tour_premiere_phase(self):
        """
        Cette méthode permet de faire le tour de tous les joueurs et leur permet de jouer pendant la charge.
        Rappel: pendant la charge chaque joueur ne peut lancer les dés qu'une seule fois et le perdant du tour doit
        prendre dans le pot un nombre de jetons égale au nombre de points du gagnant du tour.
        Vous devez afficher à l'interface un récapitulatif des jetons des joueurs après chaque tour
        :return: un tuple d'entier qui correspond à l'index du perdant et celui du gagnant du tour
        """
        #Commence par créer une liste d'index commencant par self.premier et terminant par le perdant de déterminer_premier_lanceur
        global index_perdant

        index = []
        for i in range(self.premier, self.nb_joueurs):
            index.append(i)
        for i in range(0, self.premier):
            index.append(i)

        #self.interface.afficher("----- CHARGE -----")
        #Déterminer le résultat du lancer de tous les participants en ordre et les placer dans la liste "resultat"
        resultat = []
        verif = []
        for x in index:
            self.joueurs[x].jouer_tour(1)
            resultat.append(self.joueurs[x].comb_act)
            verif.append(self.joueurs[x].comb_act.elements)

        #Trouver le gagnant et perdant du tour
        gagnant = resultat[0]
        perdant = resultat[0]
        for i in range(len(resultat)-1):
            if resultat[i+1] > gagnant:         #Trouver gagnant
                gagnant = resultat[i+1]
            index_gagnant = resultat.index(gagnant)         #Index du gagnant dans la liste résultat
            if resultat[i+1] < perdant:             #Trouver perdant
                perdant = resultat[i+1]
            index_perdant = resultat.index(perdant)     #Index du perdant dans la liste resultat

        # Si la combinaison gagnante est tirée plus d'une fois
        if verif.count(gagnant.elements) > 1:
            index_gagnant = []
            for element in verif:
                if element == gagnant.elements:
                    index_gagnant.append(verif.index(element))
            index_gagnant = max(index_gagnant)
        index_gagnant = index[index_gagnant]    #Associer l'index du lancer gagnant à l'index du joueur

        # Si la combinaison perdante est tirée plus d'une fois
        if verif.count(perdant.elements) > 1:
            index_perdant = []
            for element in verif:
                if element == perdant.elements:
                    index_perdant.append(verif.index(element))
            index_perdant = min(index_perdant)
        index_perdant = index[index_perdant]    #Associer l'index du lancer perdant à l'index du joueur

        #Gestion de la nenette
        index_nenette = []
        for element in resultat:
            if element.est_nenette() == True:
                index_nenette.append(resultat.index(element))
                for i in range(len(index_nenette)):
                    index_nenette[i] = index[index_nenette[i]]  # Associer l'index de la nenette à l'index du joueur
                for element in index_nenette:
                    self.joueurs[element].nb_jetons += 2        #Ajouter 2 jetons

        #Ajout et retrait de jetons
        jetons_a_prendre = gagnant.valeur
        self.joueurs[index_perdant].ajouter_jetons(jetons_a_prendre)
        self.nb_jetons_du_pot -= jetons_a_prendre

        #Récapitulatif
        self.interface.afficher("------ RÉCAPITULATIF DU TOUR -------"'\n')
        self.interface.afficher("Joueur ----- jetons")
        for element in self.joueurs:
            print(element)

        tuple = (index_perdant, index_gagnant)
        self.premier = index_perdant
        #print("Le premier lanceur de la décharge sera le joueur", index_perdant)
        return tuple

    def jouer_tour_deuxieme_phase(self):
        """
        Cette méthode permet de faire le tour de tous les joueurs et leur permet de jouer pendant la décharge.
        Rappel: pendant la décharge chaque joueur peut lancer les  dés autant de fois que le premier joueur
        de la charge l'a fait. De plus, le gagnant du tour doit donner un nombre de jetons égale à son nombre de points au perdant du tour.
        Vous devez afficher à l'interface un récapitulatif des jetons des joueurs après le tour
        :return: un tuple d'entier qui correspond à l'index du perdant et celui du gagnant du tour
        """

        # Commence par créer une liste d'index commencant par le perdant de la phase 1(la charge)
        index = []
        for i in range(self.premier, self.nb_joueurs):
            index.append(i)
        for i in range(0, self.premier):
            index.append(i)
        print("Ordre:", index)

        # Déterminer le résultat du lancer de tous les participants en ordre et les placer dans la liste "resultat"
        resultat = []
        verif = []
        maximum_lancer = self.joueurs[index[0]].jouer_tour(3)  # le premier lanceur initie la valeur de maximum_lancer des autres joueurs
        resultat.append(self.joueurs[0].comb_act)               #Résultat du premier lanceur
        verif.append(self.joueurs[0].comb_act.elements)

        for x in index[1:]:
            self.joueurs[x].jouer_tour(maximum_lancer)       # Résultats des autres lanceurs
            resultat.append(self.joueurs[x].comb_act)
            verif.append(self.joueurs[x].comb_act.elements)
        print('\n''verif:',verif)

        # Trouver le gagnant et perdant du tour
        gagnant = resultat[0]
        perdant = resultat[0]
        for i in range(len(resultat) - 1):
            if resultat[i + 1] > gagnant:  # Trouver gagnant
                gagnant = resultat[i + 1]
            index_gagnant = resultat.index(gagnant)  # Index du gagnant dans la liste résultat
            if resultat[i + 1] < perdant:  # Trouver perdant
                perdant = resultat[i + 1]
            index_perdant = resultat.index(perdant)  # Index du perdant dans la liste resultat

        # Si la combinaison gagnante est tirée plus d'une fois
        if verif.count(gagnant.elements) > 1:
            index_gagnant = []
            for element in verif:
                if element == gagnant.elements:
                    index_gagnant.append(verif.index(element))
            index_gagnant = max(index_gagnant)
        index_gagnant = index[index_gagnant]  # Associer l'index du lancer gagnant à l'index du joueur

        # Si la combinaison perdante est tirée plus d'une fois
        if verif.count(perdant.elements) > 1:
            index_perdant = []
            for element in verif:
                if element == perdant.elements:
                    index_perdant.append(verif.index(element))
            index_perdant = min(index_perdant)
        index_perdant = index[index_perdant]  # Associer l'index du lancer perdant à l'index du joueur


        #Le gagnant donne au perdant le nombre de jetons correspondant à la valeur de sa combinaison.
        # Ajout et retrait de jetons
        jetons_a_prendre = gagnant.valeur
        self.joueurs[index_perdant].ajouter_jetons(jetons_a_prendre)
        self.joueurs[index_gagnant].retirer_jetons(jetons_a_prendre)

        # Récapitulatif
        self.interface.afficher("------ RÉCAPITULATIF DU TOUR -------"'\n')
        self.interface.afficher("Joueur ----- jetons")
        for element in self.joueurs:
            print(element)

        #Le joueur qui perd le tour commence le tour suivant
        self.premier = index_perdant

        tuple = (index_perdant, index_gagnant)
        return tuple


    def jouer(self):
        """
        Cette méthode permet de jouer une partie complète de 421.
        La partie doit commencer avec la détermination du joueur qui commence la charge, puis il s'en suit la charge.
        Une fois la charge terminé, la décharge débute par le dernier perdant de la charge.
        Le jeu se termine dès qu'un joueur a tous les jetons de la partie
        """

        #CHARGE
        self.interface.afficher("----- CHARGE -----")
        while self.nb_jetons_du_pot > 0:        #Tant qu'il  y a des jetons dans le pot on rejout un tour de charge
            self.jouer_tour_premiere_phase()

        #DÉCHARGE
        self.interface.afficher("----- DÉCHARGE -----")

        for element in self.joueurs:                        #On enleve les joueurs qui n'ont pas pigé de jetons durant la charge
            if self.verifier_gagnant(element) == True:
                self.retirer_joueur(int(element.nom))
                print("Le joueur", element.nom, "a été retiré")

        while len(self.joueurs) > 1:            #Tant qu'il ne reste plus qu'un joueur dans la partie on rejout un tour
            self.jouer_tour_deuxieme_phase()
            for element in self.joueurs:
                if self.verifier_gagnant(element) == True:
                    self.retirer_joueur(int(element.nom))           #Retirer les joueurs gagnants
                    print("Le joueur", element.nom, "a été retiré")


    def verifier_gagnant(self, joueur):
        """
        Cette méthode permet de déterminer si un joueur a gagné la partie, i.e qu'il n'a plus de jetons
        :param joueur: le joueur en question
        :return: True si le joueur n'a plus de jetons, False sinon
        """

        if joueur.nb_jetons == 0:
            return True

    def verifier_perdant(self, joueur):
        """
        Cette méthode permet de déterminer si un joueur a perdu la partie
        :param joueur: le joueur en question
        :return: True si le joueur a tous les jetons de la partie, False sinon
        """
        if joueur.nb_jetons == 21:
            return True

    def retirer_joueur(self, position):
        """
        Retirer un joueur du jeu
        :param position: la position du joueur dans la liste des joueurs à retirer
        :return:
        """
        self.joueurs.remove(self.joueurs[position])

    def afficher_recapitulatif(self):
        """
        Affiche un tableau récapitulatif de la partie
        """

        raise NotImplementedError("Partie : afficher_recapitulatif ")


