#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8


# # Climate catastrophe<br><br>
# <br><br>
# ## Data analysis on changes in average temperatures<br><br>
# <br><br>
# Project analyzing data on changes in average temperatures. The `csv` file containing the raw data can be found at [kaggle.com](https://www.kaggle.com/datasets/sevgisarac/temperature-change)

# ### Import

# In[ ]:

# In[25]:

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
from scipy.interpolate import splrep, splev


# ### DataFrame

# In[ ]:

# Default value

# In[26]:

# In[2]:


pd.set_option("display.width", 80)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[ ]:

# Default DataFrame

# In[27]:

# In[3]:


df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv",
                 encoding="Windows-1250")  # index_col=False


# df.head(1)

# In[ ]:

# In[7]:

# In[4]:


df.shape


# In[ ]:

# Columns name rename, where \s (inside names) into _

# In[28]:

# In[5]:


df = df.rename(columns={"Area Code": "Area_Code",
                        "Months Code": "Months_Code",
                        "Element Code": "Element_Code"})


# In[ ]:

# Replacing comas in string

# In[29]:

# In[6]:


df['Area'] = df['Area'].str.replace(',', '')


# Replacing quote in string

# In[10]:

# In[7]:


df['Area'] = df['Area'].str.replace('\"', '')


# In[ ]:

# Optional 1 !!! (Jaro is using this in his part o code)<br><br>
# Adding continent name & continent number columns. To have those columns added to default dataframe.<br><br>
# 1. Reading and creating additional frame, for join puprose (from '_Countries_Continents.csv' file)<br><br>
# 2. Inner join default dataframe with two new columns (continents for each country)<br><br>
# (every rows containing country name will stay in df)<br><br>
# (every rows containing geo-region name will not stay in df)

# In[30]:

# In[8]:


def optional_1(df):
    continent = pd.read_csv("_Countries_Continents.csv", names=[
                            'Area', 'Continent', 'Continent_Code'], encoding="UTF-8")
   
    df = pd.merge(left=continent, right=df, on='Area', how='inner')
    return df


# In[ ]:

# Optional 2 !!! (Jaro is using this in his part o code)<br><br>
# 1. Remove each row that contain 'Standard Deviation' value in column 'Element_Code' (code: 7271)<br><br>
# 2. For loop that will iterate each row (separately), searching NaN values in last 59 columns (year columns).<br><br>
# After each iteration every NaN will be updated to row mean value (from 59 year columns for each row separately)<br><br>
# new df is returned but it must be override, like: "df_new = optional_2(df)"<br><br>
# (of course this can be the same variable: "df = optional_2(df)" )

# In[31]:

# In[9]:


def optional_2(df):
    df = df.loc[(df['Element_Code'] == 7271) & (df['Area_Code'] < 5000)]
    for i in range(df.shape[0]-1):
        m = round(df.iloc[i, -59:].mean(), 3)
        df.iloc[i, -59:] = df.iloc[i, -59:].fillna(m)
    return df


# #### JARO

# #### Displayng all rows in dataframe<br><br>
# `pd.set_option('display.max_rows', None)`

# In[ ]:

# In[13]:

# In[ ]:


jaro1 = df.copy()


# In[ ]:

# In[14]:

# In[ ]:


jaro1.columns = jaro1.columns.str.replace('Y', '')


# #### Whole World temperatures (1961-2019)

# In[ ]:

# In[15]:

# In[ ]:


