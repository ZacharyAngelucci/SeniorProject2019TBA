import yaml
import os.path
from subscripts import aboutyou, yourdrivers, yourvehicles

configData = {'Iterations': 0}
iterations = None
if os.path.isfile("config.yaml"):
    with open('config.yaml') as f:
        configData = yaml.safe_load(f)
else:
    with open('config.yaml', 'w') as f:
        yaml.dump(configData, f, default_flow_style=False)
    quit()

for i in range(configData['Iterations']):
    print(aboutyou.makeList())