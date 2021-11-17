#!/usr/bin/python
# -*- coding: utf-8 -*-

from pokelol.poketools import txt_parser
from env_loader import POKEMON_PATH


class Pokemon:
    poke_list = txt_parser(POKEMON_PATH)

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

    def attack(self, ability: "Ability", other: "Pokemon"):
        if ability.cost > self.ap:
            return False
        ability(other)
        self.ap -= ability.cost
        return True

    def defend(self, ability: "Ability"):
        if ability.cost > self.ap:
            return False
        ability(self)
        self.ap -= ability.cost
        return True

    def init_abillities(self):
        pass
