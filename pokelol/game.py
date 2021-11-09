import Menu.menu_output as m_out
import Menu.menu_input as m_in


class Game :

    # TODO : remplir constructeur
    # def __init__(self):

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
        # trainer.pokelist.to_string()

        # we display the main menu and take the user input for his choice
        choices = m_out.main_menu()
        choice = m_in.choose_integer(0, len(choices)-1)
        print(choices[choice])

        # See pokemons choice:
        if choice == 0:

            # TODO: affichage des pokemons du dresseur
            # trainer.pokelist.to_string()
            print()

        if choice == 1:

            # TODO: changement du deck du dresseur
            # trainer.pokelist.change()
            print()

        if choice == 2:

            # TODO: Combattre / Capturer un pokemon
            print()

        if choice == 3:

            # TODO: Combattre un autre dresseur
            self.combat()
            print()

        if choice == 4:
            # TODO : Creer un autre dresseur
            print()

        if choice == 5:

            print("Merci d'avoir joue, au revoir!")

    # TODO : instancier le combat
    def combat(self):

        print()


if __name__ == "__main__":

    g = Game()
    g.start(1)
