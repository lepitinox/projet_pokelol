"""
abilities obj, will be instantiated at the loading of the game (creation of pokemon obj)
"""
from typing import Union
import random

from pokelol.poketools import txt_parser, txt_openner
from env_loader import ATTAQUE_PATH, DEFENSE_PATH


class Ability:
    def __init__(self, name: str, config: Union[dict, None]):
        self.name = name
        self.conf = config
        self.kind = config["Element"]
        self.a_type = config["Element"]
        self.cost = int(config["Cout"])
        self.description = config["Description"]

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        return f"{str(self.name)}  - Type: {str(self.kind)} | Cout: {str(self.cost)} - {str(self.__name__)} : {str(self.description)}"

    def __repr__(self):
        return f"{str(self.name)}  - Type:{str(self.kind)} | Cout: {str(self.cost)} - {str(self.__name__)} {str(self.description)}"


class Attack(Ability):
    attack_dict = txt_parser(txt_openner(ATTAQUE_PATH))

    def __init__(self, name: str, config: Union[dict, None]):
        super().__init__(name, config)
        self.accuracy = int(config["Precision"])
        self.power = int(config["Puissance"])
        self.target = None
        self.__name__ = "Attaque"

    def calc_damage(self, atta, rec):
        """
        function used to calculate the damage inflicted to a pokemon

        Parameters
        ----------
        atta : Pokemon
            attacking pokemon
        reci : Pokemon
            pokemon receiving the attack

        Returns
        -------

        """
        elem_matrix = [[1, 1, 0.5, 1.5], [1.5, 1, 1, 0.5], [0.5, 1.5, 1, 1], [1, 0.5, 1.5, 1]]
        elem = {"Air": 0, "Eau": 1, "Feu": 2, "Terre": 3}
        # The index element of the is obtained from the attribute of the ability
        elem_ability = elem[self.a_type]
        # The index element of the defending pokemon
        elem_def = elem[rec.p_type]
        # =================================================================== #
        # ===== The following variables are used to calculate the damage ==== #
        # =================================================================== #
        # Getting the beta variable using the two previous indices on the matrix
        beta = elem_matrix[elem_def][elem_ability]
        # na is the level of the attacking pokemon
        na = atta.lvl
        # omega is the resistance of the defending pokemon
        omega = rec.resistance
        # p is the power of the ability used by the attack
        p = int(self.power)
        # cm adds a bit of randomness to the value of beta
        cm = beta * random.uniform(0.85, 1)
        # the calculation of damage
        dmg = int(cm * ((p * (4 * na + 2)) / omega + 2))

        return dmg

    def calc_succes(self):
        return random.randint(0, 100) <= self.accuracy

    def __call__(self, me, other):
        if self.calc_succes():
            damage = self.calc_damage(me, other)
            print(f"Vous infliger {damage} de dégats a {other.name}")
            other.hp -= damage
        else:
            print(f"{me.name} a rater son attaque")

class Defence(Ability):
    defence_dict = txt_parser(txt_openner(DEFENSE_PATH))

    def __init__(self, name: str, config: Union[dict, None]):
        super().__init__(name, config)
        if config["Soin"] != '':
            temp = list(map(int, config["Soin"].replace(" ", "").split("-")))
        else:
            temp = ""
        if config["Energie"] != "":
            temp2 = list(map(int, config["Energie"].replace(" ", "").split("-")))
        else:
            temp2 = ""
        self.energie_range = temp2
        self.heal_range = temp
        self.__name__ = "Defence"

    def __call__(self, poke):
        if self.cost == 0:
            newap = poke.ap + random.randint(self.energie_range[0], self.energie_range[1])
            if newap > poke.max_ap:
                poke.ap = poke.max_ap
            else:
                poke.ap = newap
        else:
            newhp = poke.hp + random.randint(self.heal_range[0], self.heal_range[1])
            if newhp > poke.max_hp:
                poke.hp = poke.max_hp
            else:
                poke.hp = newhp
