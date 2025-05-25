import configparser
import os

config = configparser.ConfigParser()
# Always load config.ini from project root directory
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.ini")
config.read(config_path)

def get_base_url():
    try:
        env = config.get('DEFAULT', 'env')
        base_url = config.get(env, 'base_url')
        print(f"[INFO] Environment: {env} | Base URL: {base_url}")  # optional debug log
        return base_url
    except Exception as e:
        print(f"[ERROR] Failed to load base URL from config.ini: {e}")
        raise