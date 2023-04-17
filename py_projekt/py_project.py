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
df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv",
                 encoding="Windows-1250")  # index_col=False

# df.head(1)


# In[ ]:


df.shape


# In[ ]:


# Columns name rename, where \s (inside names) into _
df = df.rename(columns={"Area Code": "Area_Code",
                        "Months Code": "Months_Code",
                        "Element Code": "Element_Code"})


# In[ ]:


# Replacing comas in string
df['Area'] = df['Area'].str.replace(',', '')

# Replacing quote in string
df['Area'] = df['Area'].str.replace('\"', '')


# In[ ]:


# Optional 1 !!! (Jaro is using this in his part o code)
# Adding continent name & continent number columns. To have those columns added to default dataframe.
# 1. Reading and creating additional frame, for join puprose (from '_Countries_Continents.csv' file)
# 2. Inner join default dataframe with two new columns (continents for each country)
# (every rows containing country name will stay in df)
# (every rows containing geo-region name will not stay in df)

def optional_1(df):
    continent = pd.read_csv("_Countries_Continents.csv", names=[
                            'Area', 'Continent', 'Continent_Code'], encoding="UTF-8")
    # continent = continent.rename(columns={'Contintnt':'Continent',
    #                                      'Contintnt_Code': 'Continent_Code'})
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
        m = round(df.iloc[i, -59:].mean(), 3)
        df.iloc[i, -59:] = df.iloc[i, -59:].fillna(m)
    return df


# #### JARO

# #### Displayng all rows in dataframe
# `pd.set_option('display.max_rows', None)`

# In[ ]:


jaro1 = df.copy()


# In[ ]:


jaro1.columns = jaro1.columns.str.replace('Y', '')


# #### Whole World temperatures (1961-2019)

# In[ ]:


