# Regression metrics is used to evaluate the performance of regression model below metrics are used :


                                #    MAE - Mean Absolute Error
                                # it calculate the avg of diff between the predicted and the actual value 
                                
                                # MSE - MEan Square Error 
                                
                                # It calculates the squared differences between the predicted and actual 
                                # values, squaring the difference ensure larger error are penalized making 
                                # it sensitive to outliners
                                
                                
                                # RMSE - Root Mean Square Error 
                                
                                # square root of MSE , like MSE it heavily penalises large error: it is
                                # useful when we want to know how much our prediction deviates from the 
                                # actual values in terms of the same scale 
                                
                                # RMSLE - Root Mean Squared Logarithmic Error
                                 
                                # useful when target variable span wide range of values RMSLE is helpful
                                # where we are predicting qualities that very greatly in scale like 
                                # predicting prices or population.
                                
                                # R2Score -- R-Squared
                                
                                # represents the proportion of varience in the dependent variaable 
                                # that is predictable from independent variable 
                                
                                # R2 value close to 1 shows a model that explain the most of the varience
                                # R2 value close to 0 show the model does not explain much of the varience
                                # in data
                                # R2 score is used to access the goodness-of-fit regression models 
                                 