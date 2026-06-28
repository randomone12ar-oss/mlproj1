import os
from src.utils import load_object

print("Loading model...")

model = load_object(
    os.path.join("artifacts", "model.pkl")
)

print("✅ Model loaded successfully!")

print("Loading preprocessor...")

preprocessor = load_object(
    os.path.join("artifacts", "preprocessor.pkl")
)

print("✅ Preprocessor loaded successfully!")