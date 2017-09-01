import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

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

# We are trying to apply y = C1X1 + C2X2 + C3
# y(w, x) = w_0 + w_1 x_1 + ... + w_n x_n
# Factors that may lead to diabetes
X = array[:,0:8]
# People who actually got diabetes and who don't
Y = array[:,8]
kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression()

# scoring = 'neg_mean_absolute_error'
scoring = 'r2'
# scoring = 'neg_mean_absolute_error'

results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print results
print("Scoring: %.3f (%.3f)") % (results.mean()*100.0, results.std()*100.0)






