import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create synthetic dataset
X, y = make_blobs(
    n_samples=4000,
    n_features=3,
    centers=3,
    cluster_std=2,
    random_state=80
)

print('X (Features):')
print(X)

print('\nShape of X:')
print(X.shape)

print('\ny (Target/Class):')
print(y)

print('\nShape of y:')
print(y.shape)

# Plot first two features
plt.figure(figsize=(6, 6))

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    cmap='rainbow'
)

plt.show()

# Convert X into DataFrame
df = pd.DataFrame(X)

print(df.head())

# Histogram
plt.rcParams['figure.figsize'] = (10, 8)

df.plot(
    kind='hist',
    bins=100,
    subplots=True,
    layout=(3, 1),
    sharex=False,
    sharey=False
)

plt.show()


#scatter plot - how are my classes distributed based on features 1 and feature 2?
# historgram -- distribution of each features individually
# the first step is to figure out the k . the calculation of the k value varies greatly depending 
# on the situation the default value of k when using the scikit-learn library is 5 and the default 
# distance metric used is euclidean

#scatter plot answers-How are my classes distributed based on Feature 1 and Feature 2?
#histogram --Distribution of each feature individually
'''The first step is to figure out the k. The calculation of the K value varies greatly depending on the situation.
The default value of K when using the Scikit-Learn Library is 5 and the default distance metric used is Euclidean.'''


#Tuning the Model to Get High K Nearest Neighbor Accuracy

from sklearn.model_selection import GridSearchCV
param_grid = {'n_neighbors':np.arange(1,4)}

knn = KNeighborsClassifier()
knn_cv= GridSearchCV(knn,param_grid,cv=5)
knn_cv.fit(X,y)

print(knn_cv.best_params_)
print(knn_cv.best_score_)
#train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 80)
# instantiate the model
knn = KNeighborsClassifier(n_neighbors=3)

# fit the model to the training set
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

