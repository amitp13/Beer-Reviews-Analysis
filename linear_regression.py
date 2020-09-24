#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import seaborn as sns
import sqlite3
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# #### 3. Regression

# To predict the overall beer quality we will look at how consumers rated aroma, palate and taste. We will use Multiple Linear Regression to build our model.

# In[28]:


X = data[['avg_review_aroma','avg_review_palate','avg_review_taste']]
Y = data[['avg_review_overall']]


# In[29]:


x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.20,random_state=42)


# In[30]:


#Define the Model
model = linear_model.LinearRegression(normalize = True)
model.fit(x_train,y_train)


# In[31]:


#predicting on test data
pred = model.predict(x_test)


# In[24]:


# prediction with sklearn
aroma = 4.4
palate = 3.9
taste = 4.2
print ('Predicted Overall Beer Quality: \n', model.predict([[aroma,palate,taste]]))


# In[39]:


rmse = np.sqrt(mean_squared_error(y_test,pred))
print('RMSE: {}'.format(rmse))

r2 = r2_score(y_test,pred)
print('R-Sqruared: {}'.format(r2))
