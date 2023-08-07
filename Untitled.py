#!/usr/bin/env python
# coding: utf-8

# Here,The Weather Dataset is a time-series data set with per-hour information about the weather conditions at a paritcular 
# Location. It recors temperature, Dew Point temperature, Relative humudity,Wind speed,Visibilty,pressure,and conditions
# 
# This Datasets is available as a CSV file . We are going to analize the data set using the pandas DATAFRAME.

# # THE WEATHER DATASETS

# In[2]:


import pandas as pd


# In[3]:


data= pd.read_csv("Weather Data.csv")


# In[4]:


data


# In[ ]:





# In[5]:


data.head()


# In[6]:


data.shape


# In[7]:


data.index


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[10]:


data['Weather'].unique()


# In[11]:


data.nunique()


# In[12]:


data.count()


# In[14]:


data['Weather'].value_counts()


# In[15]:


data.info()


# # ASK 1 All the unique 'WIND SPEED' values in the data

# In[17]:


data.head(5)


# In[22]:


data['Wind Speed_km/h'].nunique()


# In[23]:


data['Wind Speed_km/h'].unique()


# # Q)2. find all the numbers of times when the "weather is exactly clear".

# In[24]:


data.head(5)


# In[25]:


# value_counts() first way to show the result
data.Weather.value_counts()


# In[27]:


# filtering the second way
#data.head(2)
data[data.Weather =='Clear']


# In[28]:


#group() the third way
data.head(5)
data.groupby('Weather').get_group('Clear')


# # Q)3. find the number of times when the "Wind speed Exactly was 4km/h"

# In[29]:


data.head(5)


# In[31]:


data[data['Wind Speed_km/h']==4]


# # Q)3. Find all the Null values in data

# In[32]:


data.isnull().sum()


# In[33]:


data.notnull().sum()


# # Q)5.Rename the columns name 'Weather' of the data frame to Weather conditon.

# In[34]:


data.head(5)


# In[39]:


data.rename(columns={'Weather':'Weather conditon'})


# In[40]:


data.head()


# # Q)6 What is mean "visiblity"

# In[42]:


data.head(5)


# In[43]:


data.Visibility_km.mean()


# In[45]:


data.Visibility_km.std()


# # Variance of "Relative humidity"

# In[47]:


data['Rel Hum_%'].var()


# # Q)7.FInd all the instances when "Snow" was recorded

# In[49]:


#value_counts()
data.head(5)
data['Weather conditon'].value_counts()


# In[50]:


#filtering
data[data["Weather conditon"]=='Snow']


# In[52]:


#str.contains
data[data['Weather conditon'].str.contains("Snow")].head(50)


# In[53]:


#str.contains
data[data['Weather conditon'].str.contains("Snow")].tail(50)


# In[54]:


#str.contains
data[data['Weather conditon'].str.contains("Snow")].tail(50)


# # Q)8. Find all the instances When 'Wind Speed is above 24' and 'Visibility is 25'.

# In[55]:


data.head(5)


# In[56]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)]


# # Q)9.What is the mean value of each column against each "Weather condtion ?"

# In[57]:


data.head(5)


# In[58]:


data.groupby('Weather conditon').mean()


# In[ ]:





# In[ ]:





# In[ ]:




