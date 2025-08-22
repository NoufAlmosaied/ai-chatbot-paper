class RiskAnalyzer:
    def analyze(self, prediction_proba):
        if prediction_proba >= 0.8:
            return {"level": "HIGH", "color": "red"}
        elif prediction_proba >= 0.5:
            return {"level": "MEDIUM", "color": "orange"}
        else:
            return {"level": "LOW", "color": "green"}
