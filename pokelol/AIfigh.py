from abc import ABC, abstractmethod


class AIfight(ABC):
    """
    Class to generate an artificial intelligence for a pokefight
    """

    def __init__(self, pokemons):

        self.pokemons = pokemons

    def difficulty(self):
        pass

    def who(self):
        pass

    def choixpoke(self, a, b):
        import random
        self.deck = []
        for i in range(3):
            var = random.randint(a, b)
            self.deck.append(self.pokemons[var])
        return deck

    def __str__(self):
        res = "Niveau de difficulté"
        res = "Un combat contre" + self.who() + "est lancé!"
        res += "Voici l'équipe de" + self.who() + ":"
        for i in self.deck:
            res += i["Nom"] + ";"
        return res

    @abstractmethod
    def AItour(self):
        pass


class AIeasy(AIfight):
    def __init__(self):
        super().__init__(pokemons)

    def who(self):
        return "Maitre Trace"

    def difficulty(self):
        return "Facile"

    def __str__(self):
        res = super().__str__()
        return res

    def deck(self):
        self.deck = AIfight.choixpoke(0, 11)
        return self.deck
