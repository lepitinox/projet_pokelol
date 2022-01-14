#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
from typing import Union, List

from .Menu.menu_input import choose_integer
import ast
from pokelol.poketools import txt_parser, txt_openner
from env_loader import POKEMON_PATH
from ability import Attack, Defence
import random

# May be used later
POKEMON_ARGS = [
    "name",
    "p_type",
    "max_hp",
    "max_ap",
    "hp",
    "ap",
    "abilities",
    "lvl",
    "xp",
    "ap_regen",
    "resistance"
]


class Pokemon:
    poke_dict = txt_parser(txt_openner(POKEMON_PATH))

    def __init__(self, config: Union[dict, None], name: Union[str, None]):
        """
        if config is given, will use the configuration, else will generate a Pokemon config.
        if both args given, will use the config, and if nether are given, will ark user for a Pokemon name

        Parameters
        ----------
        config: Union[dict, None]
            a dictionary containing a Pokemon config (attributes of obj)

        name : Union[str, None]
            The name of a new pokemon
        """
        if isinstance(name, str) and config is None:
            # if name is given but no config, will check if the Pokemon exist and create a new Pokemon
            if self.check_name(name):
                self.name = name
            else:
                self.name = self.ask_for_name()
            self.base_config = self.create_pokemon(self.name)

        elif name is None and config is None:
            # if nothing is given, will ask the player give the name of the new Pokemon
            self.name = self.ask_for_name()
            self.base_config = self.create_pokemon(self.name)

        elif isinstance(name, str) and isinstance(config, dict):
            # if both name and config given, will only use the config, considering that the config is properly created
            if name.upper() != config.get("name", "").upper():
                # will warn the user is config name and name are different
                print(f"Warning: you gave a name : {name}\n and a config : {config.get('name', '')}")
                print("Using the config...")
            self.base_config = config
        else:
            # if only config is given, will use it, there is no check of the pokemon being in the pokemon list here
            # because even if the configuration user an other name,
            # attributes are already given and can be used in battle (not a bug, a feature ;) )
            self.base_config = config

        self.name = self.base_config["name"]
        self.p_type = self.base_config["p_type"]
        self.max_hp = self.base_config["max_hp"]
        self.max_ap = self.base_config["max_ap"]
        self.hp = self.base_config["hp"]
        self.ap = self.base_config["ap"]
        self.abilities = self.base_config["abilities"]
        self.lvl = self.base_config["lvl"]
        self.xp = self.base_config["xp"]
        self.ap_regen = self.base_config["ap_regen"]
        self.resistance = self.base_config["resistance"]
        self.evolution = self.base_config["evolution"]
        if self.evolution != "":
            self.evolution_lvl = int(self.poke_dict[self.evolution]["Niveau"].split(" ")[0])
        else:
            self.evolution_lvl = None

    """ Pokemon init """

    def create_pokemon(self, name: str) -> dict:
        """
        create a pokemon using the pokemon base config file

        Parameters
        ----------
        name : str
            name of the new pokemon

        Returns
        -------
        dict
        """
        ret = {}
        pokemon_base_config = self.poke_dict[name]
        ret["name"] = name
        ret["p_type"] = pokemon_base_config["Element"]
        ret["lvl"] = 0
        ret["xp"] = 0
        ret["evolution"] = pokemon_base_config["Apres"]
        hp_range = pokemon_base_config["Vie"].replace(" ", "").split("-")
        ret["max_hp"] = ret["hp"] = random.randint(int(hp_range[0]), int(hp_range[1]))

        ap_range = pokemon_base_config["Energie"].replace(" ", "").split("-")
        ret["max_ap"] = ret["ap"] = random.randint(int(ap_range[0]), int(ap_range[1]))
        temp = list(map(int, pokemon_base_config["Resistance"].replace(" ", "").split("-")))
        ret["resistance"] = random.randint(temp[0],temp[1])
        temp = list(map(int, pokemon_base_config["Regeneration"].replace(" ", "").split("-")))
        ret["ap_regen"] = random.randint(temp[0],temp[1])
        ret["abilities"] = {"attack": [], "defence": []}
        for ability in list(map(lambda x: x.replace('"', "").replace("[", "").replace("]", "").lstrip(" ").rstrip(" "),
                                pokemon_base_config["Competences"].split(","))):
            if ability in Attack.attack_dict.keys():
                ret["abilities"]["attack"].append(Attack(ability, Attack.attack_dict[ability]))
            elif ability in Defence.defence_dict.keys():
                ret["abilities"]["defence"].append(Defence(ability, Defence.defence_dict[ability]))
            else:
                raise KeyError(f"The ability : {ability} is nether in the attack nor the defence config file")

        return ret

    def xp_gain(self, xp_gain):
        newxp = self.xp + xp_gain
        if newxp >= 100:
            self.gain_lvl()
            self.xp -= 100
        else:
            self.xp = newxp

    def gain_lvl(self):
        self.lvl += 1
        self.max_hp += random.randint(1, 5)
        self.max_ap += random.randint(1,4)
        self.resistance += random.randint(1, 3)
        if self.evolution_lvl is not None:
            lvl = copy.deepcopy(self.evolution_lvl)
            if self.lvl >= self.evolution_lvl:
                self.create_pokemon(self.evolution)
                self.lvl = lvl

    def ask_for_name(self):
        """
        Ask user for a pokemon name, if not in poke_dict, will ask again
        returns an existing pokemon name

        Returns
        -------
        str
        """
        while True:
            user_input = str(
                input("Please enter a pokemon name :"
                      "\n(if you need a list of available pokemon type 'pokemon list'\n"))
            if user_input.lower() == "pokemon list":
                print(self.poke_dict.keys())
            if self.check_name(user_input):
                return user_input
            else:
                print("Sorry this pokemon does not exist please ask for one of those :")
                print(self.poke_dict.keys())

    def check_name(self, name: str):
        """
        check if pokemon is in poke_dict

        Parameters
        ----------
        name : str

        Returns
        -------
        bool
        """
        return name.lower() in str(self.poke_dict.keys()).lower()

    """ Pokemon Methods """

    def abilities_menu(self):

        return self.abilities["attack"] + self.abilities["defence"]

    def regen(self):
        newap = self.ap + self.ap_regen
        if newap > self.max_ap:
            self.ap = self.max_ap
        else:
            self.ap = newap

    def attack(self, ability: Attack, other: "Pokemon"):
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
            print(f"{self.name} n'a pas assez de point d'attaque pour lancer {ability.name} : {self.ap}/{self.max_ap}")
            return False
        ability(self, other)
        self.ap -= ability.cost
        return True

    def defend(self, ability: Defence):
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
            print(f"{self.name} n'a pas assez de point d'attaque pour lancer {ability.name} : {self.ap}/{self.max_ap}")
            return False
        print(f"{self.name} utilise {ability.name}")
        ability(self)
        self.ap -= ability.cost
        return True

    @classmethod
    def generate_random_pokemon(cls, lvl: int) -> "Pokemon":
        """
        randomly generate a pokemon of level lvl, takes in account min lvl for evolved Pokemon

        Parameters
        ----------
        lvl : int
            level of the generated Pokemon

        Returns
        -------
        Pokemon
        """
        data: dict = cls.poke_dict
        req_lvl: List[dict] = [{i: j} for i, j in data.items() if lvl in range(*list(map(int, j["Niveau"].replace(" ", "").split("-"))))]
        pokemon_dict: dict = random.choice(req_lvl)
        poke = Pokemon(name=str(list(pokemon_dict.keys())[0]), config=None)
        poke.lvl = lvl
        return poke

    def __repr__(self):
        n_ = "\n"
        return f"{self.name}({self.lvl}, {self.xp}/1000, {self.p_type}): Vie {self.hp}/{self.max_hp}, Energie ({self.ap}/" \
               f"{self.max_ap}) (+{self.ap_regen}), Resistance ({self.resistance})\n" \
               f"{f'{n_}'.join(map(str,list(self.abilities.values())[0]))}\n"
