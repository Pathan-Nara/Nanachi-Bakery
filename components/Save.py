import json
import os

class Save:
    def __init__(self, filename):
        self.filename = filename
        os.makedirs("saves", exist_ok=True)
        self.filename = os.path.join("saves", self.filename)

    def save_game(self, player, buildings, upgrades):
        with open(self.filename, 'w') as f:
            buildings_data = []
            for building in buildings:
                building_dict = {
                    'name': building.name,
                    'base_cost': building.base_cost,
                    'base_nps': building.base_nps,
                    'level': building.level if hasattr(building, 'level') else 1
                }
                buildings_data.append(building_dict)
            
            upgrades_data = []
            for upgrade in upgrades:
                upgrade_dict = {
                    'name': upgrade.name,
                    'base_cost': upgrade.base_cost,
                    'level': upgrade.level if hasattr(upgrade, 'level') else 1
                }
                upgrades_data.append(upgrade_dict)

            data = {
                'name': player.name,
                'nanachi': player.nanachi,
                'nps': player.nps,
                'npc': player.npc,
                'buildings': buildings_data,
                'upgrades': upgrades_data
            }
            json.dump(data, f, indent=4)