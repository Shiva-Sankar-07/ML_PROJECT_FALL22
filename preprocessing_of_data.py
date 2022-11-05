from sklearn.preprocessing import LabelEncoder

# drop the unrequired columns
train_df.drop(['date_time', 'weather_description'], axis = 1, inplace = True)

# convert values of day column to numerical format
encoder = LabelEncoder()
train_df['day'] = encoder.fit_transform(train_df['day'])

# subtract 242 from the temp column as there is no temperature below it
train_df['temp'] = train_df['temp'] - 242

# convert the values of weather_main column to numerical format
encoder = LabelEncoder()
train_df['weather_main'] = encoder.fit_transform(train_df['weather_main'])
