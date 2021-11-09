def welcome_menu():
    """
    The welcome menu (first menu that appears when running the game)
    Returns : no return
    -------
    """

    print("#--------------------------------------#")
    print("#        Bienvenue dans POOkemon!      #")
    print("#  Le jeu de Pokemon Oriente Objet :D  #")
    print("#--------------------------------------#")

    print("Quel est votre nom?")

def main_menu():
    """
    The main menu
    Returns : A list of the choices
    -------
    """

    choices = ["0 : Voir vos pokemons", "1 : Changer le deck", "2 : Combattre / Capturer un pokemon",
               "3 : Combattre un autre dresseur", "4 : Creer un autre dresseur", "5 : Quitter"]

    for i in range(len(choices)):
        print(choices[i])

    return choices


if __name__ == "__main__":

    print()