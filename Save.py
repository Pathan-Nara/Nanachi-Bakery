import json
import os

class Save:
    def __init__(self, filename):
        self.filename = filename
        os.makedirs("saves", exist_ok=True)
        self.filename = os.path.join("saves", self.filename)

    def save_game(self, player, buildings):
        with open(self.filename, 'w') as f:
            buildings_data = []
            for building in buildings:
                building_dict = {
                    'name': building.name,
                    'cost': building.cost,
                    'nps': building.nps,
                    'count': building.count if hasattr(building, 'count') else 1
                }
                buildings_data.append(building_dict)
            
            data = {
                'name': player.name,
                'nanachi': player.nanachi,
                'nps': player.nps,
                'buildings': buildings_data
            }
            json.dump(data, f, indent=4)