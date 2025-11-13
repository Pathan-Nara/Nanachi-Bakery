from Upgrades import Upgrades

class JorysHand(Upgrades):
    def __init__(self, level=1):
        super().__init__("Jory's Hand", 100, level)

    def apply_effect(self, player):
        player.npc += self.level * 2

    
    