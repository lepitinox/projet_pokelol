import random


class IA:
    def __init__(self, dif=0):
        self.difficulty = dif

    def choose_pokemon(self, player):
        if self.difficulty == 0:
            player.deck.change_curr_pokemon(random.choices(player.deck.decklist)[0])

    def choose_attack(self, attack_list):
        return random.choice(attack_list)
