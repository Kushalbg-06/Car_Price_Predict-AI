import pickle
import os

def load_model():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    path = os.path.join(BASE_DIR, "ml", "model.pkl")

    with open(path, "rb") as f:
        model, preprocessor = pickle.load(f)

    return model, preprocessor