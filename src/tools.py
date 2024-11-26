import yaml
import os
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))  # Root directory
CONFIG_PATH = os.path.join(PROJECT_ROOT, "config.yaml")    # Path to config.yaml

print(CONFIG_PATH)

def load_config(config_path=CONFIG_PATH):
    """Load configuration from a YAML file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
    
def download_file(url, save_path):
    """Download a file from a URL."""
    import requests
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded: {save_path}")

def load_excel(file_path):
    """Load an Excel file as a DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_excel(file_path)

def load_config(config_path):
    """
    Load the configuration file (YAML format).
    
    Args:
        config_path (str): Path to the configuration file.
    
    Returns:
        dict: Configuration data as a dictionary.
    """
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
