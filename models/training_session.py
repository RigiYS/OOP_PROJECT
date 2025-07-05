from abc import ABC, abstractmethod

class TrainingSession(ABC):
    def __init__(self, duration, notes=""):
        self.duration = duration
        self.notes = notes

    @abstractmethod
    def describe(self):
        pass

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "duration": self.duration,
            "notes": self.notes
        }