world_t = jaro1.loc[(jaro1['Area_Code'] == 5000) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# world_t.iloc[:,-59:].isna().sum()
world_t_ok = world_t.iloc[:, -59:]


# #### Africa temperatures (1961-2019)

# #### Africa temperatures (1961-2019)

# In[ ]:

# In[16]:

# In[ ]:


africa_t = jaro1.loc[(jaro1['Area_Code'] == 5100) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# africa_t.iloc[:,-59:].isna().sum()
africa_t_ok = africa_t.iloc[:, -59:]


# #### Caribbean, Northern & Central Americas temperatures (1961-2019)

# In[ ]:

# In[17]:

# In[ ]:


north_america_t = jaro1.loc[((jaro1['Area_Code'] == 5203) | (jaro1['Area_Code'] == 5204) | (jaro1['Area_Code'] == 5206))
                            & (jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# north_america_t.iloc[:,-59:].isna().sum()
north_america_t_ok = north_america_t.iloc[:, -59:].mean()


# #### South America temperatures (1961-2019)

# In[ ]:

# In[15]:

# In[ ]:


south_america_t = jaro1.loc[(jaro1['Area_Code'] == 5207) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# south_america_t.iloc[:,-59:].isna().sum()
south_america_t_ok = south_america_t.iloc[:, -59:]


# #### Asia temperatures (1961-2019)

# In[ ]:

# In[16]:

# In[ ]:


asia_t = jaro1.loc[(jaro1['Area_Code'] == 5300) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# asia_t.iloc[:,-59:].isna().sum()
asia_t_ok = asia_t.iloc[:, -59:]


# #### Europe temperatures (1961-2019)

# In[ ]:

# In[17]:

# In[ ]:


europe_t = jaro1.loc[(jaro1['Area_Code'] == 5400) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# europe_t.iloc[:,-59:].isna().sum()
europe_t_ok = europe_t.iloc[:, -59:]


# #### Oceania temperatures (1961-2019)

# In[ ]:

# In[18]:

# In[ ]:


oceania_t = jaro1.loc[(jaro1['Area_Code'] == 5500) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
oceania_t_ok = oceania_t.iloc[:, -59:]


# #### Antarctica temperatures (1961-2019)

# In[ ]:

# In[19]:

# In[ ]:


antarctica_t = jaro1.loc[(jaro1['Area_Code'] == 30) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
antarctica_t_ok = antarctica_t.iloc[:, -59:]


# In[ ]:

# In[20]:

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = africa_t_ok.values.T


# In[21]:

# In[ ]:


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

# In[22]:

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = north_america_t_ok.values.T


# In[23]:

# In[ ]:


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

# In[24]:

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = south_america_t_ok.values.T


# In[25]:

# In[ ]:


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

# In[26]:

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = asia_t_ok.values.T


# In[27]:

# In[ ]:


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

# In[28]:

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = europe_t_ok.values.T


# In[29]:

# In[ ]:


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

# In[30]:

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = oceania_t_ok.values.T


# In[31]:

# In[ ]:


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

# In[32]:

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = antarctica_t_ok.values.T


# In[33]:

# In[ ]:


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

# In[34]:

# In[ ]:


jaro = optional_1(df)
jaro.columns = jaro.columns.str.replace('Y', '')
jaro.shape


# Removing specific rows, leaving only those where:<br><br><br>
# 1. 'Months_Code' is 'Meteorological year'<br><br><br>
# 2. 'Element_Code' is 'Temperature change'<br><br><br>
# 3. 'Area_Code' < 5000 means only countries (not regions name)

# In[ ]:

# In[35]:

# In[ ]:


jaro = jaro.loc[(jaro['Months_Code'] == 7020) & (
    jaro['Element_Code'] == 7271) & (jaro['Area_Code'] < 5000)]
jaro.shape


# Using 'Optional 2'

# In[ ]:

# In[36]:

# In[ ]:


jaro = optional_2(jaro)
jaro.shape


# #### If optional_1() and/or optional_2() isn't choosen then start from here:

# Making individual variable for group purpose working

# In[ ]:

# In[37]:

# In[ ]:


jaro = df.copy()


# In[38]:

# In[ ]:


antarctica_t = jaro1.loc[(jaro1['Area_Code'] == 30) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
antarctica_t_ok = antarctica_t.iloc[:, -59:]


# In[ ]:

# In[39]:

# In[ ]:


jaro.iloc[:, -59:].isna().sum()


# #### NORTHERN & CENTRAL AMERICA

# In[ ]:

# Making individual variable for group purpose working

# DataFrame with 5 countries from America (Northern & Central

# In[40]:

# In[ ]:


NAmerica = df.copy()
NAmerica = optional_1(NAmerica)
NAmerica_full= NAmerica [(NAmerica.Continent == 'North America')]
NAmerica_c3 = NAmerica_full[(NAmerica_full.Area == 'Canada')
              | (NAmerica_full.Area == 'United States of America')
                | (NAmerica_full.Area == 'Dominican Republic')]
NAmerica_c3 = NAmerica_c3[(NAmerica_c3.Months == 'Meteorological year')
              & (NAmerica_c3.Element == 'Temperature change')]
NAmerica_c3


# Inp[]:<br><br>
# reparing data

# In[41]:

# In[ ]:


NAmerica_c3.columns = NAmerica_c3.columns.str.replace('Y', '')
del NAmerica_c3['Area_Code']
del NAmerica_c3['Months_Code']
del NAmerica_c3['Months']
del NAmerica_c3['Element']
del NAmerica_c3['Unit']
del NAmerica_c3['Element_Code']
del NAmerica_c3['Continent']
del NAmerica_c3['Continent_Code']
NAmerica_c3


# In[]:<br><br>
# Transformation table

# In[42]:

# In[ ]:


NAmerica_trans = pd.melt(NAmerica_c3, id_vars='Area')
NAmerica_trans = NAmerica_trans.rename(columns={'variable': 'Year',
                              'value': 'Temp'})
NAmerica_trans = NAmerica_trans.sort_values(by=['Area', 'Year'])
NAmerica_trans.Year = pd.to_numeric(NAmerica_trans.Year)
NAmerica_trans.info()


# In[]:<br><br>
# DataFrame with Forests

# In[43]:

# In[ ]:


NAmerica_forest = pd.read_csv('forest.csv')
NAmerica_forest = NAmerica_forest[(NAmerica_forest.country_name == 'Canada')
                | (NAmerica_forest.country_name == 'United States')
                | (NAmerica_forest.country_name == 'Dominican Republic')]


# In[44]:

# In[ ]:


NAmerica_forest = NAmerica_forest.rename(columns={'year': 'Year',
                                'country_name': 'Area',
                                'value': 'Forest'})


# In[45]:

# In[ ]:


NAmerica_forest.replace(to_replace="United States",
           value="United States of America", inplace=True)


# In[46]:

# In[ ]:


del NAmerica_forest['country_code']
NAmerica_forest.Year = pd.to_numeric(NAmerica_forest.Year)
NAmerica_forest.isnull().sum()
NAmerica_forest


# In[]:<br><br>
# DataFrame with CO2

# In[47]:

# In[ ]:


NAmerica_co2 = pd.read_csv('co2.csv')
NAmerica_co2 = NAmerica_co2[(NAmerica_co2.country_name == 'Canada')
          | (NAmerica_co2.country_name == 'United States')
          | (NAmerica_co2.country_name == 'Dominican Republic')]


# In[48]:

# In[ ]:


NAmerica_co2 = NAmerica_co2.rename(columns={'year': 'Year',
                          'country_name': 'Area',
                          'value': 'CO2'})


# In[49]:

# In[ ]:


NAmerica_co2.replace(to_replace="United States",
           value="United States of America", inplace=True)


# In[50]:

# In[ ]:


del NAmerica_co2['country_code']


# In[51]:

# In[ ]:


NAmerica_co2.isnull().sum()


# In[52]:

# In[ ]:


NAmerica_co2.info()


# In[]:<br><br>
# DataFrame with GDP

# In[53]:

# In[ ]:


NAmerica_gdp = pd.read_csv('GDP_percapita.csv')


# In[54]:

# In[ ]:


NAmerica_gdp = NAmerica_gdp.rename(columns={'Country Name':'Area'})


# In[55]:

# In[ ]:


NAmerica_gdp = NAmerica_gdp[(NAmerica_gdp.Area == 'Canada')
          | (NAmerica_gdp.Area == 'United States')
          | (NAmerica_gdp.Area == 'Dominican Republic')]


# In[56]:

# In[ ]:


NAmerica_gdp.replace(to_replace="United States",
           value="United States of America", inplace=True)
del NAmerica_gdp['Code']
del NAmerica_gdp['Unnamed: 65']


# In[57]:

# In[ ]:


NAmerica_gdp


# In[]:<br><br>
# Transform GDP

# In[58]:

# In[ ]:


NAmerica_gdp_trans = pd.melt(NAmerica_gdp, id_vars='Area')
NAmerica_gdp_trans = NAmerica_gdp_trans.rename(columns={'variable': 'Year',
                              'value': 'GDP_per_capita'})
NAmerica_gdp_trans = NAmerica_gdp_trans.sort_values(by=['Area', 'Year'])
NAmerica_gdp_trans.Year = pd.to_numeric(NAmerica_gdp_trans.Year)


# In[59]:

# In[ ]:


NAmerica_gdp_trans


# In[]:<br><br>
# Join  temperature, forest, co2 and GDP

# In[60]:

# In[ ]:


NAmerica_tf = pd.merge(NAmerica_trans, NAmerica_forest, on =['Area','Year'], how = 'left')
NAmerica_tfc = pd.merge(NAmerica_tf, NAmerica_co2, on=['Area', 'Year'], how = 'left')
NAmerica_tfcg = pd.merge(NAmerica_tfc, NAmerica_gdp_trans, on=['Area', 'Year'], how = 'left')
NAmerica_tfcg 


# In[]:<br><br>
#  Temperature

# In[61]:

# In[ ]:


tfc_Canada = NAmerica_tfcg [(NAmerica_tfcg.Area == 'Canada')]
tfc_US = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
tfc_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.Temp, label = 'Kanada', color = '#00035b')
plt.plot(tfc_US.Year, tfc_US.Temp, label = 'Stany Zjednoczone', color = '#0343df')
plt.plot(tfc_Dominican.Year, tfc_Dominican.Temp, label = 'Dominikana', color = '#a2cffe')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103')
plt.title('Zmiany temperatur (1961-2019)')
plt.legend()
plt.show()


# In[]:<br><br>
#  Forest

# In[62]:

# In[ ]:


tfc_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
tfc_US = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
tfc_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.Forest, label = 'Kanada', color = '#00035b')
plt.plot(tfc_US.Year, tfc_US.Forest, label = 'Stany Zjednoczone', color = '#0343df')
plt.plot(tfc_Dominican.Year, tfc_Dominican.Forest, label = 'Dominikana', color = '#a2cffe')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Poziom zalesienia')
plt.title('Zalesienie (1990-2019)')
plt.legend()
plt.show()


# In[]:<br><br>
#  CO2

# In[63]:

# In[ ]:


tfc_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
tfc_US = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
tfc_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.CO2, label = 'Kanada', color = '#00035b')
plt.plot(tfc_US.Year, tfc_US.CO2, label = 'Stany Zjednoczone', color = '#0343df')
plt.plot(tfc_Dominican.Year, tfc_Dominican.CO2, label = 'Dominikana', color = '#a2cffe')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Emisja CO^2')
plt.title('Emisja CO^2 (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
# anada: temp vs CO2

# In[ ]:


fig, ax1 = plt.subplots()


# In[ ]:


ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#00035b')
ax1.plot(tfc_Canada.Year, tfc_Canada.Temp, label = 'Kanada', color = '#00035b')
ax1.tick_params(axis='y', labelcolor='#00035b')


# In[ ]:


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# In[ ]:


ax2.set_ylabel('CO^2', color='black')  # we already handled the x-label with ax1
ax2.plot(tfc_Canada.Year, tfc_Canada.CO2, label = 'Kanada', color = 'black')
ax2.tick_params(axis='y', labelcolor='black')


# In[ ]:


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Kanada: zmiany temperatury vs emisja CO^2 (1961-2019)')


# In[ ]:


plt.show()


# In[]:<br>
# SA: temp vs CO2

# In[ ]:


fig, ax1 = plt.subplots()


# In[ ]:


ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#0343df')
ax1.plot(tfc_US.Year, tfc_US.Temp, label = 'USA', color = '#0343df')
ax1.tick_params(axis='y', labelcolor='#0343df')


# In[ ]:


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# In[ ]:


ax2.set_ylabel('CO^2', color='black')  # we already handled the x-label with ax1
ax2.plot(tfc_US.Year, tfc_US.CO2, label = 'USA', color = 'black')
ax2.tick_params(axis='y', labelcolor='black')


# In[ ]:


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('USA: zmiany temperatury vs emisja CO^2 (1961-2019)')


# In[ ]:


plt.show()


# In[]:<br>
# ominikana: temp vs CO2

# In[ ]:


fig, ax1 = plt.subplots()


# In[ ]:


ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#a2cffe')
ax1.plot(tfc_Dominican.Year, tfc_Dominican.Temp, label = 'Dominikana', color = '#a2cffe')
ax1.tick_params(axis='y', labelcolor='#a2cffe')


# In[ ]:


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# In[ ]:


ax2.set_ylabel('CO^2', color='black')  # we already handled the x-label with ax1
ax2.plot(tfc_Dominican.Year, tfc_Dominican.CO2, label = 'Dominikana', color = 'black')
ax2.tick_params(axis='y', labelcolor='black')


# In[ ]:


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Dominikana: zmiany temperatury vs emisja CO^2 (1961-2019)')


# In[ ]:


plt.show()


# n[]:<br><br>
# Correlation_Canada

# In[64]:

# In[ ]:


corr_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
del corr_Canada['Area']
del corr_Canada['Year']


# In[65]:

# In[ ]:


corr_Canada= corr_Canada.corr()
sns.heatmap(corr_Canada, annot=True)
plt.show()


# n[]:<br><br>
# Correlation_USA

# In[66]:

# In[ ]:


corr_USA = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
del corr_USA['Area']
del corr_USA['Year']


# In[67]:

# In[ ]:


corr_USA= corr_USA.corr()
sns.heatmap(corr_USA, annot=True)
plt.show()


# n[]:<br><br>
# Correlation_Dominican

# In[68]:

# In[ ]:


corr_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
del corr_Dominican['Area']
del corr_Dominican['Year']


# In[69]:

# In[ ]:


corr_Dominican= corr_Dominican.corr()
sns.heatmap(corr_Dominican, annot=True)
plt.show()


# #### AFRICA<br><br>
# In[ ]:

# Making individual variable for group purpose working

# DataFrame with 3 countries from Africa

# In[70]:

# In[ ]:


africa = df.copy()
africa_t = optional_1(africa)
africa_t_full= africa_t [(africa_t.Continent == 'Africa')]
africa_t_c3 = africa_t_full[(africa_t_full.Area == 'Algeria')
                | (africa_t_full.Area == 'United Republic of Tanzania')
                | (africa_t_full.Area == 'Mozambique')]
africa_t_c3 = africa_t_c3[(africa_t_c3.Months == 'Meteorological year')
              & (africa_t_c3.Element == 'Temperature change')]
africa_t_c3


# Inp[]:<br><br>
# reparing data

# In[71]:

# In[ ]:


africa_t_c3.columns = africa_t_c3.columns.str.replace('Y', '')
africa_t_c3.replace(to_replace="United Republic of Tanzania",
           value="Tanzania", inplace=True)
del africa_t_c3['Area_Code']
del africa_t_c3['Months_Code']
del africa_t_c3['Months']
del africa_t_c3['Element']
del africa_t_c3['Unit']
del africa_t_c3['Element_Code']
del africa_t_c3['Continent']
del africa_t_c3['Continent_Code']
africa_t_c3


# In[]:<br><br>
# Transformation table

# In[72]:

# In[ ]:


africa_t_c3_trans = pd.melt(africa_t_c3, id_vars='Area')
africa_t_c3_trans = africa_t_c3_trans.rename(columns={'variable': 'Year',
                              'value': 'Temp'})
africa_t_c3_trans = africa_t_c3_trans.sort_values(by=['Area', 'Year'])
africa_t_c3_trans.Year = pd.to_numeric(africa_t_c3_trans.Year)
africa_t_c3_trans.info()


# In[]:<br><br>
# DataFrame with Forests

# In[73]:

# In[ ]:


africa_forest = pd.read_csv('forest.csv')
africa_forest = africa_forest[(africa_forest.country_name == 'Algeria')
                | (africa_forest.country_name == 'Tanzania')
            
                | (africa_forest.country_name == 'Mozambique')]


# In[74]:

# In[ ]:


africa_forest = africa_forest.rename(columns={'year': 'Year',
                                'country_name': 'Area',
                                'value': 'Forest'})


# In[75]:

# In[ ]:


del africa_forest['country_code']
africa_forest.Year = pd.to_numeric(africa_forest.Year)
africa_forest.isnull().sum()
africa_forest.info()


# In[]:<br><br>
# DataFrame with CO2

# In[76]:

# In[ ]:


africa_co2 = pd.read_csv('co2.csv')
africa_co2 = africa_co2[(africa_co2.country_name == 'Algeria')
          | (africa_co2.country_name == 'Tanzania')
          | (africa_co2.country_name == 'Mozambique')]


# In[77]:

# In[ ]:


africa_co2 = africa_co2.rename(columns={'year': 'Year',
                          'country_name': 'Area',
                          'value': 'CO2'})


# In[78]:

# In[ ]:


del africa_co2['country_code']


# In[79]:

# In[ ]:


africa_co2.isnull().sum()
africa_co2.info()


# In[]:<br><br>
# DataFrame with GDP

# In[80]:

# In[ ]:


africa_gdp = pd.read_csv('GDP_percapita.csv')


# In[81]:

# In[ ]:


africa_gdp = africa_gdp.rename(columns={'Country Name':'Area'})


# In[82]:

# In[ ]:


africa_gdp = africa_gdp[(africa_gdp.Area == 'Algeria')
          | (africa_gdp.Area == 'Tanzania')
          | (africa_gdp.Area == 'Mozambique')]


# In[83]:

# In[ ]:


del africa_gdp['Code']
del africa_gdp['Unnamed: 65']


# In[84]:

# In[ ]:


africa_gdp


# In[]:<br><br>
# Transform GDP

# In[85]:

# In[ ]:


africa_gdp_trans = pd.melt(africa_gdp, id_vars='Area')
africa_gdp_trans = africa_gdp_trans.rename(columns={'variable': 'Year',
                              'value': 'GDP_per_capita'})
africa_gdp_trans = africa_gdp_trans.sort_values(by=['Area', 'Year'])
africa_gdp_trans.Year = pd.to_numeric(africa_gdp_trans.Year)


# In[86]:

# In[ ]:


africa_gdp_trans.Area.unique()


# In[]:<br><br>
# Join  temperature, forest & co2

# In[87]:

# In[ ]:


africa_tf = pd.merge(africa_t_c3_trans, africa_forest, on =['Area','Year'], how = 'left')
africa_tfc = pd.merge(africa_tf, africa_co2, on=['Area', 'Year'], how = 'left')
africa_tfcg = pd.merge(africa_tfc, africa_gdp_trans, on =['Area', 'Year'], how = 'left')
africa_tfcg


# In[]:<br><br>
#  Temperature

# In[88]:

# In[ ]:


tfcg_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
tfcg_Tanzania = africa_tfcg[(africa_tfcg.Area == 'Tanzania')]
tfcg_Mozambique = africa_tfcg[(africa_tfcg.Area == 'Mozambique')]
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp, label = 'Algieria', color = '#000000')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp, label = 'Tanzania', color='#929591')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp, label = 'Mozambik', color = '#d8dcd6')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103')
plt.title('Zmiany temperatur (1961-2019)')
plt.legend()
plt.show()


# In[]:<br><br>
#  ALGERIA: Temperature vs GDP

# In[89]:

# In[ ]:


tfcg_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp, label = 'Algieria_temp')
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.GDP_per_capita, label = 'Algieria_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('AGLIERIA: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()


# In[]:<br><br>
#  Tanzania: Temperature vs GDP

# In[90]:

# In[ ]:


tfcg_Tanzania = africa_tfcg[(africa_tfcg.Area == 'Tanzania')]
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp, label = 'Tanzania_temp')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.GDP_per_capita, label = 'Tanzania_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('TANZANIA: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()


# In[]:<br><br>
#  Mozambique: Temperature vs GDP

# In[91]:

# In[ ]:


tfcg_Mozambique = africa_tfcg[(africa_tfcg.Area == 'Mozambique')]
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp, label = 'Mozambik_temp')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.GDP_per_capita, label = 'Mozambik_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('MOZAMBIK: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()


# In[]:<br><br>
#  Forest

# In[92]:

# In[ ]:


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Forest, label = 'Algieria', color = '#000000')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Forest, label = 'Tanzania', color='#929591')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Forest, label = 'Mozambik', color = '#d8dcd6')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Poziom zalesienia')
plt.title('Zalesienie (1990-2019)')
plt.legend()
plt.show()


