#!/usr/bin/env python
# coding: utf-8

# # Working on Real Project with Python

# # (A part of Big Data Analysis)

# # The Weather Dataset 

# Here, The Weather Dataset is a time-series data set with per-hour information about the weather conditions at a particular location. it records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressurw, and Conditions.
# 
# The data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame.

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv(r"C:\Users\pawar\Downloads\1. Weather Data.csv")


# In[4]:


data


# In[ ]:





# # How to Analyze Dataframes ?

# # .head()

# it shows the first N rows in the data (by default,N=5)

# In[5]:


data.head()


# # .shape

# it shows the total no. of eows and no. of columns of the dataframe

# In[6]:


data.shape


# # .index

# this attribute provides the index of the dataframe

# In[7]:


data.index


# # .columns

# it shows the name of each column

# In[8]:


data.columns


# # .dtypes

# it shows the data-type of each column

# In[9]:


data.dtypes


# # .unique()

# In a column. it shows all the unique values. it can be applied on a single column only. not on the whole dataframe.

# In[10]:


data['Weather'].unique()


# # .nunique()

# It shows the total no. of unique values in each column. It can be applied on a single column as well as on whole dataframe.

# In[11]:


data.nunique()


# # .count

# It shows the total no. of non-null values in each column. It can be applied on a single column as well on whole dataframe.

# In[12]:


data.count()


# # .value_counts

# In a column. it shows all shows all the unique values with their count. It can be applied on single column only.

# In[13]:


data['Weather'].value_counts()


# # .info()

# Provides basic informatin about the dataframe.

# In[14]:


data.info()


# # Q) 1. Find all the unique 'Wind Speed' values in the data.

# In[15]:


data.head(2)


# In[16]:


data.nunique()


# In[17]:


data['Wind Speed_km/h'].nunique()


# In[18]:


data['Wind Speed_km/h'].unique() # Answer


# # Q) 2. Find the number of times when the 'Weather is exactly Clear'.

# In[19]:


data.head(2)


# In[20]:


# value_counts()
data.Weather.value_counts()


# In[21]:


# Filtering
#data.head(2)
data[data.Weather == 'Clear']


# In[22]:


# groupby()
#data.head(2)
data.groupby('Weather').get_group('Clear')


# # Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[23]:


data.head(2)


# In[24]:


data[data['Wind Speed_km/h'] == 4] #Answer


# # Q.4) Find out all the Null Values in the data.

# In[25]:


data.isnull().sum()


# In[26]:


data.notnull().sum()


# # Q.5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[27]:


data.head(2)


# In[28]:


data.rename(columns = {'Weather' : 'Weather Condition'})


# In[29]:


data.head()


# # Q.6) What is the mean 'Visibility'?

# In[30]:


data.head(2)


# In[31]:


data.Visibility_km.mean()


# # Q.7) What is the Standard Deviation of 'Pressure' in thid data?

# In[32]:


data.Press_kPa.std()


# # Q.8) Whats is the Variance of 'Relative Humidity' in this data ?

# In[33]:


data['Rel Hum_%'].var()


# # Q.9) Find all instances when 'Snow' was recorded.

# # Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

# In[34]:


data.head(2)


# In[35]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# # Q. 11) What is the Mean value of each column against each 'Weather Condition'?

# In[36]:


data.head(2)


# In[37]:


data.groupby('Weather').mean()


# # Q. 12) What is the Minimum & Maximum value of each column against each 'Wearher C'

# In[38]:


data.head(2)


# In[39]:


data.groupby('Weather').max()

