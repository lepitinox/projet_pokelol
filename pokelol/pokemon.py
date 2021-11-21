#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Union

from .Menu.menu_input import choose_integer
import ast
from pokelol.poketools import txt_parser, txt_openner
from env_loader import POKEMON_PATH
from ability import Attack, Defence
import random

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
        pokemon_base_config = self.poke_dict[name.lower()]
        ret["p_type"] = pokemon_base_config["element"]
        ret["lvl"] = 0
        ret["xp"] = 0

        hp_range = pokemon_base_config["vie"].replace(" ", "").split("-")
        ret["max_hp"] = ret["hp"] = random.randint(int(hp_range[0]), int(hp_range[1]))

        ap_range = pokemon_base_config["energie"].replace(" ", "").split("-")
        ret["max_ap"] = ret["ap"] = random.randint(int(ap_range[0]), int(ap_range[1]))

        ret["resistance"] = map(int, pokemon_base_config["resistance"].replace(" ", "").split("-"))

        ret["ap_regen"] = map(int, pokemon_base_config["regeneration"].replace(" ", "").split("-"))

        ret["abilities"] = {"attack": [], "defence": []}
        for ability in ast.literal_eval(pokemon_base_config["competences"]):
            if ability.lower() in Attack.attack_dict.keys():
                ret["abilities"]["attack"].append(Attack(Attack.attack_dict[ability.lower()]))
            elif ability.lower() in Defence.defence_dict.keys():
                ret["abilities"]["defence"].append(Defence(Defence.defence_dict[ability.lower()]))
            else:
                raise KeyError(f"The ability : {ability} is nether in the attack nor the defence config file")

        return ret

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
                      "\n(if  you need a list of available pokemon type 'pokemon list'\n"))
            if user_input.lower() == "pokemon list":
                print(self.poke_dict.keys())
            if self.check_name(user_input):
                return user_input
            else:
                print("Sorry this pokemon does not exist please ask for one og this :")
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
            return False
        ability(other)
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
            return False
        ability(self)
        self.ap -= ability.cost
        return True

