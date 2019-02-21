import json
import os.path

if os.path.exists("Config.json"):
    with open('Config.json') as json_data_file:
        settings = json.load(json_data_file)

data = {}
data["Iterations"] = []

with open('Config.json', 'w') as outfile:
    json.dump(data, outfile)