world_t = jaro1.loc[(jaro1['Area_Code'] == 5000) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# world_t.iloc[:,-59:].isna().sum()
world_t_ok = world_t.iloc[:, -59:]


# #### Africa temperatures (1961-2019)

# In[ ]:


africa_t = jaro1.loc[(jaro1['Area_Code'] == 5100) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# africa_t.iloc[:,-59:].isna().sum()
africa_t_ok = africa_t.iloc[:, -59:]


# #### Caribbean, Northern & Central Americas temperatures (1961-2019)

# In[ ]:


north_america_t = jaro1.loc[((jaro1['Area_Code'] == 5203) | (jaro1['Area_Code'] == 5204) | (jaro1['Area_Code'] == 5206))
                            & (jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# north_america_t.iloc[:,-59:].isna().sum()
north_america_t_ok = north_america_t.iloc[:, -59:].mean()


# #### South America temperatures (1961-2019)

# In[ ]:


south_america_t = jaro1.loc[(jaro1['Area_Code'] == 5207) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# south_america_t.iloc[:,-59:].isna().sum()
south_america_t_ok = south_america_t.iloc[:, -59:]


# #### Asia temperatures (1961-2019)

# In[ ]:


asia_t = jaro1.loc[(jaro1['Area_Code'] == 5300) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# asia_t.iloc[:,-59:].isna().sum()
asia_t_ok = asia_t.iloc[:, -59:]


# #### Europe temperatures (1961-2019)

# In[ ]:


europe_t = jaro1.loc[(jaro1['Area_Code'] == 5400) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# europe_t.iloc[:,-59:].isna().sum()
europe_t_ok = europe_t.iloc[:, -59:]


# #### Oceania temperatures (1961-2019)

# In[ ]:


oceania_t = jaro1.loc[(jaro1['Area_Code'] == 5500) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
oceania_t_ok = oceania_t.iloc[:, -59:]


# #### Antarctica temperatures (1961-2019)

# In[ ]:


antarctica_t = jaro1.loc[(jaro1['Area_Code'] == 30) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
antarctica_t_ok = antarctica_t.iloc[:, -59:]

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = africa_t_ok.values.T

plt.plot(x, y1, label='World')
plt.plot(x, y2, label='Africa')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = north_america_t_ok.values.T

plt.plot(x, y1, label='World')
plt.plot(x, y2, label='North America')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = south_america_t_ok.values.T

plt.plot(x, y1, label='World')
plt.plot(x, y2, label='South America')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = asia_t_ok.values.T

plt.plot(x, y1, label='World')
plt.plot(x, y2, label='Asia')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = europe_t_ok.values.T

plt.plot(x, y1, label='World')
plt.plot(x, y2, label='Europe')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = oceania_t_ok.values.T

plt.plot(x, y1, label='World')
plt.plot(x, y2, label='Oceania')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = antarctica_t_ok.values.T

plt.plot(x, y1, label='World')
plt.plot(x, y2, label='Antarctica')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# Using 'Optional 1'

# In[ ]:


jaro = optional_1(df)
jaro.shape


# Removing specific rows, leaving only those where:<br>
# 1. 'Months_Code' is 'Meteorological year'<br>
# 2. 'Element_Code' is 'Temperature change'<br>
# 3. 'Area_Code' < 5000 means only countries (not regions name)

# In[ ]:


jaro = jaro.loc[(jaro['Months_Code'] == 7020) & (
    jaro['Element_Code'] == 7271) & (jaro['Area_Code'] < 5000)]
jaro.shape


# Using 'Optional 2'

# In[ ]:


jaro = optional_2(jaro)
jaro.shape


# #### If optional_1() and/or optional_2() isn't choosen then start from here:

# Making individual variable for group purpose working

# In[ ]:


jaro = df.copy()


# In[ ]:


jaro.iloc[:, -59:].isna().sum()


# #### ANNA

# In[ ]:


# Making individual variable for group purpose working

# DataFrame with 5 countries from America (Northern & Central)
anna = df.copy()
anna1 = optional_1(anna)
anna2 = anna1[(anna1.Continent == 'North America')]
anna3 = anna2[(anna2.Area == 'Greenland')
              | (anna2.Area == 'United States of America')
              | (anna2.Area == 'Cuba')
              | (anna2.Area == 'Haiti')
              | (anna2.Area == 'Dominican Republic')]
anna3 = anna3[(anna2.Months == 'Meteorological year')
              & (anna2.Element == 'Temperature change')]
anna3
# In[ ]:
anna3.isnull().sum()
# In[ ]:
# DataFrame with continents
anna4 = anna[(anna.Area == 'Northern America')
             | (anna.Area == 'Central America')]
anna4 = anna4[(anna.Months == 'Meteorological year')
              & (anna.Element == 'Temperature change')]
anna4

# In[]:
anna4.isnull().sum()
# In[ ]:

anna5 = pd.concat([anna4, anna3])
anna5
# Inp[]:
anna5.columns = anna5.columns.str.replace('Y', '')
del anna5['Area_Code']
del anna5['Months_Code']
del anna5['Months']
del anna5['Element']
del anna5['Unit']
del anna5['Element_Code']
del anna5['Continent']
del anna5['Continent_Code']
anna5

# In[]:
# Transformation table
anna6 = pd.melt(anna5, id_vars='Area')
anna6 = anna6.rename(columns={'variable': 'Year',
                              'value': 'Temp'})
anna6 = anna6.sort_values(by=['Area', 'Year'])
anna6

# In[]:
# DataFrame with Forests
forest = pd.read_csv('forest.csv')
forest = forest[(forest.country_name == 'Canada')
                | (forest.country_name == 'United States')
                | (forest.country_name == 'Cuba')
                | (forest.country_name == 'Haiti')
                | (forest.country_name == 'Dominican Republic')]

forest = forest.rename(columns={'year': 'Year',
                                'country_name': 'Area',
                                'value': 'Forest'})

del forest['country_code']
forest.isnull().sum()
forest

# In[]:
# DataFrame with CO2
co2 = pd.read_csv('co2.csv')
co2 = co2[(co2.country_name == 'Canada')
          | (co2.country_name == 'United States')
          | (co2.country_name == 'Cuba')
          | (co2.country_name == 'Haiti')
          | (co2.country_name == 'Dominican Republic')]

co2 = co2.rename(columns={'year': 'Year',
                          'country_name': 'Area',
                          'value': 'CO2'})

del co2['country_code']

co2.isnull().sum()

co2


# #### MATTHIAS

# In[ ]:


# Making individual variable for group purpose working
mateo = df.copy()

mateo1=optional_1(mateo)


# In[ ]:

# Creating individual Dataframe for countries in Asia

asia=mateo1[(mateo1.Continent_Code==2) & (mateo1.Months_Code==7020) & (mateo1.Element_Code==7271)]

# In[ ]:

# Droping unnecessary columns

asia=asia.drop(columns=['Continent',
                            'Continent_Code',
                             'Area_Code',
                             'Months_Code',
                             'Months',
                             'Element_Code',
                             'Element',
                             'Unit'])

# In[ ]:

# Repalcing unnecessary marks with space

asia.columns=asia.columns.str.replace('Y', '')
asia['Area'] = asia['Area'].str.replace("'" ,' ')


#In[ ]:

# Dataframe 5 Asia countries

asia_5=asia[(asia.Area=='Afghanistan') | (asia.Area=='Saudi Arabia') | (asia.Area=='India') |
             (asia.Area=='Republic of Korea') | (asia.Area=='China')]

# In[ ]:

asia_5.isnull().sum()

# IN[ ]:

# X axis from columns 

x=asia_5.columns[1:].T

# In[ ]:

# Y axis for countries

y1=asia_5.iloc[0,-59:].values.T # Afganistan
y2=asia_5.iloc[1,-59:].values.T #China
y3=asia_5.iloc[2,-59:].values.T #India                  
y4=asia_5.iloc[3,-59:].values.T #South Korea
y5=asia_5.iloc[4,-59:].values.T #Arabia

# In[ ]:

plt.plot(x, y1, label='Afganistan')
plt.plot(x, y2, label='Chiny')
plt.plot(x, y3, label='Indie')
plt.plot(x, y4, label='South Korea')   
plt.plot(x, y5, label='Arabia')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show();

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
