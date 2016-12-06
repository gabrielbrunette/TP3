class Interface:
    def __init__(self):
        pass

    def choisir_des_a_relancer(self, resultat_du_lancer):
        """
        Méthode permettant de choisir selon un résultat de lancé de dés les dés qu'il veut relancer.
        Dans cette méthode, doit demander à l'utilisateur les valeurs de dés à relancer.
        Tant que les valeurs entrées ne sont pas dans la liste en paramètre, vous devez le redemander au joueur.
        :param resultat_du_lancer:  la liste des valeurs des dés où il faut choisir les valeurs de dés  à relancer
        :return: la liste des valeurs des dés choisis pour le relancement
        """
        liste_relancer = []
        resultat_du_lancer_str = []

        for element in resultat_du_lancer:
            resultat_du_lancer_str.append(str(element))         #Conversion des éléments de resultat_du_lancer en str

        relancer = input("Entrer la valeur des dés que vous voulez relancer (ex: 123), 'Entrée' pour ne rien relancer : ") #Conversion en string pour créer une liste
        for element in relancer:
            liste_relancer.append(str(element))                  #Création d'une liste contenant des element str

        i = 0
        while i <= len(liste_relancer) - 1:
            if liste_relancer[i] not in resultat_du_lancer_str:
                relancer = input("Entrer la valeur des dés que vous voulez relancer, les valeurs doivent être valides: ")
                liste_relancer = []
                for element in relancer:
                    liste_relancer.append(str(element))
            else: i += 1

        liste_relancer_int = []
        for element in liste_relancer:                    #Reconvertion en liste d'integer
            liste_relancer_int.append(int(element))

        return list(liste_relancer_int)



    def demander_entree(self, message_demande=""):
        return input(message_demande)

    def afficher(self, message=""):
        print(message)




