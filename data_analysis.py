# import all required libraries for analysing data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
train_df = pd.read_csv('Metro_Interstate_Traffic_Volume.csv')
print('Dataset shape: ', train_df.shape)
train_df.info()
train_df.head()
train_df.describe(include = 'all')
train_df.isnull().sum()
