# convert the date_time column to datetime type
train_df['date_time'] = pd.to_datetime(train_df['date_time'])

# Time vs Traffic Flow
train_df['time'] = train_df['date_time'].dt.hour
fig, (axis1,axis2) = plt.subplots(2, 1, figsize = (20,12))
sns.countplot(x = 'time', data = train_df, ax = axis1, palette="Set3" )
sns.lineplot(x = 'time', y = 'traffic_volume', data = train_df, ax = axis2);

# Month vs Traffic Flow
train_df['month'] = train_df['date_time'].dt.month
fig, (axis1,axis2) = plt.subplots(2, 1, figsize = (20,12))
sns.countplot(x = 'month', data = train_df, ax = axis1, palette="Set3")
sns.lineplot(x = 'month', y = 'traffic_volume', data = train_df, ax = axis2,)

# Year vs Traffic Flow
train_df['year'] = train_df['date_time'].dt.year
fig, (axis1,axis2) = plt.subplots(1, 2, figsize = (20,6))
sns.countplot(x = 'year', data = train_df, ax = axis1, palette="Set2")
sns.lineplot(x = 'year', y = 'traffic_volume', data = train_df, ax = axis2);

# Day vs Traffic Volume
train_df['day'] = train_df['date_time'].dt.day_name()
fig, (axis1,axis2) = plt.subplots(1, 2, figsize = (20,6))
sns.countplot(x = 'day', data = train_df, ax = axis1)
sns.lineplot(x = 'day', y = 'traffic_volume', data = train_df, ax = axis2);

# Holiday vs Traffic Flow
train_df['holiday'].value_counts()
z = lambda x: False if x == 'None' else True
train_df['holiday'] = train_df['holiday'].apply(z)

fig, (axis1,axis2) = plt.subplots(1, 2, figsize = (20,6))
sns.countplot(x = 'holiday', data = train_df, ax = axis1)
sns.barplot(x = 'holiday', y = 'traffic_volume', data = train_df, ax = axis2);

# Temperature vs Traffic Flow
(train_df['temp'] == 0).sum()
train_df = train_df[train_df['temp'] != 0]
sns.scatterplot(x = 'temp', y = 'traffic_volume', data = train_df);

# Rain vs Traffic Flow
(train_df['rain_1h'] > 100).sum()
train_df = train_df[train_df.rain_1h < 100]
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sns.scatterplot(x = 'rain_1h', y = 'traffic_volume', data = train_df,);

# Snow vs Traffic Flow
sns.scatterplot(x = 'snow_1h', y = 'traffic_volume', data = train_df);

# Clouds vs Traffic Flow
sns.scatterplot(x = 'clouds_all', y = 'traffic_volume', data = train_df);

# Short Weather Description vs Traffic Volume
fig, (axis1,axis2) = plt.subplots(2, 1, figsize = (16,12))
sns.countplot(x = 'weather_main', data = train_df, ax = axis1)
sns.lineplot(x = 'weather_main', y = 'traffic_volume', data = train_df, ax = axis2);

# Long Weather Description vs Traffic Flow
train_df['weather_description'].value_counts()
plt.figure(figsize = (20,6))
sns.lineplot(x = 'weather_description', y = 'traffic_volume', data = train_df);
