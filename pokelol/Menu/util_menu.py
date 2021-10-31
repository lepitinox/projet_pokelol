def choix_numero(a, b):
    """
    Une fonction qui demande a l'utilisateur de saisir un chiffre entre a et b (inclusif).
    Si l'utilisateur repond incorrectement, la fonction redemande une entree.
    Parameters
    ----------
    a : Entier min
    b : Entier max

    Returns
    -------
    """

    #valeur initiale de n
    n = -1

    #boucle d'entree
    while n < a or n > b :

        print("Que voulez vous faire? (", a, "-", b, ")")
        n = input()

        #si l'entree n'est pas un chiffre
        if not n.isnumeric():
            print("Erreur: \"", n, "\" n'est pas un chiffre!",sep='')
            print("Veuillez entrer un chiffre entre", a, "et ", b)
            n = -1

        n = int(n)

        #si l'entree est plus grand que chiffre max (b)
        if n > b:
            print("Erreur: chiffre tres grand! ( > ", b, ")")

        #si l'entree est plus petit que chiffre min (a)
        if n < a:
            print("Erreur: chiffre tres petit! ( < ", a, ")")

    print("Vous avez choisi: ", n)

if __name__ == "__main__":

    choix_numero(0, 5)