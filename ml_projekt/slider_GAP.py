#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px
from datetime import date
from datetime import datetime
from dateutil import parser
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error
import pickle
from prophet.serialize import model_to_json, model_from_json
from prophet import Prophet
from prophet.plot import add_changepoints_to_plot
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
from prophet.plot import plot_plotly, plot_cross_validation_metric, plot_components_plotly, add_changepoints_to_plot, plot_yearly
from prophet.serialize import model_to_json, model_from_json

import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller


# In[2]:


#!wget https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip
#!unzip household_power_consumption.zip


# In[3]:


pd.set_option("display.float_format", "{:.2f}".format)


# In[4]:


# The ds (datestamp) column should be of a format expected by Pandas,
# ideally YYYY-MM-DD for a date or YYYY-MM-DD HH:MM:SS for a timestamp.


# In[5]:


df = pd.read_csv("household_power_consumption.txt", sep=";", parse_dates={'ds':['Date', 'Time']}, na_values=['nan', '?'], infer_datetime_format=True, low_memory=False)
del df['Sub_metering_1']
del df['Sub_metering_2']
del df['Sub_metering_3']
del df['Global_reactive_power']
del df['Voltage']
del df['Global_intensity']

df


# In[6]:


df.info()


# In[7]:


df


# In[8]:


df.head(15)


# In[9]:


df.isna().sum()


# In[10]:


df.describe(include='all').T


# In[11]:


df = df.fillna(df.shift(60*24*7))


# In[12]:


df.isna().sum()


# In[13]:


df = df.fillna(df.shift(60*24*7))


# In[14]:


df.isna().sum()


# In[15]:


df = df.fillna(df.shift(60*24))


# In[16]:


df.isna().sum()


# In[17]:


df.describe(include='all').T


# In[19]:


df["Global_active_power"] = df["Global_active_power"].apply(lambda x: x/60)


# In[20]:


df_H = df.resample('H', on="ds").mean()
df_H= df_H.reset_index(drop=False)
df_H.head()


# In[ ]:





# In[ ]:





# In[ ]:





# ## Global active power - slider

# In[25]:


fig = px.line(df, x='ds', y = 'Global_active_power', title = 'Energy Use: Global active power')

fig.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count=1, label = "day", step = "day", stepmode = "backward"),
            dict(count=7, label="week", step="day", stepmode="backward"),
            dict(count=1, label="month", step="month", stepmode="backward"),
            dict(count=12, label="year", step="month", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




