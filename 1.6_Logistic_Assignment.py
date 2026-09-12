# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import sklearn

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# from sklearn.feature_extraction.text import TfidfVectorizer


# # Load dataset
# df = pd.read_csv(r"M:\CETPA_AI_ML\spam detection dataset.csv")

# print(df.head())


# # Checking missing values
# print("Missing values before cleaning:")
# print(df.isnull().sum())


# # Split features and target
# X = df['Message']
# y = df['Category']


# # Convert text into numerical features
# vectorizer = TfidfVectorizer()

# X = vectorizer.fit_transform(X)


# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )


# # Create model
# model = LogisticRegression(max_iter=1000)

# # Train model
# model.fit(X_train, y_train)


# # Prediction
# y_pred = model.predict(X_test)


# # Accuracy
# print("Accuracy:", accuracy_score(y_test, y_pred))


# # Confusion Matrix
# print("\nConfusion Matrix:")

# cm = confusion_matrix(y_test, y_pred)

# print(cm)


# # Classification Report
# print("\nClassification Report:")
# print(classification_report(y_test, y_pred))


# # Heatmap
# plt.figure(figsize=(5, 4))

# sns.heatmap(
#     cm,
#     annot=True,
#     fmt='d',
#     cmap='Blues'
# )

# plt.title('Spam Detection')
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.show()





