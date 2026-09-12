# Logistic Regression 

# it is a supervised ml algo used forclassification. It predicts the probability that belongs to a
# specific categories (yes/no, spam/no spam , 0/1)

# the sigmoid function converts the raw output into a probability value between 0 and 1 
# in LOR we use threshold value [0.5] to decide the class label 
# if the sigmoid output is same or above the threshold input isclassified 
# if the sigmoid output is below the threshold input is classified as 0


# WHY NOT linear regression for classification :
        #  linear regression can give values beyong 0-1
        #  classification needs probability between 0-1
        

# working : logistic regression computes combination of input features z - wX+b and
# pass it through sigmoid function to produce probability between 0 and 1 this probability is then used to assgn the input to a class 

        
        
        #logistic regression Alogoritm 

# step 1 import the lib
 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
     
# step 2 create database 

df = sns.load_dataset ('titanic')
print(df.head())

# step 3 - select required columns

df = df[['pclass','age','sex','fare','survived']]

# step 4 -  check missing values 
print('Missing Values before cleaning:')
print(df.isnull().sum())

# step 5 -  drop rows containing missing values 
df = df.dropna()
print(df.isnull().sum())

# step 6 - convert male/female into numbers 
df['sex'] = df['sex'].map({
    'male':0,
    'female':1
})
print(df)

# step 7 - features and targets
X = df[['pclass','age','sex','fare']]
y = df['survived']

# step 8 - split the dataset 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# step 9 - create model 
model = LogisticRegression(max_iter=1000)

# why are we using max_iter - LoR trained iteratively, the model keeps adjusting its 
# cofficients until it coverages
# max iter-maximum no of iterations the model is allowed  to perform,
# model = Logisticregression(max_iter = 1000) means the model can take up to 1000 iterartion to find a solution 

# step 10 train the model
model.fit(X_train,y_train)

#step 11 -  prediction
y_pred = model.predict(X_test)

# step 12 - Accuracy
print("Accuracy:",accuracy_score(y_test,y_pred))

# step 13 - confussion_matrix
cm = confusion_matrix(y_test,y_pred)

# print heatmap
plt.figure(figsize=(5,4))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# predict new passenger

new_passenger = pd.DataFrame({
    'pclass':[1],
    'sex':[1],
    'age':[25],
    'fare':[100]
})

new_passanger = new_passenger[X.columns]
prediction = model.predict(new_passanger)
print('Prediction:',prediction)

#predict another passenger 

new_passanger = pd.DataFrame ({
                            'pclass' : [3],
                            'sex'    : [0],
                            'age'    : [45],
                            'fare'   : [8] 
                            })
new_passanger = new_passanger[X.columns]
prediction = model.predict(new_passanger)
print('Prediction:',prediction)


#probability of survial (most important)
probability = model.predict_proba(new_passanger)
print('Probability:',probability)






# Likelihood Function: measures the accuracy of logistic regression algorithm       
# loss function 

