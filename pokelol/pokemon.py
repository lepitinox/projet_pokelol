#!/usr/bin/python
# -*- coding: utf-8 -*-
import pokemon as pokemon

from pokelol.poketools import txt_parser,txt_openner
from env_loader import POKEMON_PATH
import random

class Pokemon:
    poke_list = txt_parser(txt_openner(POKEMON_PATH))

    def __init__(self):
        self.name = None
        self.p_type = None
        self.max_hp = None
        self.max_ap = None
        self.hp = None
        self.ap = None
        self.abillities = None
        self.lvl = None
        self.xp = None
        self.ap_regen = None
        self.resistance = None

    """ Pokemon init """
    def init_abillities(self):
        pass

    def generate_random_pokemon(self, lvl: int):
        """
        Create a random pokemon at level lvl
        Parameters
        ----------
        lvl: int
            lvl of the pokemon

        Returns
        -------
        None
        # >>> Pokemon().generate_random_pokemon(1)
        """
        self.name = random.choice([i for i in self.poke_list.keys()])
        self.lvl = lvl
        self.xp = 0
        self.ap = None
        poke_conf = self.poke_list[self.name]

    def generate_pokemon_stats(self, pokemon_stats: dict,lvl: int =1):
        """
        Generate attributes values for the pokemon using the pokemon_stats

        Parameters
        ----------
        pokemon_stats: dict
            dict containing pokemon statistics
        lvl: int
            base lvl of the pokemon

        Returns
        -------
        None

        / >>>Pokemon().generate_pokemon_stats()
        """
        self.lvl = lvl
        self.xp = 0
        self.name = None
        self.p_type = pokemon_stats["Element"]
        pass


    def select_abilities(self):
        """
        used to select abilities of Pokemon (self)

        Returns
        -------
        None
        """

    """ Pokemon Methods """


    def attack(self, ability: "Ability", other: "Pokemon"):
        """
        This function use the ability on other
        it also checks if there is enough ap to use the ability and if so, remove the used ap and return True.
        else return False and do nothing.

        Parameters
        ----------
        ability : Ability
        other : Pokemon

        Returns
        -------
        bool
        """
        if ability.cost > self.ap:
            return False
        ability(other)
        self.ap -= ability.cost
        return True

    def defend(self, ability: "Ability"):
        """
        use the ability on self
        checks if there is enough ap to use the ability and if so, remove the used ap and return True.
        else return False and do nothing.

        Parameters
        ----------
        ability : Ability

        Returns
        -------
        bool
        """
        if ability.cost > self.ap:
            return False
        ability(self)
        self.ap -= ability.cost
        return True



if __name__ == '__main__':
    Pokemon().generate_random_pokemon(1)
