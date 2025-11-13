import json
import os
class Save:
    def __init__ (self, filename):
        self.filename = filename
        os.makedirs("saves", exist_ok=True)
        self.filename = os.path.join("saves", self.filename)

    def save_game(self, player, buildings):
        with open(self.filename, 'w') as f:
            data = {
                'name': player.name,
                'nanachi': player.nanachi,
                'nps': player.nps,
                'buildings': [building.name for building in buildings]
            }
            json.dump(data, f)


    
    
