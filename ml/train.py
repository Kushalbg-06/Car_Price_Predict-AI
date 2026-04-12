import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os
from preprocess import preprocess_data

os.makedirs("ml", exist_ok=True)

data = pd.read_csv("data/car_data.csv")

X, y, preprocessor = preprocess_data(data)

model = RandomForestRegressor()
model.fit(X, y)

# Save both model + preprocessor
with open("ml/model.pkl", "wb") as f:
    pickle.dump((model, preprocessor), f)

print("✅ Advanced model saved!")