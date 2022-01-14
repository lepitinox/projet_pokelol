from time import sleep
from typing import Union

import numpy as np

import Menu.menu_output as m_out
from pokelol.trainer import Player, Npc, WildPoke, Trainer
from interface import print, multiple_choices_no_back, input, multiple_choices
from ia import IA
from ability import Attack, Defence


class Game:

    def __init__(self, difficulty: int = 0, use_player: Player = None):
        self.ia_difficulty = difficulty

        print(m_out.welcome_menu())

        if use_player is None:
            use_player = Player()

        self.joueur = use_player
        print("Vos Pokemon : ")
        self.joueur.show_pokemons()

    def start(self):

        self.main_menu()

    def main_menu(self):

        def display_poke():
            poke_str = self.joueur.show_pokemons()
            self.start()

        def change_deck():
            self.joueur.change_deck()
            self.start()

        def vs_wild_p():
            self.main_combat(self.joueur, WildPoke(IA(self.ia_difficulty)))
            self.start()

        def vs_trainer():
            self.main_combat(self.joueur, Npc(IA(self.ia_difficulty)))
            self.start()

        def create_new_player():
            self.joueur = Player()
            self.start()

        def _quit():
            print("Shutting down game:")
            print("Merci d'avoir joué, au revoir!")

        choices = {
            "Voir vos pokemons": display_poke,
            "Changer le deck": change_deck,
            "Combattre / Capturer un pokemon": vs_wild_p,
            "Combattre un autre dresseur": vs_trainer,
            "Creer un autre dresseur": create_new_player,
            "Quitter": _quit
        }
        multiple_choices_no_back(choices)()

    def main_combat(self, p1: Player, p2: Union[Npc, WildPoke]):
        """

        Parameters
        ----------
        p1 : The user's dresseur (player 1)
        p2 : The opponent's dresseur (player 2)

        Returns
        -------

        """
        if p1 == p2:
            print("You can play against yourself")
            return
        print(f"Combat entre {p1.name} et {p2.name}")
        fight = Fight(p1, p2)
        fight.fight()


class Fight:

    def __init__(self, f1: Player, f2: Union[Npc, WildPoke]):
        self.turn = 1
        self.p1 = f1
        self.p2 = f2
        if isinstance(f2, Npc):
            self.f_type = "JcJ"
        else:
            self.f_type = "JcE"
        self.winner = None

    def prep_fight(self):
        self.p1.deck.heal_all()
        self.p2.deck.heal_all()
        self.p1.deck.change_pokemon()
        self.p2.ia.choose_pokemon(self.p2)

    def fight(self):
        self.prep_fight()
        while True:
            print(f"Debut du tour {self.turn}")
            self.player_turn()
            if self.winner is not None or not self.p2.deck.is_alive():
                self.winner = self.p1
                break
            self.ia_turn()
            if self.winner is not None or not self.p1.deck.is_alive():
                self.winner = self.p2
                break
            self.turn += 1
            self.p1.deck.current_pokemon.regen()
            self.p2.deck.current_pokemon.regen()
        print(f"{self.winner} a gagné !")

        if self.f_type == "JcJ":
            looser = [self.p1, self.p2].pop([self.p1, self.p2].index(self.winner))
            for i in self.winner.deck.decklist:
                xp_gain = 10 + (np.mean([i.lvl for i in looser.deck.decklist])) - i.lvl
                i.gain_xp(xp_gain)
        else:
            if self.winner == self.p1 and self.p2 is not None:
                for i in self.winner.deck.decklist:
                    xp_gain = (10 + self.p2.deck.decklist[0].lvl - i.lvl) / 3
                    i.gain_xp(xp_gain)

    def player_turn(self):
        print(f"Pokemon actuel de {self.p1.name} \n{self.p1.deck.current_pokemon}\n")
        print(f"Pokemon actuel de {self.p2.name} \n{self.p2.deck.current_pokemon}\n")

        def abilities_menu():
            abi = self.p1.deck.current_pokemon.abilities_menu()
            _choices = {str(i): i for i in abi}
            res = multiple_choices(_choices, "Quelle compétence voulez vous utiliser ?", combat_menu)
            if isinstance(res, Attack):
                ok = self.p1.deck.current_pokemon.attack(res, self.p2.deck.current_pokemon)
                if not ok:
                    abilities_menu()
                    return
            elif isinstance(res, Defence):
                ok = self.p1.deck.current_pokemon.defend(res)
                if not ok:
                    abilities_menu()
                    return
            else:
                res()

        def combat_menu():
            choices = {"Change poke": self.p1.deck.change_pokemon,
                       "Utiliser une compétance": abilities_menu,
                       "Passer le tour": lambda: 1}
            if self.f_type.lower() == "JCJ".lower():
                choices["ff"] = self.p1.deck.kill_all
            else:
                choices["Capturer"] = self.capture_try
            multiple_choices_no_back(choices)()

        if self.p1.deck.current_pokemon.hp <= 0:
            self.p1.deck.change_pokemon()
            if self.p1.deck.current_pokemon is None:
                # if no pokemon left, p2 is the winner
                self.winner = self.p2
                return
        combat_menu()

        print(f"Fin du tour de {self.p1.name}\n")

    def capture_try(self):
        print(f"Vous tentez de capturer {self.p2.name}")
        sleep(1)
        ok = self.p1.capture(self.p2)
        if ok:
            print(f"Vous avez capturé le pokemon : {self.p2.name} !")
            self.winner = self.p1
            self.p2 = None
        else:
            print(f"Vous n'avez pas réussi a capturer {self.p2.name}")

    def ia_turn(self):
        sleep(3)
        a = self.p2.ia.choose_attack(
            self.p2.deck.current_pokemon.abilities_menu() + [lambda: print(f"{self.p2.name} passe son tour")])
        if isinstance(a, Attack):
            ok = self.p2.deck.current_pokemon.attack(a, self.p1.deck.current_pokemon)
            if not ok:
                self.ia_turn()
                return
        elif isinstance(a, Defence):
            ok = self.p2.deck.current_pokemon.defend(a)
            if not ok:
                self.ia_turn()
                return
        print(f"Fin du tour de {self.p2.name}\n")
        sleep(1)


if __name__ == "__main__":
    g = Game()
    g.start()
