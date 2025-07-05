from .training_session import TrainingSession

class ServeTraining(TrainingSession):
    def describe(self):
        return "Serve Training: fokus akurasi dan konsistensi"
