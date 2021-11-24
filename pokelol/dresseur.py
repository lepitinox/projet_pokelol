#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

from pokelol.Menu.menu_input import choose
from pokelol.pokemon import Pokemon


class Deck:
    def __init__(self, pokemon_list: List[Pokemon]):
        self.pokemon_list = pokemon_list

    def change_deck(self):
        choice = choose("Which Pokemon do you want to replace ?", self.pokemon_list)
        self.pokemon_list.pop(choice)

        print("")

    def __str__(self):
        print("Your Deck :")
        for j, i in enumerate(self.pokemon_list):
            print(f"{j}/ {i}")


class Trainer:
    def __init__(self, name, pokelist, deck):
        self.name = name
        self.pokelist = pokelist
        self.deck = deck


class Player(Trainer):
    def __init__(self):
        name = str(input("what's your name ?\n"))
        # TODO (aducourthial): selection of the pokelist and deck
        pokelist = None
        deck = None
        super().__init__(name, pokelist, deck)

    def change_deck(self):
        self.deck.change_deck()

