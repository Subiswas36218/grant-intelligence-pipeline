import json

def load_raw_data():
    with open("data/raw_grants.json") as f:
        return json.load(f)