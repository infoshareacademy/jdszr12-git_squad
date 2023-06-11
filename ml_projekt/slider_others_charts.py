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
df.rename(columns={'Global_active_power':'y'}, inplace = True)
df


# In[6]:


df.info()


# In[7]:


df


# In[8]:


df.head(15)


# ### Other charts

# In[92]:


# Create new columns for year, quarter, month, and day
df['year'] = df['ds'].apply(lambda x: x.year)
df['quarter'] = df['ds'].apply(lambda x: x.quarter)
df['month'] = df['ds'].apply(lambda x: x.month)
df['day'] = df['ds'].apply(lambda x: x.day)
df = df.loc[:,['ds','y', 'year','quarter','month','day']]
df.tail(5)


# In[119]:


# Create a figure with 4 subplots
plt.figure(figsize=(30,18))

# Plot the first subplot showing the violinplot of yearly global active power
plt.subplot(2,2,1)
# Adjust the subplot's width
plt.subplots_adjust(wspace=0.2)
# Create the violinplot using Seaborn's violinplot function
sns.violinplot(x="year", y="y", data=df, color='blue')
# Label the x-axis
plt.xlabel('Year', fontsize=12)
# Add a title to the plot
plt.title('Violin plot of Yearly Global Active Power', fontsize=25)
# Remove the top and right spines of the plot
sns.despine(left=True, bottom=True)
# Add a tight layout to the plot
plt.tight_layout() 
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 20)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 20)

# Plot the second subplot showing the violinplot of quarterly global active power
plt.subplot(2,2,2)
# Create the violinplot using Seaborn's violinplot function
sns.violinplot(x="quarter", y="y", data=df, color='blue')
# Label the x-axis
plt.xlabel('Quarter', fontsize=12)
# Add a title to the plot
plt.title('Violin plot of Quarterly Global Active Power', fontsize=25)
# Remove the top and right spines of the plot
sns.despine(left=True, bottom=True)
# Add a tight layout to the plot
plt.tight_layout()
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 20)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 20)

# Plot the second subplot showing the violinplot of monthly global active power
plt.subplot(2,2,3)
# Create the violinplot using Seaborn's violinplot function
sns.violinplot(x="month", y="y", data=df, color='blue')
# Label the x-axis
plt.xlabel('Month', fontsize=12)
# Add a title to the plot
plt.title('Violin plot of Monthly Global Active Power', fontsize=25)
# Remove the top and right spines of the plot
sns.despine(left=True, bottom=True)
# Add a tight layout to the plot
plt.tight_layout()
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 20)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 20)

# Plot the second subplot showing the violinplot of dayly global active power
plt.subplot(2,2,4)
# Create the violinplot using Seaborn's violinplot function
sns.violinplot(x="day", y="y", data=df, color='blue')
# Label the x-axis
plt.xlabel('Day', fontsize=12)
# Add a title to the plot
plt.title('Violin plot of Dayly Global Active Power', fontsize=25)
# Remove the top and right spines of the plot
sns.despine(left=True, bottom=True)
# Add a tight layout to the plot
plt.tight_layout()

plt.tick_params(axis='x', labelcolor='#000000', labelsize = 20)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 20)


# In[ ]:





# In[ ]:





# ### Global active power - slider

# In[9]:


fig = px.line(df, x='ds', y = 'y', title = 'Energy Use: Global active power')

fig.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count=1, label = "1d", step = "day", stepmode = "backward"),
            dict(count=7, label="7d", step="day", stepmode="backward"),
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




