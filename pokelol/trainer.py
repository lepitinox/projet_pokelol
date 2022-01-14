#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from typing import Union

from deck import Deck
from pokelol.pokemon import Pokemon
from interface import print, multiple_choices_no_back, input


class Trainer:
    """
    Abstract class, used to define methods for Player and Npc
    """
    __existing_trainer = {}

    def __init__(self, nb_poke: int = 6):
        self.poke_list = None
        self.generate_random_pokemon_list(nb_poke)

    def generate_random_pokemon_list(self, list_size: int):
        """
        generate a random list of Pokemon of length list_size and set poke_list to it

        Parameters
        ----------
        list_size : int (optional)
            length of the Pokemon list

        """
        self.poke_list = [Pokemon.generate_random_pokemon(1) for _ in range(list_size)]


class Player(Trainer):
    def __init__(self, name: Union[str, None] = None):
        if name is None:
            name = str(input("Quel est votre nom?"))
        self.name = name
        super().__init__()
        self.deck = Deck(self.poke_list[:3])

    def change_deck(self):
        """
        replace a pokemon of the deck
        Returns
        -------

        """

        choices = {str(i): i for i in self.deck.decklist}
        ress = multiple_choices_no_back(choices, "Quel pokémon voulez vous changer ?")

        ok_pok = [i for i in self.poke_list if i not in self.deck.decklist]

        choices = {str(i): i for i in ok_pok}
        res = multiple_choices_no_back(choices, "Quel pokémon ajouter ?")
        self.deck.change(ress, res)

    def show_pokemons(self):
        """
        display all pokemons
        """
        for pokemon in self.poke_list:
            if pokemon in self.deck:
                print(f"In deck : {pokemon}")
            else:
                print(f"Not in deck : {pokemon}")

    def capture(self, p2):
        """
        Function to calculate whether a pokemon will be captured or not.

        Parameters

        ------------
        poke_capt: The pokemon being captured

        Return
        -----------
        Boolean: True or false whether the pokemon got captured or not
        """
        # V is current health of the pokemon
        v = p2.deck.current_pokemon.hp
        # Vmax is the maximum health of the pokemon
        v_max = p2.deck.current_pokemon.max_hp
        # The probability of capture
        proba = 4 * (0.2 - v / v_max)

        # Random number between 0 and 1
        rand = random.random()

        if rand <= proba:
            self.poke_list.append(p2.deck.decklist[0])
            return True
        else:
            return False
        return


class WildPoke(Trainer):
    def __init__(self, ia):
        super().__init__(nb_poke=1)
        self.deck = Deck(self.poke_list)
        # use Pokemon name as trainer name
        self.name = self.poke_list[0].name
        self.ia = ia


class Npc(Trainer):
    npc_names = ["Jcvd", "Mozinor"]

    def __init__(self, ia):
        self.name = random.choice(self.npc_names)
        super().__init__()
        self.deck = Deck(self.poke_list[:3])
        self.ia = ia

    @classmethod
    def _generate_random_npc(cls):
        pass
