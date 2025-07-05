import json
import os
from datetime import date

class DataManager:
    def __init__(self, filepath="data/training_log.json"):
        self.filepath = filepath

    def load(self):
        if not os.path.exists(self.filepath):
            return {}
        with open(self.filepath, "r") as f:
            return json.load(f)

    def save(self, date_str, session_list):
        data = self.load()
        data[date_str] = session_list
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2)

    def get_by_date(self, date_str):
        data = self.load()
        return data.get(date_str, [])

    def get_all(self):
        return self.load()
