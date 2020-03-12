#!/usr/bin/env python
# coding: utf-8

# ## Libraries

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ## Dataset 
# (***obtained from kaggle.com***)

# corona = pd.read_csv("novel-corona-virus-2019-dataset/2019_nCoV_data.csv")

# In[3]:


corona.head(10)


# In[4]:


corona.describe()


# In[5]:


sns.relplot(x = "Confirmed", y = "Deaths", data=corona)


# In[6]:


sns.relplot(x = "Confirmed", y = "Recovered", data=corona)


# In[88]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Confirmed", data=corona)


# In[89]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Deaths", data=corona)


# In[90]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Recovered", data=corona)


# In[91]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Confirmed", data=corona.head(30))


# In[97]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Deaths", data=corona.head(30))


# In[93]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Recovered", data=corona.head(30))


# In[94]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Confirmed", data=corona.tail(50))


# In[95]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Deaths", data=corona.tail(50))


# In[96]:


plt.figure(figsize=(15,8))
sns.barplot(y = "Province/State", x = "Recovered", data=corona.tail(30))


# In[ ]:




