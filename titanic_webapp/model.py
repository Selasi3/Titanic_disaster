import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump

data = pd.read_csv("../csv/cleaned_titanic.csv")

X = data.drop(["Family Size", "Survived"], axis=1)
y = data["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
dump(logmodel, "model.pkl")