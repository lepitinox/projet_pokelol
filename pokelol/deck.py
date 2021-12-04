

class Deck:

    def __init__(self):

        self.decklist = [] #pokemon list
        self.current_pokemon = None #the pokemon that is being used for combat

        # TODO: add tostring option for deck

    def kill_all(self):
        """
        Sets all pokemons' current hp in deck to 0
        Returns
        -------

        """

        #loop to kill all pokemons in the deck
        for i in range (len(self.decklist)):
            self.decklist[i].hp = 0

    def change(self):
        """
        Changes the pokemons in the deckist
        Returns
        -------

        """
        pass

    def change_curr_pokemon(self):
        """
        Changes the current pokemon used in combat
        Returns
        -------

        """
        pass

    def is_alive(self):
        """
        Checks whether all pokemons in the decklist are alive

        Returns True or False
        -------
        """

        bool = False

        for i in range(self.decklist):

            #if at least one pokemon is alive, we return true
            if (self.decklist[i].hp>0):
                bool = True

        return bool