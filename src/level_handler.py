import json

# This just gets the level from the level file.
# Nothing really special....

def load_level(level_id: str):
    with open("resources/levels.json") as json_file:
        res = json.load(json_file)
        if res[level_id]:
            return res[level_id]
        else:
            return None