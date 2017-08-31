import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

pd.set_option('display.expand_frame_repr', False)

url = "https://goo.gl/vhm1eU"

'''
1. preg = Number of times pregnant 
2. plas = Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
3. pres = Diastolic blood pressure (mm Hg) 
4. skin = Triceps skin fold thickness (mm) 
5. test = 2-Hour serum insulin (mu U/ml) 
6. mass = Body mass index (weight in kg/(height in m)^2) 
7. pedi = Diabetes pedigree function 
8. age = Age (years) 
9. class = Class variable (0 or 1) 
'''

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(url, names=names)
# print type(dataframe)

# df_head = dataframe.head()
# print df_head

# df_shape = dataframe.shape
# print df_shape

# df_dtypes = dataframe.dtypes
# print df_dtypes

# df_describe = dataframe.describe()
# print df_describe

# df_correlation = dataframe.corr()
# print df_correlation

array = dataframe.values
# separate array into input and output components
scale_X = array[:,0:8]
# StandardScaler will create a scaler object that has properties to further transform the dataframe
# scaler is actually this object StandardScaler(copy=True, with_mean=True, with_std=True)
# Change with_std or with_mean properties to transform the dataframe according to yourself
# Generally they are both true because to scale, we first subtract the mean and then divide by std_dev
# Above transformation will make all the features(factors) revolve around 0 (i.e. mean=0 and variance=1)
scaler = StandardScaler().fit(scale_X)

print scaler.with_mean
rescaledX = scaler.transform(scale_X)
# summarize transformed data
np.set_printoptions(precision=3)
print(rescaledX[0:5,:])