#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#reading the csv
uberData = pd.read_csv('uber-raw-data-jul14.csv')


# In[3]:


uberData.head()


# In[4]:


#getting rid of the data I was not going to use
uberData.drop(['Lat','Lon'], axis =1)


# In[5]:


uberData.shape


# In[6]:


#checking the the type of the column date time
type(uberData.loc[0,'Date/Time'])


# In[7]:


#converting the date/time column to datetime for easier indexing
uberData['Date/Time'] = pd.to_datetime(uberData['Date/Time'])


# In[8]:


#showing that it chaned 
type(uberData.loc[0,'Date/Time'])


# In[9]:


#graphing the amount of rides per day in the month of july in 2014
plt.figure(figsize=(15,8))
#if we we did not make the Date/Time in the dt format we would not be able to do this 
uberData['Date/Time'].dt.day.value_counts().sort_index().plot(kind='bar',color="blue")
plt.title('NYC Uber rides per day in July 2014')
plt.xlabel('Days in the month of July')
plt.ylabel('Amount of rides')


# In[10]:


#making the data easier to analyze and graph
uberData['flooredData']=uberData['Date/Time'].dt.floor('15min')
#this will make all the data that below 15 to 0 also below 30 will be become 15 


# In[11]:


uberData.head()
#checking the new column and seeing the data has changed


# In[12]:


#Plotting all the intervals of 15 mins over the course of the month of july for every day 
plt.figure(figsize=(15,8))
uberData['flooredData'].value_counts().sort_index().plot(c='blue')
plt.title('NYC Uber rides per 15 minutes in July 2014')
plt.xlabel('Days in the month of July')
plt.ylabel('Amount of rides')


# In[13]:


uberData['flooredData'].value_counts()


# In[14]:


#testing
date = uberData.loc[0,'flooredData']
print(date.day_name())


# In[15]:


#Getting all the dates to have weekday values 
uberData['dayOfWeek'] = uberData['Date/Time'].dt.day_name()
uberData.head()


# In[16]:


dayData = uberData['dayOfWeek'].value_counts()
dayData


# In[17]:


days = pd.unique(uberData["dayOfWeek"])


# In[18]:


#creating a bar graph to show the amount of rides on each given day
plt.figure(figsize=(10,10))
order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
ax = sns.barplot(y = dayData, x = days, order = order)
plt.ylabel('Amount of rides')
plt.title('Total NYC Uber rides per day in July 2014')


# In[19]:


uberData.head()


# In[20]:


#Creating a row for just the time of the day
uberData['timeOfDay'] = uberData['Date/Time'].dt.time
uberData.head()


# In[21]:


#Creating a row for just the date
uberData['date'] = uberData['Date/Time'].dt.date
uberData.head()


# In[22]:


#creating a table to count the number of rides
weeklyData = uberData.groupby(['date','dayOfWeek','timeOfDay']).count().dropna().rename(columns={'flooredData':'rides'})['rides'].reset_index()
weeklyData.head()


# In[ ]:





# In[23]:


weeklyData = weeklyData.groupby(['dayOfWeek','timeOfDay']).mean()['rides']
weeklyData.head()


# In[24]:


#unstacking data to later create a heatmap
weeklyData= weeklyData.unstack(level=0)
weeklyData.head()


# In[25]:


#Issue here is that its not in oder so the map is not quite what we are looknig for 
plt.figure(figsize=(15,15))
sns.heatmap(weeklyData)
plt.title('Heatmap of average rides in time')


# In[26]:


weeklyData.head()


# In[27]:


#Ordering the columns
weeklyData = weeklyData.reindex(columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
weeklyData.head()


# In[28]:


weeklyData.mean()


# In[29]:


#fixed the order 
plt.figure(figsize=(15,15))
sns.heatmap(weeklyData)
plt.title('Heatmap of the average amount of rides at specific times during each day of the week')


# In[30]:


#plotting the time of the day and averages of amount of rides per day
plt.figure(figsize=(15,12))
weeklyData.plot(kind="line")


# In[ ]:





# In[ ]:




