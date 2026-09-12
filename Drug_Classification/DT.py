import pandas as pd 
import kagglehub
import os
path = kagglehub.dataset_download("prathamtripathi/drug-classification")
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv(os.path.join(path,"drug200.csv"))
print(df.head())



