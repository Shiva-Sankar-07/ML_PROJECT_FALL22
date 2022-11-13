# import the required modules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor

(X, Y) = (train_df.drop(['traffic_volume'], axis = 1).values, train_df['traffic_volume'].values)

# Scale the values
scaler = StandardScaler()
X = scaler.fit_transform(X)

(X_train, X_val, Y_train, Y_val) = train_test_split(X, Y)
print("X_train shape:" + str(X_train.shape))
print("Y_train shape:" + str(Y_train.shape))
print("X_val shape:" + str(X_val.shape))
print("Y_val shape:" + str(Y_val.shape))

# DataFrame to store the RMSE scores of various algorithms
results = pd.DataFrame(columns = ['RMSE'])

# helper function to evaluate a model
def evaluate_model(regressor, name):
    # train and test scores
    train_score = round(regressor.score(X_train, Y_train), 2)
    val_score = round(regressor.score(X_val, Y_val), 2)
    # predicted output
    Y_pred = regressor.predict(X_val)
    
    print(name + ' Train score: ', train_score)
    print(name + 'Test score: ', val_score)
    print('Root Mean Squared error: ', sqrt(mean_squared_error(Y_val, Y_pred)))
    print('Coefficient of determination: ', r2_score(Y_val, Y_pred))
    
    # add the current RMSE to the scores list
    results.loc[name] = sqrt(mean_squared_error(Y_val, Y_pred))
    
    # plot predicted vs true values
    x_points=np.linspace(0,8e3)
    plt.figure(figsize=(12,5))
    plt.plot(x_points, x_points, color='r')
    plt.scatter(Y_val, Y_pred)
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title('True Values Vs Predicted Values');

#Linear Regression
lireg = LinearRegression()
lireg.fit(X_train, Y_train)

#calling linear regression function
LinearRegression()

#evaluating the linear regression model
evaluate_model(lireg, 'Linear Regression')

#DecisionTreeRegressor
dtreg = DecisionTreeRegressor(max_depth = 12)
dtreg.fit(X_train,Y_train) 

#calling the DecisionTreeRegressor function
DecisionTreeRegressor(max_depth=12) 

#evaluating the DecisionTreeRegressor model
evaluate_model(dtreg, "Decision Tree")

#Random Forest 
# n_estimators - The number of trees in the forest.
# min_samples_split - The minimum number of samples required to split an internal node
rfreg = RandomForestRegressor(n_estimators = 60, max_depth = 13, min_samples_split = 5)
rfreg.fit(X_train, Y_train)

#Calling the Random Forest function
RandomForestRegressor(max_depth=13, min_samples_split=5, n_estimators=60)

# evaluate the Random Forest 
evaluate_model(rfreg, 'Random Forest')

