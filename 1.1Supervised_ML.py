# SUPERVISED MACHINE LEARNING

# check python -- version 
# check lib -- pandas, numpy, matplotlib, sklearn(scikit-learn)

# step 1 -- import the lib. 

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# step 2 -- create dataset

df = pd.DataFrame({
    'Hours':[1,2,3,4,5,6,7,8,9,10],
    'Marks':[10,20,30,40,50,60,70,80,90,100]
})

# step 3 -- split the dataset into features and sample 

X = df[['Hours']]          # X--capital 
y = df['Marks']            # y -- small    

# step 4 -- split the dataset into training and testing dataset 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Step 5 -- Train the model using Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)  # -- load the data into the model and train it.


# step 6 -- make predictions using the trained model
y_pred = model.predict(X_test)   # -- prediction is done on the test dataset.
                                 # x--independent variable, y--dependent variable that's why we use x_test with y_pred.
print("Prediction:",y_pred)                       


# step 7 --plot 
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Obtained')
plt.title('Linear Regression example')
plt.show()

# step 8 -- evaluate the model


print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

print('R2 Score:', r2_score(y_test, y_pred))


