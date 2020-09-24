#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import seaborn as sns
import sqlite3
import matplotlib.pyplot as plt

#### 2. Exploratory Data Analysis

# In[47]:


viz_abv = data.sort_values('beer_abv').tail(5)
sns.barplot(x="beer_abv",y="beer_name",  
            palette="Blues_d", 
            order=viz_abv.sort_values('beer_abv',ascending=False).beer_name,
            label = "Beers with Highest ABV",
            data=viz_abv)


# In[50]:


viz_abv = data.sort_values('avg_review_taste').tail(10)
viz_abv[['beer_name','brewery_name','beer_style','beer_abv']]


# In[51]:


viz_abv = data.sort_values('avg_review_overall').tail(10)
viz_abv[['beer_name','brewery_name','beer_style','beer_abv']]


# In[52]:


data_quant = data[['beer_abv','avg_review_appearance','avg_review_aroma',
                   'avg_review_palate','avg_review_taste', 'avg_review_overall']]
corr = data_quant.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, linewidth=0.5)


# Here we see that taste, palate and aroma are most closely related to high overall ratings. Next we will look at how these three factors on a regression line.

# In[64]:


fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(8,8))
sns.lineplot(x='avg_review_aroma',y='avg_review_overall', data=data, ax = ax1).set_title('Aroma vs Review');
sns.lineplot(x='avg_review_taste',y='avg_review_overall', data=data, ax = ax2).set_title('Taste vs Review');
sns.lineplot(x='avg_review_palate',y='avg_review_overall', data=data, ax = ax3).set_title('palate vs Review');
plt.show()


# We see that aroma, taste and palate are good indicator to a highly rated beer. So these can be used in our Regression models.