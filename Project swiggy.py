#!/usr/bin/env python
# coding: utf-8

# # ExxpertSCM internship task
# 
# ### Data Analytics Assigment ---- Project - 1
# ###  Swiggy Data Analysis

# ######    Project 1- Swiggy or similar platform data set. On all India basis, based on at least 3-month data
#     Tasks - 1. The top 3 food ordered
#     2. Top 3 Shops doing maximum business
#     3. Bottom 3 rated shops
#     4. Average delivery time for items in Task 1

# ### By Mohamad Ehthesham S

# LinkedIn - https://www.linkedin.com/in/-mohamad-ehthesham/overlay/contact-info/
# 
# GitHub - https://github.com/MohamadFaiz0102

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt

import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# Data can be found here - https://www.kaggle.com/datasets/aniruddhapa/swiggy-restaurants-dataset-of-metro-cities?select=Swiggy_dataset.csv

# In[2]:


db=pd.read_csv('Swiggy_dataset.csv')


# In[3]:


db.head(2)


# In[4]:


db.info()


# ### Nulls

# In[5]:


db.isnull().sum()
# deleting uuid,avgrating, address,llocality,unserisable,veg,city2 these have null values


# In[6]:


# deleting unnecessary columns
# deleting type,uuid,avgrating, address,llocality,unserisable,veg,city2

db.drop(['type','uuid','address','area','locality','unserviceable','City2'],inplace=True,axis=1)


# In[7]:


db.head(2)


# ### Cleaning the data by deleting commas and brackets 

# In[8]:


db['cuisines']=db['cuisines'].str.replace('[','',regex=True);
db['cuisines']=db['cuisines'].str.replace(']','',regex=True);
db['cuisines']=db['cuisines'].str.replace("'",'',regex=True);


# In[9]:


db.head(2)


# ### Task 1

# ### The top 3 food ordered

# In[10]:


t1=db['cuisines'].value_counts().head(5)
t1


# #### Visuals

# In[11]:


t1.plot(kind='bar',figsize=(10,8),color='olive')

plt.title('The top 5 food ordered',fontsize=15)

plt.ylabel('Total Orders',fontsize=15)
plt.xlabel('Names',fontsize=15)

plt.xticks(rotation=360,ha='right');


# ####    So Indian, North Indian , Fast Food are top orderd foods

# ### Task 2

# In[12]:


# check uniques for costforTwo

a=db['costForTwoStrings'].unique()
# a


# In[13]:


# seperating the strings from costForTwoStrings and converting to int

db['costForTwoStrings']=db['costForTwoStrings'].replace('₹','',regex=True).replace('FOR TWO','',regex=True).replace(' ','',regex=True)

db['costForTwoStrings']=db['costForTwoStrings'].astype(int)

db['costForTwoStrings'].unique()


# In[14]:


db.head(2)


# In[15]:


# check restaraounts for max price and rating

m=db.groupby(['name','avgRating'])[['costForTwoStrings']].sum().nlargest(5,'costForTwoStrings')
m


# ### Top 3 restaurants doing maximum business

# In[16]:


# check restaraounts for max price

t2 =db.groupby(['name'])[['costForTwoStrings']].sum().nlargest(5,'costForTwoStrings')

t2
# so top 3 restaraunts doing maximum business are Mainland China, Oven Story Pizza, Behrouz Biryani


# In[17]:


t2.plot(kind='bar',figsize=(10,8),color='brown',legend=None)

plt.title('The top 5 maximum Restaraunts doing Business',fontsize=15)

plt.ylabel('Total Order Prices',fontsize=15)
plt.xlabel('Names',fontsize=15)

plt.tight_layout()

plt.xticks(rotation=50,ha='right');


# ####    So top 3 restaraunts doing maximum business are Mainland China, Oven Story Pizza, Behrouz Biryani

# ### Task 3

# In[18]:


nu=db['name'].value_counts()
nu.head(5)


# In[19]:



db[db['avgRating']=='--'].head()


#     # There are about 1949 such rows, we will drop these 1949 rows because the value for 'rate' column is '--'

# In[20]:


a=db.loc[db['avgRating']=='--'].index
db.drop(a,axis=0,inplace=True)


# In[21]:


# db[db['avgRating']=='--'].head()


# In[22]:


# check for null vlues in ratings
db['avgRating'].isnull().sum()


# In[23]:


# convert all null / empty values to 0 or 1 in ratings

db['avgRating']=db['avgRating'].fillna(0)


# In[24]:


# converting avgRating to float
db['avgRating']=db['avgRating'].astype(float)


# In[25]:


db[['totalRatingsString','avgRating']].sort_values(by='avgRating',ascending=False).head(5)


# In[26]:


db['avgRating'].unique()


# In[27]:


db[db['avgRating']==5][['name','avgRating']]


# In[28]:


db['totalRatingsString'].unique()


# In[29]:


db[['name','avgRating']].sort_values(by='avgRating',ascending=False)


# In[30]:


db.head(2)


# ### Top 3 rated Shops

# In[31]:



ab=db[(db['avgRating']==5) & (db['totalRatingsString'].isin(['50+ ratings','5000+ ratings','20+ ratings']))][['name','avgRating','totalRatingsString']].tail(5)
ab


# ####   So from the above result we can see that Cafe Kokomo, NIVALA APKA APNA, The Asian Pavilion are the Top 3 rated restaraunts  

# ### Bottom 3 rated shops

# In[32]:


# Bottom 3 rated shops

db[(db['avgRating']==0) & (db['totalRatingsString']=='Too Few Ratings')][['name','avgRating','totalRatingsString']].tail(5)

# so Bottom 3 rated shops are PAPACREAM, CREAM AND FUDGE, Ammi's Biryani


# ### Task 4

# ### Average delivery time for items in Task 1

#     Indian          
#     Chinese         
#     North Indian    

# In[33]:


db.head(2)


# #### Indian

# In[34]:


# Average delivery time for items in Task 1

t4a=db[db['cuisines']=='Indian'][['deliveryTime']].mean()
t4a


# ####    So Average delivery time for Indian food is 56.65 minutes

# #### Chinese

# In[35]:


t4b=db[db['cuisines']=='Chinese'][['deliveryTime']].mean()
t4b


# #### So Average delivery time for Indian food is 56.036 minutes

# #### North Indian

# In[36]:


t4c=db[db['cuisines']=='North Indian'][['deliveryTime']].mean(axis=0)
t4c


# #### So Average delivery time for Indian food is 51.01 minutes

# In[37]:


# 3 combined

t4d=db[db['cuisines'].isin(['Indian','Chinese','North Indian'])][['deliveryTime']].mean()
t4d


# In[46]:


t4a=db[db['cuisines']=='Indian']['deliveryTime'].mean()
t4b=db[db['cuisines']=='Chinese']['deliveryTime'].mean()
t4c=db[db['cuisines']=='North Indian']['deliveryTime'].mean()

a=[t4a,t4b,t4c]
print(a)

plt.figure(figsize=(10,7))

plt.xlabel('Cuisines',fontsize=15)
plt.ylabel('Avg Delivery Time',fontsize=15)

plt.title('Average cuisines of Top 3 food ordered',fontsize=15)

plt.plot(['Indian','Chinese','North Indian'],a,color='g',marker='*');


# In[ ]:





# ............

#                                                         Thank You 

# In[ ]:




