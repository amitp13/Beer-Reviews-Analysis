#!/usr/bin/env python
# coding: utf-8

# <center> <h1> Beer Reviews </h1> </center>
# 
# The following jupyter notebook is an analysis of more 50,000 beers across the world and how users have reviewed them based on aroma, taste, appearance, palate, etc. We will first look at the different subtypes of ratings and how much correlation do they have to the overall rating and which are the strongest indicators of high rated beer. Secondly we will look at the relation between ABV(alcohol level by volume) and ratings. The notebook is split in three phases namely Data Cleaning, Exploratory Data Analysis and Modelling. 

# #### 1. Data Preparation

# All our data is placed in the database beer.db. With help sqlite3 we will extract only the data we require through SQL queries. The data we will use for our prediction will be average values for aroma, palate, appearance and so on for each beer.  

# In[37]:


import pandas as pd
import numpy as np
import seaborn as sns
import sqlite3
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# In[2]:


#Code for getting dataframes from various queries fired on the database
def query_result_df(q):
    conn = sqlite3.connect(r'C:\Users\phadk\Desktop\Work\projects\beer.db')
    con = conn.cursor()
    query = con.execute(q)
    cols = [column[0] for column in query.description]
    result_df = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    return result_df


# In[3]:


#getting a dataframe with all results from beer_master table 
data = query_result_df('''SELECT beer_beerid, beer_name, brewery_id, brewery_name, beer_style, beer_abv, ROUND(AVG(review_appearance),2) AS avg_review_appearance, 
ROUND(AVG(review_aroma),2) AS avg_review_aroma, ROUND(AVG(review_palate),2) AS avg_review_palate, 
ROUND(AVG(review_taste),2) AS avg_review_taste, ROUND(AVG(review_overall),2) AS avg_review_overall 
FROM beer_reviews 
GROUP BY beer_beerid''')


# In[4]:


data.head()


# #### 1. Data Cleaning

# In[5]:


data.describe()


# Here We see that reviews are given between a value of 1 to 5. The value of beer ABV(Alcohol By Volume) level is continuous value upto 57.7.

# In[6]:


data.isna().sum()


# We see that beer_abv column has 17043 missing values. Here we can use a few strategies to fill out these values. We can analyze if certain beer styles in our dataset have a particular abv range and then fill the abv values as per our analysis.  

# In[7]:


#query to get average abv values from the style of a certain beer
data_abv = query_result_df('''SELECT beer_style,min(beer_abv)+ max(beer_abv)/2 AS avg_abv 
FROM (SELECT beer_beerid, beer_name, brewery_id, brewery_name, beer_style, beer_abv, ROUND(AVG(review_appearance),2) AS avg_review_appearance, 
ROUND(AVG(review_aroma),2) AS avg_review_aroma, ROUND(AVG(review_palate),2) AS avg_review_palate, 
ROUND(AVG(review_taste),2) AS avg_review_taste, ROUND(AVG(review_overall),2) AS avg_review_overall 
FROM beer_reviews 
GROUP BY beer_beerid)
GROUP BY beer_style''')

data = data.merge(data_abv,how="left",on='beer_style')
data['beer_abv'] = data['beer_abv'].fillna(value=data['avg_abv'])

data.drop(['avg_abv'], axis=1, inplace=True)


# #### 2. Exploratory Data Analysis

# In[8]:


viz_abv = data.sort_values('beer_abv').tail(5)
sns.barplot(x="beer_abv",y="beer_name",  
            palette="Blues_d", 
            order=viz_abv.sort_values('beer_abv',ascending=False).beer_name,
            label = "Beers with Highest ABV",
            data=viz_abv)


# In[9]:


viz_abv = data.sort_values('avg_review_taste').tail(10)
viz_abv[['beer_name','brewery_name','beer_style','beer_abv']]


# In[10]:


viz_abv = data.sort_values('avg_review_overall').tail(10)
viz_abv[['beer_name','brewery_name','beer_style','beer_abv']]


# In[11]:


data_quant = data[['beer_abv','avg_review_appearance','avg_review_aroma',
                   'avg_review_palate','avg_review_taste', 'avg_review_overall']]
corr = data_quant.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, linewidth=0.5)


# Here we see that taste, palate and aroma are most closely related to high overall ratings. Next we will look at how these three factors on a regression line.

# In[12]:


fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(8,8))
sns.lineplot(x='avg_review_aroma',y='avg_review_overall', data=data, ax = ax1).set_title('Aroma vs Review');
sns.lineplot(x='avg_review_taste',y='avg_review_overall', data=data, ax = ax2).set_title('Taste vs Review');
sns.lineplot(x='avg_review_palate',y='avg_review_overall', data=data, ax = ax3).set_title('palate vs Review');
plt.show()


# We see that aroma, taste and palate are good indicator to a highly rated beer. So these can be used in our Regression models.

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


# #### 4. Conclusion

# From our regression model we got great results for predicting our beer quality with factors like aroma, palate and taste. Our Root squared Mean Error was 0.28 and r-Squared value was 0.79. These metric show us that our model is highly accurate for prediction. 
# 
# In conclusion if your beer smells good, has a great taste and gives the consumer a good mouth feel then your beer will be quite popular. 

# In[ ]: