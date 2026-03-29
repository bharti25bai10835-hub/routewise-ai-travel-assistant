import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

print("The script is starting")

current_folder = os.path.dirname(__file__)

# dataset path
dataset_path = os.path.join(current_folder, "..", "datasets", "transport_conditions.csv")

# model save path
model_path = os.path.join(current_folder, "..", "models", "comfort_model.pkl")

data = pd.read_csv(dataset_path)

# input features
X = data[["travel_time","seat_comfort","noise_level","stability"]]

# output label
y = data["comfort_level"]

# train model
model = DecisionTreeClassifier()
model.fit(X,y)

# save model
with open(model_path,"wb") as f:
    pickle.dump(model,f)

print("AI is ready to assist!")