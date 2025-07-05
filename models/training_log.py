class TrainingLog:
    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def to_dict(self):
        return [s.to_dict() for s in self.sessions]

    def describe_all(self):
        return [
            s.describe() + f" ({s.duration} menit) - {s.notes}"
            for s in self.sessions
        ]

    def load_from_dict(self, data_list, class_map):
        for item in data_list:
            cls_name = item["type"]
            duration = item["duration"]
            notes = item.get("notes", "")
            cls = class_map.get(cls_name)
            if cls:
                self.add_session(cls(duration, notes))
