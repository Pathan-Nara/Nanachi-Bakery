from core_class.Upgrades import Upgrades

class JorysHand(Upgrades):
    def __init__(self):
        super().__init__("Jory's Hand", 100)

    def apply_effect(self, player):
        print("Applying Jory's Hand effect")
        player.npc += self.level * 2

    
    