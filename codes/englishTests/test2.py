from transformers import pipeline
# Load pipeline
classifier = pipeline("text-classification", model = "papluca/xlm-roberta-base-language-detection")
import joblib
joblib.dump(classifier,'classifier.joblib')