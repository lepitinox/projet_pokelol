class Combat:

    @staticmethod
    def player_combat_choice(self, p1, p2):
        """

        Parameters
        ----------
        p1 : The user's dresseur (player 1)
        p2 : The opponent's dresseur (player 2)
        Returns
        -------

        """
        poke1 = p1.deck.current_pokemon

        # poke1's ability choices
        ab_choices = []
        for i in range(len(poke1.abilities)):
            ab_choices.append(poke1.abilities[i])

        # number of abilities
        ab_len = len(ab_choices)

        # display poke1's ability choices
        for i in range(ab_choices):
            print(i, ":", ab_choices)

        # display the rest of player choices
        print((ab_len + 1), ": Changer le pokemon")
        print((ab_len + 2), ": Passer votre tour")
        print((ab_len + 3), ": Fuir le combat")

        # choice input
        choice = m_in.choose_integer(0, ab_len + 3)

        if choice < ab_len:
            poke1.attack(poke1.abilities[choice], p2.deck.current_pokemon)

        else:
            if choice == ab_len:
                # TODO: Add this function to Deck class
                p1.deck.change_curr_pokemon()

            elif choice == ab_len + 1:
                # Do nothing (Pass turn)
                pass

            elif choice == ab_len + 2:
                # Kill all deck's pokemon to end the combat loop and quit
                p1.deck.kill_all()

    @staticmethod
    def main_combat(self, p1, p2):
        """

        Parameters
        ----------
        p1 : The user's dresseur (player 1)
        p2 : The opponent's dresseur (player 2)

        Returns
        -------

        """
        # Combat text display between both dresseurs
        print("Combat entre", p1.name, "et", p2.name)

        # ========================================== #
        # ======== Player 1 starting pokemon ======= #
        # ========================================== #

        # Display deck of player1
        print("Les pokemons du", p1.name, ":")
        print(p1.deck.decklist)

        # Choosing the current pokemon for player one
        print("Quel pokemon voulez vous utiliser? (0-2)")
        choice = m_in.choose_integer(0, 2)

        # poke1 is player 1 currently chosen pokemon
        # TODO: create deck.current_pokemon variable
        p1.deck.current_pokemon = p1.deck.decklist[choice]

        # ========================================== #
        # ======== Player 2 starting pokemon ======= #
        # ========================================== #

        # Display deck of player2
        print("Les pokemons du", p2.name, ":")
        print(p2.deck.decklist)

        # Choosing the current pokemon for player one
        print("Quel pokemon voulez vous utiliser? (0-2)")
        choice = m_in.choose_integer(0, 2)

        # poke2 is player's one currently chosen pokemon
        p2.deck.current_pokemon = p2.deck.decklist[choice]

        # ========================================== #
        # =============== Combat loop ============== #
        # ========================================== #

        turn = 1

        # TODO: create a function to check if deck is alive
        while p1.deck.is_alive() and p2.deck.is_alive():

            print("Tour", turn)

            # ============================= #
            # ===== Player one's turn ===== #
            # ============================= #

            print("C'est a", p1.name,"de jouer!")

            #Display all current pokemon attribues
            print(p1.deck.current_pokemon)

            # TODO: combat choices for player1 and 2
            self.player_combat_choice(p1, p2)

            # ============================= #
            # ===== Player two's turn ===== #
            # ============================= #

            #Check if both decks are still alive

            if p1.deck.is_alive() and p2.deck.is_alive():

                print("C'est a", p2.name, "de jouer!")

                # Display all current pokemon attribues
                print(p2.deck.current_pokemon)

                self.player_combat_choice(p2, p1)

                turn += 1