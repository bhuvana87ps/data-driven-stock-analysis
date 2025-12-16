import os
import yaml

RAW_DIR = "data"


def get_all_yaml_files():
    """
    Recursively scan the data directory and return all YAML file paths.
    """
    yaml_files = []

    for root, _, files in os.walk(RAW_DIR):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                yaml_files.append(os.path.join(root, file))

    return sorted(yaml_files)


def process_yaml_file(file_path):
    """
    Load a YAML file and return a list of raw row dictionaries.
    """
    try:
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)

        if not isinstance(data, list):
            print(f"WARNING: {file_path} does not contain a list")
            return []

        return data

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []
