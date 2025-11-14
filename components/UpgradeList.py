from upgrades.JorysHand import JorysHand
from upgrades.SkibidiToilet import SkibidiToilet
from upgrades.BrrBrrPatapim import BrrBrrPatapim
from upgrades.MiniNana import MiniNana

class UpgradeList:
    def __init__(self):
        self.upgrades = [
            JorysHand(),
            SkibidiToilet(),
            BrrBrrPatapim(),
            MiniNana()
        ]

    def get_upgrades(self):
        return self.upgrades