# In[]:<br><br>
#  CO2

# In[93]:

# In[ ]:


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.CO2, label = 'Algieria', color = '#000000')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.CO2, label = 'Tanzania', color='#929591')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.CO2, label = 'Mozambik', color = '#d8dcd6')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Emisja CO^2')
plt.title('Emisja CO^2 (1961-2019)')
plt.legend()
plt.show()


# In[]:<br><br>
#  GDP

# In[94]:

# In[ ]:


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.GDP_per_capita, label = 'Algieria', color = '#000000')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.GDP_per_capita, label = 'Tanzania', color='#929591')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.GDP_per_capita, label = 'Mozambik', color = '#d8dcd6')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('GDP per capita (zmiana)')
plt.title('GDP per capita(1961-2019)')
plt.legend()
plt.show()


# n[]:<br>
# lgeria: temp vs CO2

# In[ ]:


fig, ax1 = plt.subplots()


# In[ ]:


ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#000000')
ax1.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp, label = 'Algeria', color = '#000000')
ax1.tick_params(axis='y', labelcolor='#000000')


# In[ ]:


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# In[ ]:


ax2.set_ylabel('CO^2', color='red')  # we already handled the x-label with ax1
ax2.plot(tfcg_Algeria.Year, tfcg_Algeria.CO2, label = 'Algeria', color = 'red')
ax2.tick_params(axis='y', labelcolor='red')


# In[ ]:


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Algeria: zmiany temperatury vs emisja CO^2 (1961-2019)')


# In[ ]:


plt.show()


# n[]:<br>
# anzania: temp vs CO2

# In[ ]:


fig, ax1 = plt.subplots()


# In[ ]:


ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#929591')
ax1.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp, label = 'Tanzania', color ='#929591')
ax1.tick_params(axis='y', labelcolor='#929591')


# In[ ]:


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# In[ ]:


ax2.set_ylabel('CO^2', color='red')  # we already handled the x-label with ax1
ax2.plot(tfcg_Tanzania.Year, tfcg_Tanzania.CO2, label = 'Tanzania', color = 'red')
ax2.tick_params(axis='y', labelcolor='red')


# In[ ]:


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Tanzania: zmiany temperatury vs emisja CO^2 (1961-2019)')


# In[ ]:


plt.show()


# n[]:<br>
# ozambik: temp vs CO2

# In[ ]:


fig, ax1 = plt.subplots()


# In[ ]:


ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#d8dcd6')
ax1.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp, label = 'Mozambik', color ='#d8dcd6')
ax1.tick_params(axis='y', labelcolor='#d8dcd6')


# In[ ]:


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# In[ ]:


ax2.set_ylabel('CO^2', color='red')  # we already handled the x-label with ax1
ax2.plot(tfcg_Mozambique.Year, tfcg_Mozambique.CO2, label = 'Mozambik', color = 'red')
ax2.tick_params(axis='y', labelcolor='red')


# In[ ]:


fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Mozambik: zmiany temperatury vs emisja CO^2 (1961-2019)')


# In[ ]:


plt.show()


# n[]:<br><br>
# Correlation_Algeria

# In[95]:

# In[ ]:


corr_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
del corr_Algeria['Area']
del corr_Algeria['Year']


# In[96]:

# In[ ]:


corr_Algeria = corr_Algeria.corr()
sns.heatmap(corr_Algeria, annot=True)
plt.show()


# n[]:<br><br>
# Correlation_Tanzania

# In[97]:

# In[ ]:


corr_Tanzania = africa_tfcg[(africa_tfcg.Area == 'Tanzania')]
del corr_Tanzania['Area']
del corr_Tanzania['Year']


# In[98]:

# In[ ]:


corr_Tanzania = corr_Tanzania.corr()
sns.heatmap(corr_Tanzania, annot=True)
plt.show()


# n[]:<br><br>
# Correlation_Mozambique

# In[99]:

# In[ ]:


corr_Mozambique = africa_tfcg[(africa_tfcg.Area == 'Mozambique')]
del corr_Mozambique['Area']
del corr_Mozambique['Year']


# In[100]:

# In[ ]:


corr_Mozambique = corr_Mozambique.corr()
sns.heatmap(corr_Mozambique, annot=True)
plt.show()


# #### MATTHIAS

# In[ ]:

# Making individual variable for group purpose working

# In[101]:

# In[78]:


mateo = df.copy()


# DataFrame with 5 countries from America (Northern & Central)

# In[102]:

# In[79]:


mateo1=optional_1(mateo)


# In[ ]:

# Creating individual Dataframe for countries in Asia

# In[103]:

# In[80]:


asia=mateo1[(mateo1.Continent_Code==2) & (mateo1.Months_Code==7020) & (mateo1.Element_Code==7271)]


# In[ ]:

# In[104]:

# In[81]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = europe_t_ok.values.T


# In[105]:

# In[82]:


plt.plot(x, y1, label='World')
plt.plot(x, y2, label='Europe')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# Droping unnecessary columns

# In[106]:

# In[83]:


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

# In[107]:

# In[84]:


asia.columns=asia.columns.str.replace('Y', '')
asia['Area'] = asia['Area'].str.replace("'" ,' ')


# In[ ]:

# Dataframe 3 Asia countries

# In[108]:

# In[85]:


asia_3=asia[(asia.Area=='India') | (asia.Area=='Republic of Korea') | (asia.Area=='China')]


# In[ ]:

# In[109]:

# In[86]:


asia_3.isnull().sum()


# In[ ]:

# Transform teble 

# In[110]:

# In[87]:


asia_3_tmp = pd.melt(asia_3, id_vars='Area')


# In[ ]:

# Renameing columns

# In[111]:

# In[88]:


asia_3_tmp=asia_3_tmp.rename(columns= {'variable' : 'Year',
                                       'value' : 'Temp' })


# In[ ]:

# In[89]:


asia_3_tmp = asia_3_tmp.sort_values(by= ['Area','Year'])


# Making x variables

# In[ ]:


In[112]:


# In[90]:


x_mat=asia_3_tmp.Year.unique()


# Converting object in to int64

# In[ ]:


In[]:


# In[91]:


x_mat=x_mat.astype(np.int64)


# Making y variables for 3 Asia countries

# In[ ]:


In[]:


# In[92]:


y1_tmp=asia_3_tmp[asia_3_tmp.Area=='China'].iloc[:,2].values.T
y2_tmp=asia_3_tmp[asia_3_tmp.Area=='India'].iloc[:,2].values.T
y3_tmp=asia_3_tmp[asia_3_tmp.Area=='Republic of Korea'].iloc[:,2].values.T


# Preparing plots for smoothing

# In[ ]:


In[]:


# In[93]:


bspl1 = splrep(x_mat,y1_tmp,s=4)   
bspl_y1 = splev(x_mat,bspl1) 


# In[94]:


bspl2 = splrep(x_mat,y2_tmp,s=4)   
bspl_y2 = splev(x_mat,bspl2) 


# In[95]:


bspl3 = splrep(x_mat,y3_tmp,s=12)   
bspl_y3 = splev(x_mat,bspl3)


# In[96]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x_mat, bspl_y1, label='Chiny')
plt.plot(x_mat, bspl_y2, label='Indie')
plt.plot(x_mat, bspl_y3, label='South Korea')


# In[97]:


plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show();


# #### South America

# In[ ]:

# Making individual variable for group purpose working

# ##### DataFrame with 3 countries from South America 

# ##### Temperature change in 3 countries of South America

# In[18]:

# In[10]:


