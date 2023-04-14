#!/usr/bin/env python
# coding: utf-8

# # Climate catastrophe
# 
# ## Data analysis on changes in average temperatures
# 
# Project analyzing data on changes in average temperatures. The `csv` file containing the raw data can be found at [kaggle.com](https://www.kaggle.com/datasets/sevgisarac/temperature-change)

# ### Import

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### DataFrame

# In[ ]:


# Default value
pd.set_option("display.width", 80)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[ ]:


# Default DataFrame
df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="Windows-1250") #index_col=False

#df.head(1)


# In[ ]:


df.shape


# In[ ]:


# Columns name rename, where \s (inside names) into _
df = df.rename(columns={"Area Code": "Area_Code",
                        "Months Code": "Months_Code",
                        "Element Code": "Element_Code"})


# In[ ]:


# Replacing comas in string
df['Area'] = df['Area'].str.replace(',','')

# Replacing quote in string
df['Area'] = df['Area'].str.replace('\"','')


# In[ ]:


# Optional 1 !!! (Jaro is using this in his part o code)
# Adding continent name & continent number columns. To have those columns added to default dataframe.
# 1. Reading and creating additional frame, for join puprose (from '_Countries_Continents.csv' file)
# 2. Inner join default dataframe with two new columns (continents for each country)
# (every rows containing country name will stay in df)
# (every rows containing geo-region name will not stay in df)

def optional_1(df):
    continent = pd.read_csv("_Countries_Continents.csv", names=['Area', 'Contintnt', 'Contintnt_Code'], encoding="UTF-8")
    continent = continent.rename(columns={'Contintnt':'Continent',
                                          'Contintnt_Code': 'Continent_Code'})
    df = pd.merge(left=continent, right=df, on='Area', how='inner')
    return df


# In[ ]:


# Optional 2 !!! (Jaro is using this in his part o code)
# 1. Remove each row that contain 'Standard Deviation' value in column 'Element_Code' (code: 7271)
# 2. For loop that will iterate each row (separately), searching NaN values in last 59 columns (year columns).
# After each iteration every NaN will be updated to row mean value (from 59 year columns for each row separately)
# new df is returned but it must be override, like: "df_new = optional_2(df)"
# (of course this can be the same variable: "df = optional_2(df)" )

def optional_2(df):
    df = df.loc[(df['Element_Code'] == 7271) & (df['Area_Code'] < 5000)]
    for i in range(df.shape[0]-1):
        m = round(df.iloc[i,-59:].mean(),3)
        df.iloc[i,-59:] = df.iloc[i,-59:].fillna(m)
    return df


# #### JARO

# In[ ]:


# Displayng all rows in dataframe
# pd.set_option('display.max_rows', None)


# In[ ]:


# Using 'Optional 1'
jaro = optional_1(df)
jaro.shape


# In[ ]:


# Removing specific rows, leaving only those where:
# 1. 'Months_Code' is 'Meteorological year'
# 2. 'Element_Code' is 'Temperature change'
# 3. 'Area_Code' < 5000 means only countries (not regions name)
jaro = jaro.loc[(jaro['Months_Code'] == 7020) & (jaro['Element_Code'] == 7271) & (jaro['Area_Code'] < 5000)]
jaro.shape


# In[ ]:


# Using 'Optional 2'
jaro = optional_2(jaro)
jaro.shape


# In[ ]:


# If optional_1() and/or optional_2() isn't choosen then start from here:

# Making individual variable for group purpose working

#jaro = df.copy()


# In[ ]:


jaro.iloc[:,-59:].isna().sum()


# In[ ]:





# #### ANNA

# In[ ]:


# Making individual variable for group purpose working
anna = df.copy()
anna1 = optional_1(anna)
anna2 = anna1[(anna1.Continent== 'North America')]
anna3 = anna2[(anna2.Area == 'Greenland')
             |(anna2.Area == 'United States of America')
             |(anna2.Area == 'Cuba')
             |(anna2.Area == 'Haiti')
             |(anna2.Area == 'Dominican Republic')]
# In[ ]:
anna3.isnull().sum()
# In[ ]:
anna4 = anna[(anna.Area == 'Norther America')
             | (anna.Area == 'Central America')]
# In[]:
anna4.isnull().sum()
# In[ ]:







# #### MATTHIAS

# In[ ]:


# Making individual variable for group purpose working
mateo = df.copy()


# In[ ]:





# #### PAULINA

# In[ ]:


# Making individual variable for group purpose working
pauli = df.copy()


# In[ ]:





# #### URSULA

# In[ ]:


# Making individual variable for group purpose working
urs = df.copy()


# In[ ]:




