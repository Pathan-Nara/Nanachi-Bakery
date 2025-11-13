class Upgrades:
    def __init__(self, name,cost):
        self.name = name
        self.base_cost = cost
        self.cost = cost
        self.level = 0

    def get_info(self):
        return f"{self.name} - {self.cost}n - Level {self.level}"

    def upgrade(self, player):
        self.level += 1
        self.update_cost()
        self.apply_effect(player)

    def update_cost(self):
        self.cost = int(self.base_cost * (1.5 ** self.level))


    def apply_effect(self, player):
        pass

