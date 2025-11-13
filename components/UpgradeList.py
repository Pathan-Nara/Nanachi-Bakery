from upgrades.JorysHand import JorysHand


class UpgradeList:
    def __init__(self):
        self.upgrades = [
            JorysHand()
        ]

    def get_upgrades(self):
        return self.upgrades