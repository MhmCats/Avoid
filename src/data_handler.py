import json
import os


def check_if_exists():
	if not os.path.exists("level_info/highscores.json"):
		with open("level_info/highscores.json", "w") as f:
			json_file_content = """\
{
    "level-one": 0,
    "level-two": 0,
    "level-three": 0
}"""
			f.write(json_file_content)


def load_level(level_id: str):
    with open(f"level_info/{level_id}.json") as json_file:
        res = json.load(json_file)
        return res[level_id]

def get_highscores(level_id: str):
	check_if_exists()
	with open("level_info/highscores.json") as json_file:
		res = json.load(json_file)
		return res[level_id]

def update_highscores(level_id: str, new_highscore: int):
	check_if_exists()
	new_content = "{"
	if level_id == "level-one":
		new_content += f'\n\t"level-one": {new_highscore},'
	else:
		new_content += f'\n\t"level-one": {get_highscores("level-one")},'
	
	if level_id == "level-two":
		new_content += f'\n\t"level-two": {new_highscore},'
	else:
		new_content += f'\n\t"level-two": {get_highscores("level-two")},'
	
	if level_id == "level-three":
		new_content += f'\n\t"level-three": {new_highscore}'
	else:
		new_content += f'\n\t"level-three": {get_highscores("level-three")}'

	new_content += "\n}"

	with open("level_info/highscores.json", "w") as json_file:
		json_file.write(new_content)
