from enum import Enum


NOMBRE_DES_DU_JEU = 3
NOMBRE_DE_JETONS_DU_JEU = 21


class TypeComb(Enum):
    """
    Cette classe doit hériter de la classe Enum du module enum de python.
    Elle sert à définir des énumurations qui représente les types des combinaisons possibles.
    Vous devez assigner les valeurs suivantes à chacun des types:
        LE421 = 5
        FICHE = 4
        BARAQUE = 3
        TIERCE = 2
        NENETTE = 1
        AUTRE = 0

    Pour vous familiariser avec les enum, nous vous recommandons de lire la page suivante
    https://docs.python.org/3/library/enum.html
    """
    LE421 = 5
    FICHE = 4
    BARAQUE = 3
    TIERCE = 2
    NENETTE = 1
    AUTRE = 0

    def __ge__(self, other):
        """
        Opérateur de comparaison ( >= ) de la classe. Cette méthode est appelée lorsque vous faites a >= b
        où a et b sont des objets de cette classe.
        :param other: membre à droite de la comparaison
        :return: Si self et other ne sont pas de la même classe, renvoyer None,
        Autrement, True si la valeur de self est supérieure ou égale à celle de other, False sinon

        """
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other):
        """
        Opérateur de comparaison ( > ) de la classe. Cette méthode est appelée lorsque vous faites a > b
        où a et b sont des objets de cette classe.
        :param other: membre à droite de la comparaison
        :return: Si self et other ne sont pas de la même classe, renvoyer None,
        Autrement, True si la valeur de self est supérieure à celle de other, False sinon

        """
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        """
        Opérateur de comparaison ( <= ) de la classe. Cette méthode est appelée lorsque vous faites a <= b
        où a et b sont des objets de cette classe.
        :param other: membre à droite de la comparaison
        :return: Si self et other ne sont pas de la même classe, renvoyer None,
        Autrement, True si la valeur de self est inférieure ou égale à celle de other, False sinon

        """
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other):
        """
        Opérateur de comparaison ( < ) de la classe. Cette méthode est appelée lorsque vous faites a < b
        où a et b sont des objets de cette classe.
        :param other: membre à droite de la comparaison
        :return: Si self et other ne sont pas de la même classe, renvoyer None,
        Autrement, True si la valeur de self est inférieur à celle de other, False sinon

        """
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class Combinaison:
    """
    Cette classe représente les combinaisons de trois (3) dés dans le jeu du 421.
    Les objets de cette classe doivent avoir les attributs suivants:
    representant: une liste en ordre décroissant des valeurs des 3 dés qui représentent la combinaison,
        exemple: [4, 2, 1] pour la combinaison 421, [4, 4, 4] pour la combinaison 444
    valeur: entier représentant la valeur de la combinaison,
        exemple: 6 pour la combinaison 116, 3 pour la combinaison 333
    type: TypeComb représentant le type de la combinaison,
        exemple: TypeComb.FICHE pour la 115, TypeComb.AUTRE pour la 431
    """
    def __init__(self, elements):
        """
        Constructeur de la classe
        :param elements: list ou tuple contenant la valeur des dés qui forment la combinaison,
        vous ne devez pas supposer que les valeurs sont ordonnées par conséquent
        il va falloir les ordornner afin d'initialiser l'attibut représentant de la classe
        N'oubliez pas d'initialiser les attributs valeur et type de la classe.
        """
        self.elements = sorted(elements, reverse=True)
        self.valeur = self.trouver_valeur(self.elements)[0]
        self.type_comb = self.trouver_valeur(self.elements)[1]

    def est_nenette(self):
        """
        Cette méthode permet de déterminer si une combinaison est une nénette ou pas
        :return: True si c'est le cas, False sinon
        """

        if self.elements == [2,2,1]:
            return True
        else:
            return False

    def __lt__(self, other):
        """
        Opérateur de comparaison ( < ) de la classe. Cette méthode est appelée lorsque vous faites A < B
        où A et B sont des combinaisons.
        Une combinaison A est inférieur à une autre combinaison B si
        1 - la valeur de A est inférieur à celle de B
        2 - en cas d'égalité des valeurs, le type de A est inférieur à celui de B
        3 - en cas d'égalité des valeurs et des types, on compare un à un par ordre décroissant les dés de  A  à ceux de B.
        :param other: membre à droite de la comparaison
        :return: True si la combinaison self est inférieure à other, False sinon.

        """
        if self.valeur < self.trouver_valeur(other.elements)[0]:        #Gestion de la valeur de la combinaison
            return True
        elif self.valeur == self.trouver_valeur(other.elements)[0]:
            if self.type_comb.value < self.trouver_valeur(other.elements)[1].value:     #Gestion du type de combinaison
                return True
            elif self.type_comb.value == self.trouver_valeur(other.elements)[1].value:
                if self.elements[0] < other.elements[0]:            #Premier chiffre de la combinaison
                    return True
                elif self.elements[1] < other.elements[1]:          #Deuxieme chiffre de la combinaison
                    return True
                elif self.elements[2] < other.elements[2]:          #Troisième chiffre de la combinaison
                    return True
                else:
                    return False
        else:
            return False

    def __eq__(self, other):
        """
        Opérateur de comparaison ( == ) de la classe. Cette méthode est appelée lorsque vous faites A == B
        où A et B sont des combinaisons.
        Une combinaison A est égale à une autre combinaison B si elles ont le même représentant
        :param other: membre à droite de la comparaison
        :return: True si la combinaison self est égale à other, False sinon.

        """
        if self.elements == other:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Opérateur de comparaison ( > ) de la classe. Cette méthode est appelée lorsque vous faites A > B
        où A et B sont des combinaisons.
        Une combinaison A est supérieur à une autre combinaison B si
        1 - la valeur de A est supérieur à celle de B
        2 - en cas d'égalité des valeurs, le type de A est supérieur à celui de B
        3 - en cas d'égalité des valeurs et des types, on compare avec un à un par ordre décroissant les dés de  A  à ceux de B.
        :param other: membre à droite de la comparaison
        :return: True si la combinaison self est supérieure à other, False sinon.

        """

        if self.valeur > self.trouver_valeur(other.elements)[0]:            #Gestion de la valeur
            return True
        elif self.valeur == self.trouver_valeur(other.elements)[0]:
            if self.type_comb.value > self.trouver_valeur(other.elements)[1].value:     #Gestion du Type
                return True
            elif self.type_comb.value == self.trouver_valeur(other.elements)[1].value:
                if self.elements[0] > other.elements[0]:            #Premier chiffre de la combinaison
                    return True
                elif self.elements[1] > other.elements[1]:          #Deuxieme chiffre de la combinaison
                    return True
                elif self.elements[2] > other.elements[2]:          #Troisieme chiffre de la combinaison
                    return True
                else:
                    return False
        else:
            return False

    def __str__(self):
        """
        Cette méthode retourne une représentation d'une combinaison.
        Cette méthode est appelée lorsque vous faites print(A) où A est une combinaison
        :return: retourne une chaine de caractère qui est la représentation de la combinaison.
            exemple "421", "666", "542", "221"
        """
        chaine = ""
        liste_de_ints = self.elements
        print(chaine.join(str(int) for int in liste_de_ints))

    @staticmethod
    def trouver_valeur(representant):
        """
        Méthode statique de la classe qui permet de retourner la valeur et le type associé à une combinaison de dés
        :param representant: liste de 3 entiers, trié en ordre décroissant
        :return: tuple dont le premier élément est la valeur des dés en paramètre,
        et le second élément est leur type (de type TypeComb)
        """

        if representant == [4,2,1]:
            valeur = 10
            type_comb = TypeComb.LE421

        elif representant == [6,1,1] or representant == [5,1,1] or representant == [4,1,1] or representant == [3,1,1] or representant == [2,1,1]:
            valeur = representant[0]
            type_comb = TypeComb.FICHE

        elif representant == [2,2,2] or representant == [3,3,3] or representant == [4,4,4] or representant == [5,5,5] or representant == [6,6,6] or representant == [1,1,1]:
            if representant == [1,1,1]:
                valeur = 7
            else:
                valeur = representant[0]

            type_comb = TypeComb.BARAQUE

        elif representant == [6,5,4] or representant == [5,4,3] or representant == [4,3,2] or representant == [3,2,1]:
            valeur = 2
            type_comb = TypeComb.TIERCE

        elif representant == [2,2,1]:
            valeur = 4
            type_comb = TypeComb.NENETTE

        else:
            valeur = 1
            type_comb = TypeComb.AUTRE

        tuple = (valeur, type_comb)
        return (tuple)


