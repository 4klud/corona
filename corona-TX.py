#!/usr/bin/env python
# coding: utf-8

# ### Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings('ignore')


# ### Load data

# In[2]:


coronaTX = pd.read_csv("texas-history.csv")
coronaTX.head(20)


# In[3]:


print(coronaTX.columns)


# ### Visualization

# In[11]:


data = coronaTX[['date', 'death', 'hospitalizedCurrently', 'onVentilatorCurrently']]
area_data = pd.DataFrame(columns=['date', 'metric', 'cases'])
for i, r in data.iterrows():
    for m in ['death', 'hospitalizedCurrently', 'onVentilatorCurrently']:
        area_data = area_data.append(
            {'date': r['date'], 'Metric': m, 'Cases': r[m]},
            ignore_index=True)

    
fig = px.area(area_data, x="date", y="Cases", color="Metric",
	      line_group="Metric"
)
fig.show()

