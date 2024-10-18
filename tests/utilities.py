import os

import yaml


def read_authenticated_email_ids():
    """Read authenticated users from text file."""
    file_path = os.path.join("..", "test_data", "authenticatedUsers.txt")
    try:
        with open(file_path, 'r') as file:
            email_ids = [line.strip() for line in file if line.strip()]
        return email_ids
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def read_non_authenticated_email_ids():
    """Read non-authenticated users from text file."""
    file_path = os.path.join("..", "test_data", "nonAuthenticatedUsers.txt")
    try:
        with open(file_path, 'r') as file:
            email_ids = [line.strip() for line in file if line.strip()]
        return email_ids
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_yaml():
    file_path = os.path.join("..", "config", "config.yaml")
    with open(r"tests\config.yaml", 'r') as file:
        return yaml.safe_load(file)



