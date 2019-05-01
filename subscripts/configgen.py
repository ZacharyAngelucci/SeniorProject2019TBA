import yaml
import os.path


def config():
    if os.path.isfile("config.yaml"):
        return load_config()
    else:
        create_config()
        quit()


def create_config():
    config_default = {
        'Iterations': 0,
        'State': 'ALL',
        'Vehicles': 1,
        'Drivers': 1,
        'Output': 'CSV'
    }
    with open('config.yaml', 'w') as f:
        yaml.dump(config_default, f, default_flow_style=False)


def load_config():
    with open('config.yaml') as f:
        return yaml.safe_load(f)