SouthAmerica = df.copy()
SouthAmerica = optional_1(SouthAmerica)
SouthAmerica_whole= SouthAmerica [(SouthAmerica.Continent == 'Shouth America')]
SouthAmerica_temp = SouthAmerica_whole[(SouthAmerica_whole.Area == 'Argentina')| (SouthAmerica_whole.Area == 'Brazil') | (SouthAmerica_whole.Area == 'Peru')]
SouthAmerica_temp = SouthAmerica_temp[(SouthAmerica_temp.Months == 'Meteorological year') & (SouthAmerica_temp.Element == 'Temperature change')]
SouthAmerica_temp


# In[11]:


SouthAmerica_temp.columns = SouthAmerica_temp.columns.str.replace('Y', '')
del SouthAmerica_temp['Area_Code']
del SouthAmerica_temp['Months_Code']
del SouthAmerica_temp['Months']
del SouthAmerica_temp['Element']
del SouthAmerica_temp['Unit']
del SouthAmerica_temp['Element_Code']
del SouthAmerica_temp['Continent']
del SouthAmerica_temp['Continent_Code']
SouthAmerica_temp


# In[ ]:

# ##### Modified table - Temperature change

# In[19]:

# In[12]:


SouthAmerica_temp_mdf = pd.melt(SouthAmerica_temp, id_vars='Area')
SouthAmerica_temp_mdf = SouthAmerica_temp_mdf.rename(columns={'variable': 'Year','value': 'Temperature'})
SouthAmerica_temp_mdf= SouthAmerica_temp_mdf.sort_values(by=['Area', 'Year'])
SouthAmerica_temp_mdf


# In[20]:

# In[13]:


SouthAmerica_temp_mdf.Year = pd.to_numeric(SouthAmerica_temp_mdf.Year)


# In[ ]:

# ##### Value of CO2 in 3 countries of South America

# In[22]:

# In[14]:


SouthAmerica_CO2 = pd.read_csv('co2.csv')


# In[23]:

# In[15]:


del SouthAmerica_CO2['country_code']


# In[24]:

# In[16]:


SouthAmerica_CO2 = SouthAmerica_CO2[(SouthAmerica_CO2.country_name == 'Argentina') | (SouthAmerica_CO2.country_name == 'Brazil')
          | (SouthAmerica_CO2.country_name == 'Peru')]
SouthAmerica_CO2


# In[472]:

# In[17]:


SouthAmerica_CO2 = SouthAmerica_CO2.rename(columns={'country_name':'Area', 'year':'Year', 'value': 'CO2'})
SouthAmerica_CO2


# In[473]:

# In[18]:


SouthAmerica_CO2.Year = pd.to_numeric(SouthAmerica_CO2.Year)


# In[ ]:

# ##### Temperature change and value of CO2

# In[366]:

# In[19]:


SouthAmerica_temp_CO2 = pd.merge(SouthAmerica_temp_mdf, SouthAmerica_CO2, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2


# In[ ]:

# ##### Regression - value of CO2 and temperature change

# In[21]:


sns.set_context('paper')
l=sns.lmplot(data=SouthAmerica_temp_CO2[((SouthAmerica_temp_CO2['Area'] == 'Argentina'))],
                                    
            x="CO2",
            y="Temperature",
            aspect=2.5, 
            col='Area',
            hue = 'Area',
            palette = 'Oranges')
l.set(xlabel = 'CO2 [kt]', ylabel = "Temperatura\u2103")
plt.title('Argentyna')

l1=sns.lmplot(data=SouthAmerica_temp_CO2[((SouthAmerica_temp_CO2['Area'] == 'Brazil'))],
                                    
            x="CO2",
            y="Temperature",
            aspect=2.5, 
            col='Area',
            hue = 'Area',
            palette = 'Oranges')
l1.set(xlabel = 'CO2 [kt]', ylabel = "Temperatura\u2103")
plt.title('Brazylia')

l2=sns.lmplot(data=SouthAmerica_temp_CO2[((SouthAmerica_temp_CO2['Area'] == 'Peru'))],
                                    
            x="CO2",
            y="Temperature",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Oranges')
l2.set(xlabel = 'CO2 [kt]', ylabel = "Temperatura\u2103")
plt.title('Peru')
plt.show()


# In[ ]:

# ##### Chart - temperature change vs value of CO2

# In[60]:


SouthAmerica_temp_CO2

SouthAmerica_temp_CO2.CO2 = round((SouthAmerica_temp_CO2.CO2/1000), 2)


# In[177]:


Argentina_temp_CO2 = SouthAmerica_temp_CO2[(SouthAmerica_temp_CO2.Area == 'Argentina')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('CO2 [mln t]', color='#FF6600')
ax1.bar(Argentina_temp_CO2.Year, Argentina_temp_CO2.CO2, label = 'Argentyna', color ='#FF6600')
ax1.tick_params(axis='y', labelcolor='#FF6600')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zmiana temperatury\u2103', color='#000000') 
ax2.plot(Argentina_temp_CO2.Year, Argentina_temp_CO2.Temperature, label = 'Argentyna', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Argentyna: średnioroczne zmiany temperatury vs emisja CO2 (1961-2019)')
plt.ylim(-1,2.5)



Brazil_temp_CO2 = SouthAmerica_temp_CO2[(SouthAmerica_temp_CO2.Area == 'Brazil')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('CO2 [mln t]', color='#FF6600')
ax1.bar(Brazil_temp_CO2.Year, Brazil_temp_CO2.CO2, label = 'Brazylia', color ='#FF6600')
ax1.tick_params(axis='y', labelcolor='#FF6600')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zmiana temperatury\u2103', color='#000000') 
ax2.plot(Brazil_temp_CO2.Year, Brazil_temp_CO2.Temperature, label = 'Brazylia', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Brazylia: średnioroczne zmiany temperatury vs emisja CO2 (1961-2019)')
plt.ylim(-1,2.5)



Peru_temp_CO2 = SouthAmerica_temp_CO2[(SouthAmerica_temp_CO2.Area == 'Peru')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('CO2 [mln t]', color='#FF6600')
ax1.bar(Peru_temp_CO2.Year, Peru_temp_CO2.CO2, label = 'Peru', color ='#FF6600')
ax1.tick_params(axis='y', labelcolor='#FF6600')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zmiana temperatury\u2103', color='#000000')
ax2.plot(Peru_temp_CO2.Year, Peru_temp_CO2.Temperature, label = 'Peru', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Peru: średnioroczne temperatury vs emisja CO2 (1961-2019)')

plt.ylim(-1,2.5)
plt.show()


# In[ ]:

# ##### GDP per capita in 3 countries of South America

# In[474]:

# In[20]:


SouthAmerica_GDP = pd.read_csv('GDP_percapita.csv')


# In[475]:

# In[21]:


del SouthAmerica_GDP['Code']
del SouthAmerica_GDP['Unnamed: 65']


# In[476]:

# In[22]:


SouthAmerica_GDP = SouthAmerica_GDP.rename(columns={'Country Name':'Area'})


# In[477]:

# In[23]:


SouthAmerica_GDP = SouthAmerica_GDP[(SouthAmerica_GDP.Area == 'Argentina') | (SouthAmerica_GDP.Area == 'Brazil')
          | (SouthAmerica_GDP.Area == 'Peru')]
SouthAmerica_GDP


# In[ ]:

# ##### Modified table - GDP per capita

# In[478]:

# In[24]:


SouthAmerica_GDP_mdf = pd.melt(SouthAmerica_GDP, id_vars='Area')
SouthAmerica_GDP_mdf = SouthAmerica_GDP_mdf.rename(columns={'variable': 'Year', 'value': 'GDP_per_capita'})
SouthAmerica_GDP_mdf= SouthAmerica_GDP_mdf.sort_values(by=['Area', 'Year'])
SouthAmerica_GDP_mdf


# In[479]:

# In[25]:


SouthAmerica_GDP_mdf.Year = pd.to_numeric(SouthAmerica_GDP_mdf.Year)


# In[ ]:

# GDP per capita other charts

# In[427]:

# In[29]:


sns.set_context('paper')
sns.relplot(data=SouthAmerica_GDP_mdf[(SouthAmerica_GDP_mdf['Area'] == 'Argentina')
                                      | (SouthAmerica_GDP_mdf['Area'] == 'Brazil')
                                       |(SouthAmerica_GDP_mdf['Area'] == 'Peru')],
            x="Year",
            y="GDP_per_capita",
            kind='line',
            col='Area')
plt.show()


# In[ ]:

# ##### Percent value of forestation in 3 countries of South America

# In[33]:

# In[26]:


SouthAmerica_forestation = pd.read_csv('forest.csv')


# In[34]:

# In[27]:


del SouthAmerica_forestation['country_code']


# In[35]:

# In[28]:


SouthAmerica_forestation = SouthAmerica_forestation[(SouthAmerica_forestation.country_name == 'Argentina') | (SouthAmerica_forestation.country_name == 'Brazil')
          | (SouthAmerica_forestation.country_name == 'Peru')]
SouthAmerica_forestation


# In[36]:

# In[29]:


SouthAmerica_forestation = SouthAmerica_forestation.rename(columns={'country_name':'Area', 'year':'Year', 'value': 'Forestation_percent'})
SouthAmerica_forestation


# In[37]:

# In[30]:


SouthAmerica_forestation.Year = pd.to_numeric(SouthAmerica_forestation.Year)


# In[ ]:

# ##### Urban population (% of total population) in 3 countries of South America

# In[489]:

# In[31]:


SouthAmerica_urban = pd.read_csv('share-of-population-urban.csv')


# In[490]:

# In[32]:


del SouthAmerica_urban['Code']


# In[491]:

# In[33]:


SouthAmerica_urban = SouthAmerica_urban.rename(columns={'Entity':'Area', 
                                     'Urban population (% of total population)': 'Urbanization_rate_percent'})


# In[492]:

# In[34]:


SouthAmerica_urban = SouthAmerica_urban[(SouthAmerica_urban.Area == 'Argentina') 
                        | (SouthAmerica_urban.Area == 'Brazil')
                            | (SouthAmerica_urban.Area == 'Peru')]
SouthAmerica_urban


# In[493]:

# In[35]:


SouthAmerica_urban.Year = pd.to_numeric(SouthAmerica_urban.Year)


# In[ ]:

# Summarized tabel: Temperature change + CO2 + GDP per capita + Forestation + energy use + urbanization

# In[497]:

# In[36]:


SouthAmerica_temp_CO2 = pd.merge(SouthAmerica_temp_mdf, SouthAmerica_CO2, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP = pd.merge(SouthAmerica_temp_CO2, SouthAmerica_GDP_mdf,  on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP_forest = pd.merge(SouthAmerica_temp_CO2_GDP, SouthAmerica_forestation, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP_forest_urb = pd.merge(SouthAmerica_temp_CO2_GDP_forest, SouthAmerica_urban, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP_forest_urb


# In[ ]:

# ##### Regression - temperature change vs GDP per capita

# In[41]:


sns.set_context('paper')
l=sns.lmplot(data=SouthAmerica_temp_CO2_GDP[((SouthAmerica_temp_CO2_GDP['Area'] == 'Argentina'))],
                                    
            x="GDP_per_capita",
            y="Temperature",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Blues')
l.set(xlabel = 'PKB per capita [$]', ylabel = "Temperatura\u2103")
plt.title('Argentyna')

l1=sns.lmplot(data=SouthAmerica_temp_CO2_GDP[((SouthAmerica_temp_CO2_GDP['Area'] == 'Brazil'))],
                                    
            x="GDP_per_capita",
            y="Temperature",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Blues')
l1.set(xlabel = 'PKB per capita [$]', ylabel = "Temperatura\u2103")
plt.title('Brazylia')

l2=sns.lmplot(data=SouthAmerica_temp_CO2_GDP[((SouthAmerica_temp_CO2_GDP['Area'] == 'Peru'))],
                                    
            x="GDP_per_capita",
            y="Temperature",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Blues')
l2.set(xlabel = 'PKB per capita [$]', ylabel = "Temperatura\u2103")
plt.title('Peru')
plt.show()


# In[ ]:

# ##### Temperature change vs GDP percapita - chart

# In[42]:


Argentina_temp_GDP = SouthAmerica_temp_CO2_GDP[(SouthAmerica_temp_CO2_GDP.Area == 'Argentina')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('PKB per capita [$]', color='#388CB2')
ax1.bar(Argentina_temp_GDP.Year, Argentina_temp_GDP.GDP_per_capita, label = 'Argentyna', color ='#388CB2')
ax1.tick_params(axis='y', labelcolor='#388CB2')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000') 
ax2.plot(Argentina_temp_GDP.Year, Argentina_temp_GDP.Temperature, label = 'Argentyna', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Argentyna: średnioroczne zmiany temperatury vs PKB per capita (1961-2019)')



Brazil_temp_GDP = SouthAmerica_temp_CO2_GDP[(SouthAmerica_temp_CO2_GDP.Area == 'Brazil')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('PKB per capita [$]', color='#388CB2')
ax1.bar(Brazil_temp_GDP.Year, Brazil_temp_GDP.GDP_per_capita, label = 'Brazylia', color ='#388CB2')
ax1.tick_params(axis='y', labelcolor='#388CB2')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000') 
ax2.plot(Brazil_temp_GDP.Year, Brazil_temp_GDP.Temperature, label = 'Brazylia', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Brazylia: średnioroczne zmiany temperatury vs PKB per capita (1961-2019)')




Peru_temp_GDP = SouthAmerica_temp_CO2_GDP[(SouthAmerica_temp_CO2_GDP.Area == 'Peru')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('PKB per capita [$]', color='#388CB2')
ax1.bar(Peru_temp_GDP.Year, Peru_temp_GDP.GDP_per_capita, label = 'Peru', color ='#388CB2')
ax1.tick_params(axis='y', labelcolor='#388CB2')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000')
ax2.plot(Peru_temp_GDP.Year, Peru_temp_GDP.Temperature, label = 'Peru', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Peru: średnioroczne zmiany temperatury vs PKB per capita (1961-2019)')

plt.show()


# In[ ]:

# ##### Regression - temperature change vs forestation

# In[43]:


sns.set_context('paper')
l = sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest[((SouthAmerica_temp_CO2_GDP_forest['Area'] == 'Argentina'))],
                                    
            x="Forestation_percent",
            y="Temperature",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Greens')
l.set(xlabel = 'Zalesienie [%]', ylabel = "Temperatura\u2103")
plt.title('Argentyna')

l1 = sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest[((SouthAmerica_temp_CO2_GDP_forest['Area'] == 'Brazil'))],
                                    
            x="Forestation_percent",
            y="Temperature",
            aspect=2.5, 
            col='Area',
            hue = 'Area',
            palette = 'Greens')
l1.set(xlabel = 'Zalesienie [%]', ylabel = "Temperatura\u2103")
plt.title('Brazylia')

l2 = sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest[((SouthAmerica_temp_CO2_GDP_forest['Area'] == 'Peru'))],
                                    
            x="Forestation_percent",
            y="Temperature",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Greens')
l2.set(xlabel = 'Zalesienie [%]', ylabel = "Temperatura\u2103")
plt.title('Peru')
plt.show()


# In[ ]:

# ##### Temperature change vs forestation - chart

# In[44]:


Argentina_temp_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Argentina')
                                                            &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]
                                             

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Zalesienie [%]', color='#009900')
ax1.bar(Argentina_temp_forest.Year, Argentina_temp_forest.Forestation_percent, label = 'Argentyna', color ='#009900')
ax1.tick_params(axis='y', labelcolor='#009900')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000') 
ax2.plot(Argentina_temp_forest.Year, Argentina_temp_forest.Temperature, label = 'Argentyna', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Argentyna: średnioroczne zmiany temperatury vs zalesienie (1990-2019)')



Brazil_temp_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Brazil')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Zalesienie [%]', color='#009900')
ax1.bar(Brazil_temp_forest.Year, Brazil_temp_forest.Forestation_percent, label = 'Brazylia', color ='#009900')
ax1.tick_params(axis='y', labelcolor='#009900')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000') 
ax2.plot(Brazil_temp_forest.Year, Brazil_temp_forest.Temperature, label = 'Brazylia', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Brazylia: średnioroczne zmiany temperatury vs zalesienie (1990-2019)')





Peru_temp_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Peru')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]
fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Zalesienie [%]', color='#009900')
ax1.bar(Peru_temp_forest.Year, Peru_temp_forest.Forestation_percent, label = 'Peru', color ='#009900')
ax1.tick_params(axis='y', labelcolor='#009900')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000')
ax2.plot(Peru_temp_forest.Year, Peru_temp_forest.Temperature, label = 'Peru', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Peru: średnioroczne zmiany temperatury vs zalesienie (1990-2019)')

plt.show()


# In[ ]:

# ##### Forestation vs GDP per capita - chart

# In[45]:


Argentina_GDP_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Argentina')
                                                            &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]
                                             

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('PKB per capita [$]', color='#388CB2')
ax1.bar(Argentina_GDP_forest.Year, Argentina_GDP_forest.GDP_per_capita, label = 'Argentyna', color ='#388CB2')
ax1.tick_params(axis='y', labelcolor='#388CB2')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900') 
ax2.plot(Argentina_GDP_forest.Year, Argentina_GDP_forest.Forestation_percent, label = 'Argentyna', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Argentyna: Zalesienie vs PKB per capita (1990-2019)')



Brazil_GDP_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Brazil')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('PKB per capita [$]', color='#388CB2')
ax1.bar(Brazil_GDP_forest.Year, Brazil_GDP_forest.GDP_per_capita, label = 'Brazylia', color ='#388CB2')
ax1.tick_params(axis='y', labelcolor='#388CB2')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900') 
ax2.plot(Brazil_GDP_forest.Year, Brazil_GDP_forest.Forestation_percent, label = 'Brazylia', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Brazylia: Zalesienie vs PKB per capita (1990-2019)')



Peru_GDP_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Peru')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]
fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('PKB per capita [$]', color='#388CB2')
ax1.bar(Peru_GDP_forest.Year, Peru_GDP_forest.GDP_per_capita, label = 'Peru', color ='#388CB2')
ax1.tick_params(axis='y', labelcolor='#388CB2')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900')
ax2.plot(Peru_GDP_forest.Year, Peru_GDP_forest.Forestation_percent, label = 'Peru', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Peru: Zalesienie vs PKB per capita (1990-2019)')

plt.show()


# In[ ]:

# ##### Forestation vs value of CO2 - chart

# In[46]:


Argentina_CO2_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Argentina')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]
                                             

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('CO2 [kt]', color='#FF6600')
ax1.bar(Argentina_CO2_forest.Year, Argentina_CO2_forest.CO2, label = 'Argentyna', color ='#FF6600')
ax1.tick_params(axis='y', labelcolor='#FF6600')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900') 
ax2.plot(Argentina_CO2_forest.Year, Argentina_CO2_forest.Forestation_percent, label = 'Argentyna', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Argentyna: Zalesienie vs wielkość emisji CO2 (1990-2019)')



Brazil_GDP_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Brazil')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('CO2 [kt]', color='#FF6600')
ax1.bar(Brazil_GDP_forest.Year, Brazil_GDP_forest.CO2, label = 'Brazylia', color ='#FF6600')
ax1.tick_params(axis='y', labelcolor='#FF6600')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900') 
ax2.plot(Brazil_GDP_forest.Year, Brazil_GDP_forest.Forestation_percent, label = 'Brazylia', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Brazylia: Zalesienie vs wielkość emisji CO2 (1990-2019)')



Peru_GDP_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Peru')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]
fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('CO2 [kt]', color='#FF6600')
ax1.bar(Peru_GDP_forest.Year, Peru_GDP_forest.CO2, label = 'Peru', color ='#FF6600')
ax1.tick_params(axis='y', labelcolor='#FF6600')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900')
ax2.plot(Peru_GDP_forest.Year, Peru_GDP_forest.Forestation_percent, label = 'Peru', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Peru: Zalesienie vs wielkość emisji CO2 (1990-2019)')

plt.show()


# In[ ]:

# ##### Forestation vs urbanization rate - chart

# In[47]:


Argentina_urban_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Argentina')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]
                                             

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Współczynnik urbanizacji [%]', color='#ABABAB')
ax1.bar(Argentina_urban_forest.Year, Argentina_urban_forest.Urbanization_rate_percent, label = 'Argentyna', color ='#ABABAB')
ax1.tick_params(axis='y', labelcolor='#ABABAB')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900') 
ax2.plot(Argentina_urban_forest.Year, Argentina_urban_forest.Forestation_percent, label = 'Argentyna', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Argentyna: Zalesienie vs urbanizacja (1990-2019)')



Brazil_urban_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Brazil')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Współczynnik urbanizacji [%]', color='#ABABAB')
ax1.bar(Brazil_urban_forest.Year, Brazil_urban_forest.Urbanization_rate_percent, label = 'Brazylia', color ='#ABABAB')
ax1.tick_params(axis='y', labelcolor='#ABABAB')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900') 
ax2.plot(Brazil_urban_forest.Year, Brazil_urban_forest.Forestation_percent, label = 'Brazylia', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Brazylia: Zalesienie vs urbanizacja (1990-2019)')



Peru_urban_forest = SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Peru')
                                                           &(SouthAmerica_temp_CO2_GDP_forest_urb.Year > 1989))]
fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Współczynnik urbanizacji [%]', color='#ABABAB')
ax1.bar(Peru_urban_forest.Year, Peru_urban_forest.Urbanization_rate_percent, label = 'Peru', color ='#ABABAB')
ax1.tick_params(axis='y', labelcolor='#ABABAB')

ax2 = ax1.twinx()  

ax2.set_ylabel('Zalesienie [%]', color='#009900')
ax2.plot(Peru_urban_forest.Year, Peru_urban_forest.Forestation_percent, label = 'Peru', color = '#009900')
ax2.tick_params(axis='y', labelcolor='#009900')

fig.tight_layout()  
plt.title('Peru: Zalesienie vs urbanizacja (1990-2019)')

plt.show()


# In[ ]:

# ##### Temperature change vs urbanization rate - chart

# In[48]:


Argentina_temp_urban = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Argentina')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Współczynnik urbanizacji [%]', color='#ABABAB')
ax1.bar(Argentina_temp_urban.Year, Argentina_temp_urban.Urbanization_rate_percent, label = 'Argentyna', color ='#ABABAB')
ax1.tick_params(axis='y', labelcolor='#ABABAB')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000') 
ax2.plot(Argentina_temp_urban.Year, Argentina_temp_urban.Temperature, label = 'Argentyna', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Argentyna: średnioroczne zmiany temperatury vs współczynnik urbanizacji (1961-2019)')



Brazil_temp_urban = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Brazil')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Współczynnik urbanizacji [%]', color='#ABABAB')
ax1.bar(Brazil_temp_urban.Year, Brazil_temp_urban.Urbanization_rate_percent, label = 'Brazylia', color ='#ABABAB')
ax1.tick_params(axis='y', labelcolor='#ABABAB')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000') 
ax2.plot(Brazil_temp_urban.Year, Brazil_temp_urban.Temperature, label = 'Brazylia', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Brazylia: średnioroczne zmiany temperatury vs współczynnik urbanizacji (1961-2019)')




Peru_temp_urban = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Peru')]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Rok')
ax1.set_ylabel('Współczynnik urbanizacji [%]', color='#ABABAB')
ax1.bar(Peru_temp_urban.Year, Peru_temp_urban.Urbanization_rate_percent, label = 'Peru', color ='#ABABAB')
ax1.tick_params(axis='y', labelcolor='#ABABAB')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temperatura\u2103', color='#000000')
ax2.plot(Peru_temp_urban.Year, Peru_temp_urban.Temperature, label = 'Peru', color = '#000000')
ax2.tick_params(axis='y', labelcolor='#000000')

fig.tight_layout()  
plt.title('Peru: średnioroczne zmiany temperatury vs współczynnik urbanizacji (1961-2019)')

plt.show()


# In[ ]:

# ##### Regression - temperature change vs urbanization rate

# In[49]:


sns.set_context('paper')
l= sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Argentina'))],
                                    
            x="Urbanization_rate_percent",
            y="Temperature",
            aspect=2.5,
            col = 'Area',
            hue='Area',
            palette = 'gray')
l.set(xlabel = 'Współczynnik urbanizacji [%]', ylabel = "Temperatura\u2103")
plt.title('Argentyna')

l1 = sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Brazil'))],
                                    
            x="Urbanization_rate_percent",
            y="Temperature",
            aspect=2.5,
            col = 'Area',
            hue='Area',
            palette = 'gray')
l1.set(xlabel = 'Współczynnik urbanizacji [%]', ylabel = "Temperatura\u2103")
plt.title('Brazylia')

l2 = sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Peru'))],
                                    
            x="Urbanization_rate_percent",
            y="Temperature",
            aspect=2.5,
            col = 'Area',
            hue = 'Area',
            palette = 'gray')
l2.set(xlabel = 'Współczynnik urbanizacji [%]', ylabel = "Temperatura\u2103")
plt.title('Peru')
plt.show()


# In[ ]:

# ##### Regression: CO2 vs GDP per capita

# In[51]:


SouthAmerica_temp_CO2_GDP_forest_urb

SouthAmerica_temp_CO2_GDP_forest_urb.CO2 = round((SouthAmerica_temp_CO2_GDP_forest_urb.CO2/1000), 2)


# In[186]:


sns.set_context('paper')
l=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Argentina'))],
                                    
            x="GDP_per_capita",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Blues')
l.set(xlabel = 'PKB per capita [$]', ylabel = "CO2 [mln t]")
plt.title('Argentyna')

l1=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Brazil'))],
                                    
            x="GDP_per_capita",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Blues')
l1.set(xlabel = 'PKB per capita [$]', ylabel = "CO2 [mln t]")
plt.title('Brazylia')
plt.ylim(0,500)
plt.xlim(0,14000)

l2=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Peru'))],
                                    
            x="GDP_per_capita",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Blues')
l2.set(xlabel = 'PKB per capita [$]', ylabel = "CO2 [mln t]")
plt.title('Peru')
plt.show()


# In[ ]:

# ##### Regression: CO2 vs forestation

# In[185]:


sns.set_context('paper')
l=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Argentina'))],
                                    
            x="Forestation_percent",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Greens')
l.set(xlabel = 'Zalesienie [%]', ylabel = "CO2 [mln t]")
plt.title('Argentyna')
plt.ylim(0,500)

l1=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Brazil'))],
                                    
            x="Forestation_percent",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Greens')
l1.set(xlabel = 'Zalesienie [%]', ylabel = "CO2 [mln t]")
plt.title('Brazylia')
plt.ylim(0,500)

l2=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Peru'))],
                                    
            x="Forestation_percent",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'Greens')
l2.set(xlabel = 'Zalesienie [%]', ylabel = "CO2 [mln t]")
plt.title('Peru')
plt.ylim(0,500)
plt.show()


# In[ ]:

# ##### Regression: CO2 vs urbanization rate

# In[187]:


sns.set_context('paper')
l=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Argentina'))],
                                    
            x="Urbanization_rate_percent",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'gray')
l.set(xlabel = 'Współczynnik urbanizacji [%]', ylabel = "CO2 [mln t]")
plt.title('Argentyna')

l1=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Brazil'))],
                                    
            x="Urbanization_rate_percent",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'gray')
l1.set(xlabel = 'Współczynnik urbanizacji [%]', ylabel = "CO2 [mln t]")
plt.title('Brazylia')
plt.ylim(0,500)

l2=sns.lmplot(data=SouthAmerica_temp_CO2_GDP_forest_urb[((SouthAmerica_temp_CO2_GDP_forest_urb['Area'] == 'Peru'))],
                                    
            x="Urbanization_rate_percent",
            y="CO2",
            aspect=2.5, 
            col = 'Area',
            hue = 'Area',
            palette = 'gray')
l2.set(xlabel = 'Współczynnik urbanizacji [%]', ylabel = "CO2 [mln t]")
plt.title('Peru')
plt.show()


# In[ ]:





# In[ ]:

# Correlation Argentina

# In[500]:

# In[37]:


corr_Argentina = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Argentina')]


# In[501]:

# In[38]:


del corr_Argentina['Area']
del corr_Argentina['Year']


# In[502]:

# In[39]:


corr_Argentina = corr_Argentina.corr()
sns.heatmap(corr_Argentina, annot=True, cmap = 'Greens')
plt.show()


# In[62]:


corr_Argentina = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Argentina')]
del corr_Argentina['Area']
del corr_Argentina['Year']

corr_Argentina.rename(columns = {'Temperature' : 'Temperatura', 'CO2': 'CO2', 'Forestation_percent' : 'Poziom zalesienia', 
                                  'GDP_per_capita': 'PKB per capita', 'Urbanization_rate_percent': 'Poziom urbanizacji'}, inplace = True)
corr_Argentina = corr_Argentina.corr()

sns.heatmap(corr_Argentina, annot=True, cmap = 'Greens')
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 15)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 15)
sns.set(font_scale = 1.6) 
plt.xticks(rotation = 90)



plt.show()


# In[ ]:

# In[ ]:

# Correlation Brazil

# In[503]:

# In[53]:


corr_Brazil = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Brazil')]


# In[504]:

# In[54]:


del corr_Brazil['Area']
del corr_Brazil['Year']


# In[505]:

# In[55]:


corr_Brazil = corr_Brazil.corr()
sns.heatmap(corr_Brazil, annot=True, cmap = "Greens")
plt.show()


# In[60]:


corr_Brazil = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Brazil')]
del corr_Brazil['Area']
del corr_Brazil['Year']

corr_Brazil.rename(columns = {'Temperature' : 'Temperatura', 'CO2': 'CO2', 'Forestation_percent' : 'Poziom zalesienia', 
                                  'GDP_per_capita': 'PKB per capita', 'Urbanization_rate_percent': 'Poziom urbanizacji'}, inplace = True)
corr_Brazil = corr_Brazil.corr()

sns.heatmap(corr_Brazil, annot=True, cmap = 'Greens')
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 15)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 15)
sns.set(font_scale = 1.6) 
plt.xticks(rotation = 90)



plt.show()


# In[ ]:

# Correlation Peru

# In[506]:

# In[56]:


corr_Peru = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Peru')]


# In[507]:

# In[57]:


del corr_Peru['Area']
del corr_Peru['Year']


# In[508]:

# In[58]:


corr_Peru = corr_Peru.corr()
sns.heatmap(corr_Peru, annot=True, cmap = "Greens")
plt.show()


# In[64]:


corr_Peru = SouthAmerica_temp_CO2_GDP_forest_urb[(SouthAmerica_temp_CO2_GDP_forest_urb.Area == 'Peru')]
del corr_Peru['Area']
del corr_Peru['Year']

corr_Peru.rename(columns = {'Temperature' : 'Temperatura', 'CO2': 'CO2', 'Forestation_percent' : 'Poziom zalesienia', 
                                  'GDP_per_capita': 'PKB per capita', 'Urbanization_rate_percent': 'Poziom urbanizacji'}, inplace = True)
corr_Peru = corr_Peru.corr()

sns.heatmap(corr_Peru, annot=True, cmap = 'Greens')
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 15)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 15)
sns.set(font_scale = 1.6) 
plt.xticks(rotation = 90)



plt.show()


# In[ ]:

# #### Antarctica

# In[ ]:

# Making individual variable for group purpose working

# ##### Temperature change in Antarctica

# In[526]:

# In[28]:


Antarctica = df.copy()
Antarctica = optional_1(Antarctica)
Antarctica_temp= Antarctica [(Antarctica.Continent == 'Antarctica')]
Antarctica_temp = Antarctica[(Antarctica.Area == 'Antarctica')]
Antarctica_temp = Antarctica_temp[(Antarctica_temp.Months == 'Meteorological year') & (Antarctica_temp.Element == 'Temperature change')]
Antarctica_temp


# In[29]:


Antarctica_temp.columns = Antarctica_temp.columns.str.replace('Y', '')
del Antarctica_temp['Area_Code']
del Antarctica_temp['Months_Code']
del Antarctica_temp['Months']
del Antarctica_temp['Element']
del Antarctica_temp['Unit']
del Antarctica_temp['Element_Code']
del Antarctica_temp['Continent']
del Antarctica_temp['Continent_Code']
Antarctica_temp


# In[ ]:

# ##### Modified table - Temperature change

# In[527]:

# In[30]:


Antarctica_temp_mdf = pd.melt(Antarctica_temp, id_vars='Area')
Antarctica_temp_mdf = Antarctica_temp_mdf.rename(columns={'variable': 'Year','value': 'Temperature'})
Antarctica_temp_mdf


# In[ ]:

# In[530]:

# In[33]:


x1=Antarctica_temp_mdf.Year.unique()

x1 = x1.astype(np.int64)

y1_temp = Antarctica_temp_mdf[Antarctica_temp_mdf.Area == 'Antarctica'].iloc[:,2].values.T

bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'k-', label = 'Antarktyda')

plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Temperatura\u2103')
plt.title('Antarktyda: Średnioroczne zmiany temperatury w latach 1961-2019')
plt.show()


# In[ ]:





# In[62]:


Antarctica_temp_change = Antarctica_temp_mdf [(Antarctica_temp_mdf.Area == 'Antarctica')]
plt.plot(Antarctica_temp_change.Year, Antarctica_temp_change.Temperature, 'k-', label = 'Antarktyda')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Temperatura\u2103')
plt.title('Antarktyda: Średnioroczne zmiany temperatury w latach 1961-2019')
plt.show()


# In[ ]:

# ### Northern Hemisphere

# #### DataFrame with temperature change 

# In[122]:


NHemisphere = pd.read_csv('northern_hemisphere.csv')
NHemisphere


# In[123]:


NHemisphere_temp = pd.melt(NHemisphere, id_vars='Season')
NHemisphere_temp = NHemisphere_temp.rename(columns={'variable': 'Year','value': 'Temperature'})
NHemisphere_temp = NHemisphere_temp.sort_values(by=['Season', 'Year'])
NHemisphere_temp


# In[124]:


NHemisphere_temp.Year = pd.to_numeric(NHemisphere_temp.Year)


# In[125]:


NHemisphere_temp_1 = NHemisphere_temp[((NHemisphere_temp.Season == 'winter') & (NHemisphere_temp.Year == 1974))
                            | ((NHemisphere_temp.Season == 'winter') & (NHemisphere_temp.Year == 1989))
                            | ((NHemisphere_temp.Season == 'winter') & (NHemisphere_temp.Year == 2004))
                            | ((NHemisphere_temp.Season == 'winter') & (NHemisphere_temp.Year == 2019))
                            | ((NHemisphere_temp.Season == 'spring') & (NHemisphere_temp.Year == 1974))
                            | ((NHemisphere_temp.Season == 'spring') & (NHemisphere_temp.Year == 1989))
                            | ((NHemisphere_temp.Season == 'spring') & (NHemisphere_temp.Year == 2004))
                            | ((NHemisphere_temp.Season == 'spring') & (NHemisphere_temp.Year == 2019))
                            | ((NHemisphere_temp.Season == 'summer') & (NHemisphere_temp.Year == 1974))
                            | ((NHemisphere_temp.Season == 'summer') & (NHemisphere_temp.Year == 1989))
                            | ((NHemisphere_temp.Season == 'summer') & (NHemisphere_temp.Year == 2004))
                            | ((NHemisphere_temp.Season == 'summer') & (NHemisphere_temp.Year == 2019))
                            | ((NHemisphere_temp.Season == 'autumn') & (NHemisphere_temp.Year == 1974))
                            | ((NHemisphere_temp.Season == 'autumn') & (NHemisphere_temp.Year == 1989))
                            | ((NHemisphere_temp.Season == 'autumn') & (NHemisphere_temp.Year == 2004))
                            | ((NHemisphere_temp.Season == 'autumn') & (NHemisphere_temp.Year == 2019))]

NHemisphere_temp_2=NHemisphere_temp_1.sort_values(ascending = False, by= ['Season'])
NHemisphere_temp_2


# In[90]:


sns.set_theme(style="dark")
NHemisphere_temp_2

# Plot each year's time series in its own facet
g = sns.relplot(
    data=NHemisphere_temp_2,
    x="Season", y="Temperature", col="Year", hue="Year",
    kind="line", palette="Greys", linewidth=4, zorder=5,
    col_wrap=2, height=4, aspect=1.5, legend=False,
)

# Iterate over each subplot to customize further
for year, ax in g.axes_dict.items():

    # Add the title as an annotation within the plot
    ax.text(.8, .85, year, transform=ax.transAxes, fontweight="bold")

    # Plot every year's time series in the background
    sns.lineplot(
        data=NHemisphere_temp_2, x="Season", y="Temperature", units="Year",
        estimator=None, color=".8", linewidth=1, ax=ax,
    )

# Reduce the frequency of the x axis ticks
ax.set_xticks(ax.get_xticks()[::1])

# Tweak the supporting aspects of the plot
g.set_titles("")
g.set_axis_labels("", "Temperatura [°C]")
g.tight_layout()


# In[126]:


NHemisphere_temp_3 = NHemisphere_temp[(NHemisphere_temp.Season == 'northern_temp_meteo_year')]
NHemisphere_temp_3


# In[ ]:

# ### Southern Hemisphere

# #### DataFrame with temperature change

# In[127]:


SHemisphere = pd.read_csv('southern_hemisphere.csv')
SHemisphere


# In[128]:


SHemisphere_temp = pd.melt(SHemisphere, id_vars='Season')
SHemisphere_temp = SHemisphere_temp.rename(columns={'variable': 'Year','value': 'Temperature'})
SHemisphere_temp = SHemisphere_temp.sort_values(by=['Season', 'Year'])
SHemisphere_temp


# In[129]:


SHemisphere_temp.Year = pd.to_numeric(SHemisphere_temp.Year)


# In[130]:


SHemisphere_temp_1 = SHemisphere_temp[((SHemisphere_temp.Season == 'winter') & (SHemisphere_temp.Year == 1974))
                            | ((SHemisphere_temp.Season == 'winter') & (SHemisphere_temp.Year == 1989))
                            | ((SHemisphere_temp.Season == 'winter') & (SHemisphere_temp.Year == 2004))
                            | ((SHemisphere_temp.Season == 'winter') & (SHemisphere_temp.Year == 2019))
                            | ((SHemisphere_temp.Season == 'spring') & (SHemisphere_temp.Year == 1974))
                            | ((SHemisphere_temp.Season == 'spring') & (SHemisphere_temp.Year == 1989))
                            | ((SHemisphere_temp.Season == 'spring') & (SHemisphere_temp.Year == 2004))
                            | ((SHemisphere_temp.Season == 'spring') & (SHemisphere_temp.Year == 2019))
                            | ((SHemisphere_temp.Season == 'summer') & (SHemisphere_temp.Year == 1974))
                            | ((SHemisphere_temp.Season == 'summer') & (SHemisphere_temp.Year == 1989))
                            | ((SHemisphere_temp.Season == 'summer') & (SHemisphere_temp.Year == 2004))
                            | ((SHemisphere_temp.Season == 'summer') & (SHemisphere_temp.Year == 2019))
                            | ((SHemisphere_temp.Season == 'autumn') & (SHemisphere_temp.Year == 1974))
                            | ((SHemisphere_temp.Season == 'autumn') & (SHemisphere_temp.Year == 1989))
                            | ((SHemisphere_temp.Season == 'autumn') & (SHemisphere_temp.Year == 2004))
                            | ((SHemisphere_temp.Season == 'autumn') & (SHemisphere_temp.Year == 2019))]

SHemisphere_temp_2=SHemisphere_temp_1.sort_values(ascending = False, by= ['Season'])
SHemisphere_temp_2


# In[373]:



SHemisphere_temp_2

# Plot each year's time series in its own facet
g = sns.relplot(
    data=SHemisphere_temp_2,
    x="Season", y="Temperature", col="Year", hue="Year",
    kind="line", palette="Greys", linewidth=4, zorder=5,
    col_wrap=2, height=4, aspect=1.5, legend=False,
)

# Iterate over each subplot to customize further
for year, ax in g.axes_dict.items():

    # Add the title as an annotation within the plot
    ax.text(.8, .85, year, transform=ax.transAxes, fontweight="bold")

    # Plot every year's time series in the background
    sns.lineplot(
        data=SHemisphere_temp_2, x="Season", y="Temperature", units="Year",
        estimator=None, color=".8", linewidth=1, ax=ax,
    )

# Reduce the frequency of the x axis ticks
ax.set_xticks(ax.get_xticks()[::1])

# Tweak the supporting aspects of the plot
g.set_titles("")
g.set_axis_labels("", "Temperatura [°C]")
g.tight_layout()


# In[131]:


SHemisphere_temp_3 = SHemisphere_temp[(SHemisphere_temp.Season == 'southern_temp_meteo_year')]
SHemisphere_temp_3


# In[46]:


NHemisphere_temp_3
SHemisphere_temp_3
plt.plot(NHemisphere_temp_3.Year, NHemisphere_temp_3.Temperature, 'k-', label = 'Półkula Północa')
plt.plot(SHemisphere_temp_3.Year, SHemisphere_temp_3.Temperature, 'k--', label = 'Półkula Południowa')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.show()


# In[132]:


x1=NHemisphere_temp_3.Year.unique()

x1 = x1.astype(np.int64)

y1_temp = NHemisphere_temp_3[NHemisphere_temp_3.Season == 'northern_temp_meteo_year'].iloc[:,2].values.T

bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 


x2=SHemisphere_temp_3.Year.unique()

x2 = x1.astype(np.int64)

y2_temp = SHemisphere_temp_3[SHemisphere_temp_3.Season == 'southern_temp_meteo_year'].iloc[:,2].values.T

bspl2 = splrep(x2, y2_temp, s=4)
bspl_y2 = splev(x2, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'k-', label = 'Półkula Północna')
plt.plot(x2, bspl_y2, 'k--', label = 'Półkula Południowa')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.show()


# In[133]:


Hemispheres = pd.merge(NHemisphere_temp_3, SHemisphere_temp_3, on =['Season','Year', 'Temperature'], how = 'outer')
Hemispheres


# In[134]:


Hemispheres_1 = Hemispheres[(((Hemispheres.Season == 'northern_temp_meteo_year') & (Hemispheres.Year == 1961))
                            | ((Hemispheres.Season == 'southern_temp_meteo_year') & (Hemispheres.Year == 1961))
                            | ((Hemispheres.Season == 'northern_temp_meteo_year') & (Hemispheres.Year == 1976))
                            | ((Hemispheres.Season == 'southern_temp_meteo_year') & (Hemispheres.Year == 1976))
                            | ((Hemispheres.Season == 'northern_temp_meteo_year') & (Hemispheres.Year == 1991))
                            | ((Hemispheres.Season == 'southern_temp_meteo_year') & (Hemispheres.Year == 1991))
                            | ((Hemispheres.Season == 'northern_temp_meteo_year') & (Hemispheres.Year == 2006))
                            | ((Hemispheres.Season == 'southern_temp_meteo_year') & (Hemispheres.Year == 2006))
                            | ((Hemispheres.Season == 'northern_temp_meteo_year') & (Hemispheres.Year == 2019))
                            | ((Hemispheres.Season == 'southern_temp_meteo_year') & (Hemispheres.Year == 2019)))]

Hemispheres_1


# In[139]:


Hemispheres_1

# Draw a nested barplot by species and sex
g = sns.catplot(
    data=Hemispheres_1, kind="bar",
    x="Year", y="Temperature", hue="Season",
    palette="bone", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Rok", "Zmiana temperatury\u2103")
g.legend.set_title("Średnioroczne zmiany temperatury")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:

# ### Climatic zones

# #### DataFrame with temperature change

# In[11]:


climatic_zone = pd.read_csv('climatic_zones.csv')
climatic_zone


# In[12]:


climatic_zone_temp = pd.melt(climatic_zone, id_vars='Strefa')
climatic_zone_temp = climatic_zone_temp.rename(columns={'variable': 'Year','value': 'Temperature'})
climatic_zone_temp = climatic_zone_temp.sort_values(by=['Strefa', 'Year'])
climatic_zone_temp


# In[13]:


climatic_zone_temp.Year = pd.to_numeric(climatic_zone_temp.Year)


# In[14]:


climatic_zone_temp_1 = climatic_zone_temp[((climatic_zone_temp.Strefa == 'A_okołobiegunowa (N)') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'B_umiarkowana (N)') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'C_podzwrotnikowa (N)') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'D_zwrotnikowa (N)') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'E_równikowa') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'F_zwrotnikowa (S)') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'G_podzwrotnikowa (S)') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'H_umiarkowana (S)') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'I_okołobiegunowa (S)') & (climatic_zone_temp.Year == 1961))
                            | ((climatic_zone_temp.Strefa == 'A_okołobiegunowa (N)') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'B_umiarkowana (N)') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'C_podzwrotnikowa (N)') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'D_zwrotnikowa (N)') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'E_równikowa') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'F_zwrotnikowa (S)') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'G_podzwrotnikowa (S)') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'H_umiarkowana (S)') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'I_okołobiegunowa (S)') & (climatic_zone_temp.Year == 1976))
                            | ((climatic_zone_temp.Strefa == 'A_okołobiegunowa (N)') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'B_umiarkowana (N)') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'C_podzwrotnikowa (N)') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'D_zwrotnikowa (N)') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'E_równikowa') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'F_zwrotnikowa (S)') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'G_podzwrotnikowa (S)') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'H_umiarkowana (S)') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'I_okołobiegunowa (S)') & (climatic_zone_temp.Year == 1991))
                            | ((climatic_zone_temp.Strefa == 'A_okołobiegunowa (N)') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'B_umiarkowana (N)') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'C_podzwrotnikowa (N)') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'D_zwrotnikowa (N)') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'E_równikowa') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'F_zwrotnikowa (S)') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'G_podzwrotnikowa (S)') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'H_umiarkowana (S)') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'I_okołobiegunowa (S)') & (climatic_zone_temp.Year == 2006))
                            | ((climatic_zone_temp.Strefa == 'A_okołobiegunowa (N)') & (climatic_zone_temp.Year == 2019))
                            | ((climatic_zone_temp.Strefa == 'B_umiarkowana (N)') & (climatic_zone_temp.Year == 2019))
                            | ((climatic_zone_temp.Strefa == 'C_podzwrotnikowa (N)') & (climatic_zone_temp.Year == 2019))
                            | ((climatic_zone_temp.Strefa == 'D_zwrotnikowa (N)') & (climatic_zone_temp.Year == 2019))
                            | ((climatic_zone_temp.Strefa == 'E_równikowa') & (climatic_zone_temp.Year == 2019))
                            | ((climatic_zone_temp.Strefa == 'F_zwrotnikowa (S)') & (climatic_zone_temp.Year == 2019))
                            | ((climatic_zone_temp.Strefa == 'G_podzwrotnikowa (S)') & (climatic_zone_temp.Year == 2019))
                            | ((climatic_zone_temp.Strefa == 'H_umiarkowana (S)') & (climatic_zone_temp.Year == 2019))
                            | ((climatic_zone_temp.Strefa == 'I_okołobiegunowa (S)') & (climatic_zone_temp.Year == 2019))]

