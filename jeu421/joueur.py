from jeu421.interface import Interface
from jeu421.combinaison import *
from random import randint


class Joueur:
    """
    Classe représentant un joueur de 421. Un joueur a les attributs
    - nom: son nom
    - nb_jetons: son nombre de jetons, entier entre 0 et 21
    - combinaison actuelle: un objet de la classe Combinaison
    La classe a un attribut static interface qui est l'interface de communication entre les joueurs et le programme

    """
    interface = Interface()


    def __init__(self, nom):
        """
        Constructeur de la classe, doit initialiser le nom du joueur à la valeur passée en paramètre.
        Le nombre de jetons à zéro, et la combinaison_actuelle à None
        :param nom: nom du joueur
        """
        self.nom = str(nom)
        self.nb_jetons = 0
        self.comb_act = None

    def lancer_des(self, nombre_des):
        """
        Méthode permettant à un joeur de lancer dés
        :param nombre_des: nombre de dés à lancer
        :return: une liste de longueur nombre_des contenant les valeurs de chaque dés selon le lancé
        """
        d1 = randint(1,6)
        d2 = randint(1,6)
        d3 = randint(1,6)
        if nombre_des == 1:
            resultat = [d1]
        elif nombre_des == 2:
            resultat = [d1, d2]
        elif nombre_des == 3:
            resultat = [d1, d2, d3]
        return resultat

    def jouer_tour(self, nb_maximum_lancer=3):
        """
        Cette méthode permet à un joueur de jouer lorsque c'est son tour dans une partie, en lançant les dés.
        Vous devez demandez au joueur de lancer des dés, de choisir les dés à relancer et puis changer l'attribut combinaison actuelle du
        :param nb_maximum_lancer: le nombre maximum de lancés auquel le joueur a droit lors de ce tour.
        :return: retourne le nombre de lancés que le joueur a fait.
        """
        global nb_lancer
        print('\n'"Joueur", self.nom)
        self.interface.afficher("Appuyer sur 'Entrée' pour lancer les dés.")
        self.interface.demander_entree("")
        joueur = Joueur(self.nom)
        comb_courante = joueur.lancer_des(3)
        if nb_maximum_lancer == 1:
            self.comb_act = Combinaison(comb_courante)

        print("Joueur", self.nom, "résultat:", sorted(comb_courante, reverse=True))

        nb_lancer = 1
        while nb_lancer < nb_maximum_lancer:
            #nb_lancer += 1
            if nb_maximum_lancer == 1:                          #La boucle ne s'exécute pas si l'utilisateur a droit à un seul lancer
                break
            relancer = self.interface.choisir_des_a_relancer(comb_courante)     #Demande a l'utilisateur quels dés il veut relancer
            for element in relancer:
                comb_courante.remove(element)                   #Enleve la valeur qu on veut relancer de la combinaison actuelle
            if len(relancer) == 0:                              #Si rien n'est entrée on quitte la boucle
                break
            lancer = joueur.lancer_des(len(relancer))         #Lance autant de dés que longueur de relancer1
            for element in lancer:                              #Ajoute le résultat du lancer à la combinaison courante
                comb_courante.append(element)

            print("Joueur", self.nom, "résultat:", sorted(comb_courante, reverse=True))
            nb_lancer += 1

        else: self.comb_act = Combinaison(comb_courante)
        return nb_lancer

    def ajouter_jetons(self, nb_jetons):
        """
        Cette méthode permet d'ajouter un nombre de jetons à ceux déjà détenus par le joueur
        :param nb_jetons: nombre de jetons à ajouter
        :return aucun
        """
        self.nb_jetons += nb_jetons

    def retirer_jetons(self, nb_jetons):
        """
        Cette méthode permet de retirer un nombre de jetons de ceux détenus par le joueur
        :param nb_jetons: nombre de jetons à retirer
        :return aucun
        """
        self.nb_jetons -= nb_jetons

    def __str__(self):
        """
        Cette méthode retourne une représentation d'un joueur. le format est "nom_du_joueur - nombre_de_jetons"
        Cette méthode est appelée lorsque vous faites print(A) où A est un joueur
        :return: retourne une chaine de caractère qui est une représentation.
            Exemple: "Joueur1 - 12"
        """
        chaine = "   " + str(self.nom) + "   -----   " + str(self.nb_jetons)
        return chaine

    def __le__(self, other):
        """
        Comparaison ( <= ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est inférieur ou égal à celui de other
        """
        if self.nb_jetons <= other:
            return True

    def __ge__(self, other):
        """
        Comparaison ( >= ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est supérieur ou égal à celui de other
        """
        if self.nb_jetons >= other:
            return True

    def __lt__(self, other):
        """
        Comparaison ( < ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est inférieur à celui de other
        """
        if self.nb_jetons < other:
            return True

    def __gt__(self, other):
        """
        Comparaison ( > ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est supérieur à celui de other
        """
        if self.nb_jetons > other:
            return True

    def __eq__(self, other):
        """
        Comparaison ( == ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est égal à celui de other
        """
        if self.nb_jetons == other:
            return True



