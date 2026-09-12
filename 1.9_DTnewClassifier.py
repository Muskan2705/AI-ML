import numpy as np
import pandas as pd 
import kagglehub
import os
path = kagglehub.dataset_download( 
    "prathamtripathi/drug-classification")
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#read data
df = pd.read_csv(os.path.join(path,"drug200.csv"))
df.head()
df.columns
df.drop(columns =['Na_to_K'])

#feature & targets 
X = df[['Age','Sex','BP','Cholesterol']]
y = df['Drug']

X_encoded = pd.get_dummies(X,columns=['Sex','BP','Cholesterol'])

#X_encoding converts categorical columns into numerical 
#columns before giving data to  ML model like DT

#split the dataset
X_train,X_test,y_train,y_test = train_test_split(X_encoded,y,test_size=0.2,random_state=42)

#create the model
model = DecisionTreeClassifier(max_depth=3,random_state=42)
model.fit(X_train,y_train)

#Prediction
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test,y_pred))

#plot tree
from sklearn import tree
import matplotlib.pyplot as plt

plt.figure(figsize = (15,10))
tree.plot_tree(model,feature_names = X_encoded.columns,class_names = model.classes_.astype(str), filled =True,rounded = True, fontsize = 8)
plt.show()

