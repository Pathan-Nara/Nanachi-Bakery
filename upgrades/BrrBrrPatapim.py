from core_class.Upgrades import Upgrades

class BrrBrrPatapim(Upgrades):
    def __init__(self):
        super().__init__("Brr Brr Patapim", 700)
        self.building_name = "Mine"

    def apply_effect(self, player):
        for building in player.buildings:
            if building.name == self.building_name:
                building.base_nps += self.level * 3
                building.update_nps()