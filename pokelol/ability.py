"""
abilities obj, will be instantiated at the loading of the game (creation of pokemon obj)
"""
from typing import Union

from pokelol.poketools import txt_parser, txt_openner
from env_loader import ATTAQUE_PATH, DEFENSE_PATH
import random


class Ability:
    def __init__(self, name: str):
        self.name = name
        self.kind = None
        self.a_type = None
        self.cost = None
        self.description = None

    def __call__(self, *args, **kwargs):
        pass


class Attack(Ability):
    attack_dict = txt_parser(txt_openner(ATTAQUE_PATH))

    def __init__(self, config: Union[dict, None], name: Union[str, None]):
        super().__init__(config)
        self.accuracy = None
        self.Attribute2 = None
        self.power = None
        self.target = None

    def calc_succes(self):
        pass

    def calc_damage(self):
        pass


class Defence(Ability):
    defence_dict = txt_parser(txt_openner(DEFENSE_PATH))

    def __init__(self, config):
        super().__init__(config)
        self.heal_range = None

    def calc_cost(self):
        pass
