from typing import List, Union

from pokelol.Menu.menu_input import choose
from pokelol.interface import multiple_choices_no_back
from pokelol.pokemon import Pokemon


class Deck:

    def __init__(self, pokemon_list: List[Pokemon]):
        self.decklist = pokemon_list
        self.current_pokemon = pokemon_list[0]

    def change_deck(self):
        choice = choose("Which Pokemon do you want to replace ?", self.decklist)
        self.decklist.pop(choice)

    def _change_one_pokemon(self, pokemon_to_change: Union[Pokemon, str], new_pokemon: Pokemon) -> bool:
        """
        change pokemon_to_change for new_pokemon, if pokemon_to_change not in deck will return False
        Parameters
        ----------
        pokemon_to_change : Union[Pokemon, str]
            if a Pokemon type is given, will look for the exact same object, if str, will search using '_find_pokemon'

        new_pokemon : Pokemon
            the new Pokemon to be added to the deck


        Returns
        -------
        bool
        true if successfully changed the Pokemon else false
        """
        if isinstance(pokemon_to_change, str):
            pokemon_to_change = self._find_pokemon(pokemon_to_change)
            if pokemon_to_change is None:
                return False

    def __iter__(self):
        for i in self.decklist:
            yield i

    def __str__(self):
        return "\n".join([str(i) for i in self.decklist])

    def heal_all(self):
        for i in self.decklist:
            i.hp = i.max_hp
            i.ap = i.max_ap

    def kill_all(self):
        """
        Sets all Pokemon' current hp in deck to 0
        Returns
        -------

        """

        # loop to kill all pokemons in the deck
        for i in range(len(self.decklist)):
            self.decklist[i].hp = 0

    def change(self, old, new):
        """
        Changes the pokemons in the deckist
        Returns
        -------

        """

        name = self._find_pokemon(old.name)
        self.decklist.pop(self.decklist.index(name))
        self.decklist.append(new)

    def change_pokemon(self):
        choices = {str(i): i for i in self.decklist if i.hp > 0}
        if len(choices) == 0:
            self.current_pokemon = None
            return
        poke = multiple_choices_no_back(choices, "Quel pokemon voulez vous utiliser?")
        self.change_curr_pokemon(poke)

    def change_curr_pokemon(self, poke: Pokemon):
        """
        Changes the current pokemon used in combat
        Returns
        -------

        """
        if poke in self.decklist:
            self.current_pokemon = poke
        else:
            print("this pokemon is not in your deck, using last pokemon")

    def is_alive(self):
        """
        Checks whether all pokemons in the decklist are alive

        Returns True or False
        -------
        """
        for pokemon in self.decklist:
            # if at least one pokemon is alive, we return true
            if pokemon.hp > 0:
                return True
        return False

    def _find_pokemon(self, pokemon_to_change: str):
        """
        find a Pokemon by name in self.decklist, if not in it return None, if multiple of same name return None

        Parameters
        ----------
        pokemon_to_change :str
            name of the pokemon

        Returns
        -------

        """
        ret = None
        for p in self.decklist:
            if p.name.lower() == pokemon_to_change.lower():
                if ret is not None:
                    return None
                ret = p
        return ret
