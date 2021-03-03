import json

def load_level(level_id):
    with open("resources/levels.json") as json_file:
        res = json.load(json_file)
        if res[level_id]:
            return res[level_id]
        else:
            return None