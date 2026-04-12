import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def preprocess_data(df):
    categorical = ['fuel', 'transmission', 'owner', 'company']
    
    ct = ColumnTransformer([
        ("encoder", OneHotEncoder(), categorical)
    ], remainder='passthrough')

    X = df.drop("price", axis=1)
    y = df["price"]

    X_transformed = ct.fit_transform(X)

    return X_transformed, y, ct