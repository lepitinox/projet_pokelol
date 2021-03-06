def choose_integer(a, b):
    """
    Function that asks a user input for a number between a and b inclusively.
    If the user inputs incorrectly, the function displays the error and asks for an input agian
    Parameters
    ----------
    a :  min integer
    b :  max integer

    Returns : the value of the integer chosen by the user
    -------
    """

    #Initial n value
    n = -1

    #input loop as long as number is incorrect
    while n < a or n > b :

        print("Que voulez vous faire? (", a, "-", b, ")")
        n = input()

        try:

            #convert string input to int
            n = int(n)

            # if the input is too big
            if n > b:
                print("Erreur: Entier tres grand! ( > ", b, ")")

            # if the input is too small
            elif n < a:
                print("Erreur: Entier tres petit! ( < ", a, ")")

        except ValueError:

            #Handling string input error
            print("Erreur: \"", n, "\" n'est pas un entier!", sep='')
            print("Veuillez entrer un entier entre", a, "et", b)
            n = -1

    print("Vous avez choisi: ", n)

    return n

if __name__ == "__main__":

    choose_integer(0, 5)