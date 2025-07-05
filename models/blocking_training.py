from .training_session import TrainingSession

class BlockingTraining(TrainingSession):
    def describe(self):
        return "Blocking Training: latihan membaca lawan dan timing blok"
