## Traffic Flow Analysis in different weather conditions
This is our academic project for CS-584 "Machine Learning". 

### Problem Statement
In current life there are a lot of pressing issues one of which is traffic congestion which needs to be addressed as it is getting more serious for quite a while. The high volume of vehicles, the lack of infrastructure and the uneven distribution of the development are the primary reasons of traffic congestion.
Traffic flow analysis and forecasting has always been a topic of enormous significance. This information can be used by the government and traffic police to better guide traffic and ensure its efficient and free flow. The knowledge gained can stop traffic jams in the future and spare commute time and resources effectively. Since emergency services like the ambulance can get to hospitals more quickly, it can also save lives. To successfully address these issues, traffic flow prediction is crucial.

### Datasets
Over the years, various approaches of predicting traffic flow volume have been put forth. We used the Metro Interstate Traffic Volume Data Set in our project. This dataset is considered because it includes a variety of elements, including weather information and is way clear than its predecessor. It contains hourly traffic data along the Minneapolis–St. Paul route.

### Data Cleaning and Data Preparation
1. Remove unneeded columns from the dataset that won't help in prediction. These are removed after examining the correlation between features.
2. Convert values to numerical format so that the algorithms can utilize them to make predictions, in order to correctly use the machine learning methods.
3. The data contains a number of rows with these values. The very big values are replaced by the maximum value that has been established, and the missing values are replaced by the mean values.

### Algorithms used
1. Linear Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. AdaBoost

### Results
The several ML models were put into practice, and the outcomes were compared to determine which model performed the best. The root mean square error for linear regression was 1844.35. 
1. The decision tree regressor outperformed the linear regression model with an accuracy rating of 94% and RMSE value of 479.64. 
2. The Random Forest produced a 95 percent accuracy rating with an RMSE value of 429.38, which is still an improvement over the previous model. 
3. Additionally, the AdaBoost method was used, with 60 estimators and a learning rate of 0.005, to create a model with a 95 percent accuracy rate and a 435.99 root mean square error. 
4. We have used the gradient boosting approach by setting the estimators count to 600, which results in an accuracy rating of 97 percent and root mean square error value of 362.48. 
5. The gradient boost approach, thus, provides the better accuracy value and the lowest root mean square error value when all the models are compared.
6. As a result, it can also be used to forecast traffic flow for hypothetical future use cases.
