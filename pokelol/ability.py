"""
abilities obj, will be instantiated at the loading of the game (creation of pokemon obj)
"""
from typing import Union

from pokelol.poketools import txt_parser, txt_openner
from env_loader import ATTAQUE_PATH, DEFENSE_PATH


class Ability:
    def __init__(self, name, config: Union[dict, None]):
        self.name = name
        self.conf = config
        self.kind = None
        self.a_type = None
        self.cost = None
        self.description = None

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class Attack(Ability):
    attack_dict = txt_parser(txt_openner(ATTAQUE_PATH))

    def __init__(self, name, config: Union[dict, None]):
        super().__init__(name, config)
        self.accuracy = None
        self.Attribute2 = None
        self.power = None
        self.target = None

    def calc_damage(self):
        pass

    def calc_succes(self):
        pass


class Defence(Ability):
    defence_dict = txt_parser(txt_openner(DEFENSE_PATH))

    def __init__(self, name, config: Union[dict, None]):
        super().__init__(name, config)
        self.heal_range = None

    def calc_cost(self):
        pass
