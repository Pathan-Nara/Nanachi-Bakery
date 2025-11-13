from upgrades.JorysHand import JorysHand
from upgrades.SkibidiToilet import SkibidiToilet
from upgrades.BrrBrrPatapim import BrrBrrPatapim

class UpgradeList:
    def __init__(self):
        self.upgrades = [
            JorysHand(),
            SkibidiToilet(),
            BrrBrrPatapim()
        ]

    def get_upgrades(self):
        return self.upgrades