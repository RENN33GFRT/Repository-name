import json
import os


def get_transactions(file_path):
    if not os.path.isfile(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
        except json.JSONDecodeError:
            return []


current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "..", "data", "transactions.json")
print(get_transactions(path))
