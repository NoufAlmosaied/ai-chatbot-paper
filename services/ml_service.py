import joblib
import numpy as np

class MLService:
    def __init__(self, model_path):
        self.model = None
        self.model_path = model_path
    
    def predict(self, features):
        if self.model is None:
            raise ValueError("Model not loaded")
        return self.model.predict([features])
