import Menu.menu_output as m_out
import Menu.menu_input as m_in
import combat
import trainer

class Game :

    # TODO : remplir constructeur
    def __init__(self):
        pass

    def start(self, trainer):
        """
        Initialize trainer name and print the main menu

        Parameters
        ----------
        trainer : Pokemon trainer

        Returns
        -------

        """
        m_out.welcome_menu()

        # TODO: saisi nom du dresseur
        # trainer.name = input()

        # TODO : affichage des pokemons du dresseur
        # print(trainer.pokelist)

        # we display the main menu and take the user input for his choice
        choices = m_out.main_menu()
        choice = m_in.choose_integer(0, len(choices)-1)
        print(choices[choice])

        # See pokemons choice:
        if choice == 0:

            # TODO: affichage des pokemons du dresseur
            # print(trainer.pokelist)
            pass

        if choice == 1:

            # TODO: changement du deck du dresseur
            trainer.deck.change()
            pass

        if choice == 2:

            # TODO: Combattre / Capturer un pokemon
            pass

        if choice == 3:

            # TODO: Combattre un autre dresseur
            combat.main_combat()
            pass

        if choice == 4:
            # TODO : Creer un autre dresseur
            pass

        if choice == 5:

            print("Merci d'avoir joué, au revoir!")

if __name__ == "__main__":

    g = Game()
    g.start(1)
