"""
abilities obj
"""


class Ability:
    def __init__(self):
        self.kind = None
        self.a_type = None
        self.cost = None
        self.description = None

    def use(self):
        pass


class Attack(Ability):
    def __init__(self):
        super().__init__()
        self.accuracy = None
        self.Attribute2 = None
        self.power = None
        self.target = None

    def calc_succes(self):
        pass

    def calc_damage(self):
        pass


class Defence(Ability):
    def __init__(self):
        super().__init__()
        self.heal_range = None

    def calc_cost(self):
        pass

