from core_class.Upgrades import Upgrades

class SkibidiToilet(Upgrades):
    def __init__(self):
        super().__init__("Skibidi Toilet", 1500)

    def apply_effect(self, player):
        player.nps += self.level * 5