Climatic_zone_temp_2=climatic_zone_temp_1.sort_values(ascending = True, by= ['Strefa'])                                     
Climatic_zone_temp_2


# In[146]:


Climatic_zone_temp_2

# Plot each year's time series in its own facet
g = sns.relplot(
    data=Climatic_zone_temp_2,
    x="Strefa", y="Temperature", col="Year", hue="Year",
    kind="line", palette="copper_r", linewidth=4, zorder=5,
    col_wrap=2, height=4, aspect=1.5, legend=False,
)

# Iterate over each subplot to customize further
for year, ax in g.axes_dict.items():

    # Add the title as an annotation within the plot
    ax.text(.8, .85, year, transform=ax.transAxes, fontweight="bold")

    # Plot every year's time series in the background
    sns.lineplot(
        data=Climatic_zone_temp_2, x="Strefa", y="Temperature", units="Year",
        estimator=None, color=".8", linewidth=1, ax=ax,
    )

# Reduce the frequency of the x axis ticks
ax.set_xticks(ax.get_xticks()[::1])

# Tweak the supporting aspects of the plot
g.set_titles("")
g.set_axis_labels("Strefa klimatyczna", "Zmiana temperatury\u2103")
g.set_xticklabels(rotation=60)
g.tight_layout()


# In[ ]:

# ##### Comparing climatic zones

# In[66]:


ob_zone_A = climatic_zone_temp[(climatic_zone_temp.Strefa == 'A_okołobiegunowa (N)')]
ob_zone_I = climatic_zone_temp[(climatic_zone_temp.Strefa == 'I_okołobiegunowa (S)')]

plt.plot(ob_zone_A.Year, ob_zone_A.Temperature,'k-', label = 'strefa okołobiegunowa (N)')
plt.plot(ob_zone_I.Year, ob_zone_I.Temperature, 'k--', label = 'strefa okołobiegunowa (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.show()


# In[19]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'A_okołobiegunowa (N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'I_okołobiegunowa (S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'k-', label = 'strefa okołobiegunowa (N)')
plt.plot(x1, bspl_y2, 'k--', label = 'strefa okołobiegunowa (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.ylim(-0.8, 3.2)
plt.show()


# In[149]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'A_okołobiegunowa (N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'I_okołobiegunowa (S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'b-', label = 'strefa okołobiegunowa (N)')
plt.plot(x1, bspl_y2, 'b--', label = 'strefa okołobiegunowa (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.show()


# In[20]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'B_umiarkowana (N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'H_umiarkowana (S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'k-', label = 'strefa umiarkowana (N)')
plt.plot(x1, bspl_y2, 'k--', label = 'strefa umiarkowana (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.ylim(-0.5, 1.5)
plt.show()


# In[21]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'B_umiarkowana (N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'H_umiarkowana (S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'g-', label = 'strefa umiarkowana (N)')
plt.plot(x1, bspl_y2, 'g--', label = 'strefa umiarkowana (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.ylim(-0.5, 1.5)
plt.show()


# In[22]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'C_podzwrotnikowa (N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'G_podzwrotnikowa (S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'k-', label = 'strefa podzwrotnikowa (N)')
plt.plot(x1, bspl_y2, 'k--', label = 'strefa podzwrotnikowa (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.ylim(-0.5, 1.5)
plt.show()


# In[23]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'C_podzwrotnikowa (N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'G_podzwrotnikowa (S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'y-', label = 'strefa podzwrotnikowa (N)')
plt.plot(x1, bspl_y2, 'y--', label = 'strefa podzwrotnikowa (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.ylim(-0.5, 1.5)
plt.show()


# In[24]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'D_zwrotnikowa (N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'F_zwrotnikowa (S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'k-', label = 'strefa zwrotnikowa (N)')
plt.plot(x1, bspl_y2, 'k--', label = 'strefa zwrotnikowa (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.ylim(-0.5, 1.5)
plt.show()


# In[28]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'D_zwrotnikowa (N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'F_zwrotnikowa (S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'tab:orange', label = 'strefa zwrotnikowa (N)')
plt.plot(x1, bspl_y2, 'k--',label = 'strefa zwrotnikowa (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.ylim(-0.5, 1.5)
plt.legend()
plt.show()


# In[26]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'J_pozostałe_strefy_(N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'E_równikowa'].iloc[:,2].values.T
y3_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'K_pozostałe_strefy_(S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

bspl3 = splrep(x1, y3_temp, s=4)
bspl_y3 = splev(x1, bspl3)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'k--', label = 'pozostałe strefy (N)')
plt.plot(x1, bspl_y2, 'k-', label = 'strefa równikowa')
plt.plot(x1, bspl_y3, 'k.', label = 'pozostałe strefy (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.ylim(-0.5, 1.5)
plt.show()


# In[27]:


x1=climatic_zone_temp.Year.unique()
x1 = x1.astype(np.int64)

y1_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'J_pozostałe_strefy_(N)'].iloc[:,2].values.T
y2_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'E_równikowa'].iloc[:,2].values.T
y3_temp = climatic_zone_temp[climatic_zone_temp.Strefa == 'K_pozostałe_strefy_(S)'].iloc[:,2].values.T
bspl1 = splrep(x1, y1_temp, s=4)
bspl_y1 = splev(x1, bspl1) 

bspl2 = splrep(x1, y2_temp, s=4)
bspl_y2 = splev(x1, bspl2)

bspl3 = splrep(x1, y3_temp, s=4)
bspl_y3 = splev(x1, bspl3)

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x1, bspl_y1, 'k--', label = 'pozostałe strefy (N)')
plt.plot(x1, bspl_y2, 'r-', label = 'strefa równikowa')
plt.plot(x1, bspl_y3, 'k.', label = 'pozostałe strefy (S)')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Zmiana temperatury\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.ylim(-0.5, 1.5)
plt.show()


# In[ ]:





# In[ ]:

# In[ ]:

# #### URSULA

# In[ ]:

# Making individual variable for group purpose working

# In[ ]:

# In[ ]:


urs = df.copy()


# In[ ]:
