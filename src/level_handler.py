import json

# This just gets the level from the level file.
# Nothing really special....

def load_level(level_id: str):
    with open(f"levels/{level_id}.json") as json_file:
        res = json.load(json_file)
        return res[level_id]