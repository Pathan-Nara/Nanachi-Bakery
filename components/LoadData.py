import os
import json

class LoadData:

    def get_data(self, filename):
        filepath = os.path.join("saves", filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as file:
                data = json.load(file)
                return data
        return None
    
    def listSaves(self):
        if not os.path.exists("saves"):
            return []
        saves = os.listdir("saves")
        return saves