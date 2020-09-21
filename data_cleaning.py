#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
import sqlite3


# In[80]:


#Code for getting dataframes from various queries fired on the database
def query_result_df(q):
    conn = sqlite3.connect(r'C:\Users\phadk\Desktop\Work\projects\Beer Reviews\beer.db')
    con = conn.cursor()
    query = con.execute(q)
    cols = [column[0] for column in query.description]
    result_df = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    return result_df


# In[81]:


#getting a dataframe with all results from beer_master table 
data = query_result_df('''SELECT * FROM beer_master''')


# In[82]:


data.head()


# #### 1. Data Cleaning

# In[83]:


data.describe()


# Here We see that reviews are given between a value of 1 to 5. The value of beer ABV(Alcohol By Volume) level is continuous value upto 57.7.

# In[84]:


data.isna().sum()


# We see that beer_abv column has 17043 missing values. Here we can use a few strategies to fill out these values. We can analyze if certain beer styles in our dataset have a particular abv range and then fill the abv values as per our analysis.  

# In[85]:


#query to get average abv values from the style of a certain beer
data_abv = query_result_df('''SELECT beer_style, min(beer_abv) as min_abv, max(beer_abv) as max_abv, 
                    min(beer_abv)+ max(beer_abv)/2 AS avg_abv 
                    FROM beer_master 
                    GROUP BY beer_style''')

data = data.merge(data_abv,how="left",on='beer_style')
data['beer_abv'] = data['beer_abv'].fillna(value=data['avg_abv'])

data.drop(['min_abv','max_abv','avg_abv'], axis=1, inplace=True)


# In[ ]:




