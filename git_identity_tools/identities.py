import configparser
import os


def load_identities(config_path=None):
    config = configparser.ConfigParser()
    config_path = config_path or os.path.expanduser("~/.config/git-identity-tools/identities.conf")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Identity config not found at {config_path}")
    config.read(config_path)
    return config


def get_identity(config, org, enterprise):
    if f"org:{org}" in config:
        return config[f"org:{org}"]["name"], config[f"org:{org}"]["email"]
    elif f"enterprise:{enterprise}" in config:
        return config[f"enterprise:{enterprise}"]["name"], config[f"enterprise:{enterprise}"]["email"]
    return None, None
