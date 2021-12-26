#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from typing import List, Union

from pokelol.Menu.menu_input import choose
from pokelol.pokemon import Pokemon
from deck import Deck


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
        self.poke_list = [Pokemon.generate_random_pokemon(0) for _ in range(list_size)]


class Player(Trainer):
    def __init__(self, name: Union[str, None] = None):
        if name is None:
            name = str(input("Quel est votre nom?\n"))
        self.name = name
        super().__init__()
        self.deck = Deck(self.poke_list[:3])

    def change_deck(self):
        print(self.deck)
        # TODO (aducourthial): Crée un obj/funcv pour faire des choix dans une list (et verif de type)
        a = int(input("le quelle ?"))
        popke = self.deck.decklist[a]
        s = 0
        rt = {}
        for pokemon in self.poke_list:
            if pokemon not in self.deck:
                print(f"{s}: {pokemon}")
                rt[s] = pokemon
                s += 1

        ok = int(input("pour ?"))
        self.deck.change(popke, rt[ok])

    def show_pokemons(self):
        """
        display all pokemons
        """
        for pokemon in self.poke_list:
            if pokemon in self.deck:
                print(f"In deck : {pokemon}")
            else:
                print(f"Not in deck : {pokemon}")


class WildPoke(Trainer):
    def __init__(self):
        super().__init__(nb_poke=1)
        self.deck = Deck(self.poke_list)
        # use Pokemon name as trainer name
        self.name = self.poke_list[0].name


class Npc(Trainer):
    npc_names = ["Jcvd", "Mozinor"]

    def __init__(self):
        self.name = random.choice(self.npc_names)
        super().__init__()
        self.deck = Deck(self.poke_list[:3])

    @classmethod
    def _generate_random_npc(cls):
        pass
