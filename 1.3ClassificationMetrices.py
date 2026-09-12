# classification model predicts categorial values 
# Metrics of classification:--

# 1) Accuracy : proportion of correct predictions made by model out of all predictions 
# accuracy - Number of correct predictions / total no. of predictions 

# In case of imbalanced datasets where a dataset with 90% class A 10% class B, accuracy 
# will predict only for class A and will fail to identify class B 

# 2) Precision : TP/TP+FP     (where TP - True Positive and FP = False Positive )
# it measures how many of the positive predictions made by model are actually correct 

# Precision is very useful in medical diagnosis 

# it is useful when cost of the FP is high such as in medical diagnoiss where predicting a disease
# a disease when it is not present can ahve serious consequences

# 3) Recall / Sensitivity: TP/TP + FN  where FN - False Negative 
# measures how many of the actual positive cases were correctly identified by the model. it is
# important when missing positive case(FN) is more costly than (FP)  recall is a key metrices
# in medical diagnosis

# 4) F1 Score is the harmonic mean of precision and recall 
#  if F1 score ishigh means the model performs well on n=both metrices (precision & recall)
# lower recall and higher presision gives great accuracy but then it missed large no. 
# of instances, more the f1 score higher will be the performance 

# F1 score = 2 X ( Precision X Recall/ Precision + Recall )
# range of F1 score is [0,1] 


# 5) AUC-ROC Curve -- evaluates the model over a spectrum of thresholds where precisions recall 
#  & F1 score provides insight about a model over only a single threshold 

# ROC curve -- 
#             is a graphical reoresentation of TPR (true positive rates) VS the FPR (false positive
# rates) at different classification thresholds 

# TPR = TP/TP+FN  (TP - true positive -- correctly predicted positives cases)
#                 ( FN - False Negative -- actual positive cases incorrectly predicted as negative )

# TPR -- it measures - out of all actual positive cases how many did themodel correctly identified 



# TNR -- True Negative Rate -- TN/TN+FP
            #   TN - True Negative (correctly predicted negative cases)
            #   FP - False Positive (actual negative cases incorrectly predicted as positive) 
            
# so TNR measures how many actual negative instances were correctly identified by the model
# or we can say that out of all actual negative how many did the md]odel correctly
# identified as negative    


# AUC Curve -- 
            #  ---  how to read AUC values -----
            # the range of AUC from 0 to 1
            # 1- perfect model 
            # 0.8 to 0.9 - the model is good or excellent 
            # 0.7 to 0.8 - the model is cceptable 
            # 0.5 - RAndom guessing (no skill)
            # less than 0.5 -- worse than Random guessing
            
# confusion Matrix - It is a NXN matrix where N is the no. of classes/categories to be predicted 
# if we have N = 2 we get 2X2 matrix

              