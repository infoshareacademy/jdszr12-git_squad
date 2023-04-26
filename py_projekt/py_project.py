#!/usr/bin/env python
# coding: utf-8

# # Climate catastrophe<br>
# <br>
# ## Data analysis on changes in average temperatures<br>
# <br>
# Project analyzing data on changes in average temperatures. The `csv` file containing the raw data can be found at [kaggle.com](https://www.kaggle.com/datasets/sevgisarac/temperature-change)

# ### Import

# In[ ]:

# In[25]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### DataFrame

# In[ ]:

# Default value

# In[26]:


pd.set_option("display.width", 80)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[ ]:

# Default DataFrame

# In[27]:


df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv",
                 encoding="Windows-1250")  # index_col=False


# df.head(1)

# In[ ]:

# In[7]:


df.shape


# In[ ]:

# Columns name rename, where \s (inside names) into _

# In[28]:


df = df.rename(columns={"Area Code": "Area_Code",
                        "Months Code": "Months_Code",
                        "Element Code": "Element_Code"})


# In[ ]:

# Replacing comas in string

# In[29]:


df['Area'] = df['Area'].str.replace(',', '')


# Replacing quote in string

# In[10]:


df['Area'] = df['Area'].str.replace('\"', '')


# In[ ]:

# Optional 1 !!! (Jaro is using this in his part o code)<br>
# Adding continent name & continent number columns. To have those columns added to default dataframe.<br>
# 1. Reading and creating additional frame, for join puprose (from '_Countries_Continents.csv' file)<br>
# 2. Inner join default dataframe with two new columns (continents for each country)<br>
# (every rows containing country name will stay in df)<br>
# (every rows containing geo-region name will not stay in df)

# In[30]:


def optional_1(df):
    continent = pd.read_csv("_Countries_Continents.csv", names=[
                            'Area', 'Continent', 'Continent_Code'], encoding="UTF-8")
   
    df = pd.merge(left=continent, right=df, on='Area', how='inner')
    return df


# In[ ]:

# Optional 2 !!! (Jaro is using this in his part o code)<br>
# 1. Remove each row that contain 'Standard Deviation' value in column 'Element_Code' (code: 7271)<br>
# 2. For loop that will iterate each row (separately), searching NaN values in last 59 columns (year columns).<br>
# After each iteration every NaN will be updated to row mean value (from 59 year columns for each row separately)<br>
# new df is returned but it must be override, like: "df_new = optional_2(df)"<br>
# (of course this can be the same variable: "df = optional_2(df)" )

# In[31]:


def optional_2(df):
    df = df.loc[(df['Element_Code'] == 7271) & (df['Area_Code'] < 5000)]
    for i in range(df.shape[0]-1):
        m = round(df.iloc[i, -59:].mean(), 3)
        df.iloc[i, -59:] = df.iloc[i, -59:].fillna(m)
    return df


# #### JARO

# #### Displayng all rows in dataframe<br>
# `pd.set_option('display.max_rows', None)`

# In[ ]:

# In[13]:


jaro1 = df.copy()


# In[ ]:

# In[14]:


jaro1.columns = jaro1.columns.str.replace('Y', '')


# #### Whole World temperatures (1961-2019)

# In[ ]:

# In[15]:


world_t = jaro1.loc[(jaro1['Area_Code'] == 5000) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# world_t.iloc[:,-59:].isna().sum()
world_t_ok = world_t.iloc[:, -59:]


# #### Africa temperatures (1961-2019)

# #### Africa temperatures (1961-2019)

# In[ ]:

# In[16]:


africa_t = jaro1.loc[(jaro1['Area_Code'] == 5100) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# africa_t.iloc[:,-59:].isna().sum()
africa_t_ok = africa_t.iloc[:, -59:]


# #### Caribbean, Northern & Central Americas temperatures (1961-2019)

# In[ ]:

# In[17]:


north_america_t = jaro1.loc[((jaro1['Area_Code'] == 5203) | (jaro1['Area_Code'] == 5204) | (jaro1['Area_Code'] == 5206))
                            & (jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# north_america_t.iloc[:,-59:].isna().sum()
north_america_t_ok = north_america_t.iloc[:, -59:].mean()


# #### South America temperatures (1961-2019)

# In[ ]:

# In[15]:


south_america_t = jaro1.loc[(jaro1['Area_Code'] == 5207) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# south_america_t.iloc[:,-59:].isna().sum()
south_america_t_ok = south_america_t.iloc[:, -59:]


# #### Asia temperatures (1961-2019)

# In[ ]:

# In[16]:


asia_t = jaro1.loc[(jaro1['Area_Code'] == 5300) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# asia_t.iloc[:,-59:].isna().sum()
asia_t_ok = asia_t.iloc[:, -59:]


# #### Europe temperatures (1961-2019)

# In[ ]:

# In[17]:


europe_t = jaro1.loc[(jaro1['Area_Code'] == 5400) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# europe_t.iloc[:,-59:].isna().sum()
europe_t_ok = europe_t.iloc[:, -59:]


# #### Oceania temperatures (1961-2019)

# In[ ]:

# In[18]:


oceania_t = jaro1.loc[(jaro1['Area_Code'] == 5500) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
oceania_t_ok = oceania_t.iloc[:, -59:]


# #### Antarctica temperatures (1961-2019)

# In[ ]:

# In[19]:


antarctica_t = jaro1.loc[(jaro1['Area_Code'] == 30) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
antarctica_t_ok = antarctica_t.iloc[:, -59:]


# In[ ]:

# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = africa_t_ok.values.T


# In[21]:


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


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = north_america_t_ok.values.T


# In[23]:


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


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = south_america_t_ok.values.T


# In[25]:


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


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = asia_t_ok.values.T


# In[27]:


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


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = europe_t_ok.values.T


# In[29]:


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


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = oceania_t_ok.values.T


# In[31]:


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


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = antarctica_t_ok.values.T


# In[33]:


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


jaro = optional_1(df)
jaro.columns = jaro.columns.str.replace('Y', '')
jaro.shape


# Removing specific rows, leaving only those where:<br><br>
# 1. 'Months_Code' is 'Meteorological year'<br><br>
# 2. 'Element_Code' is 'Temperature change'<br><br>
# 3. 'Area_Code' < 5000 means only countries (not regions name)

# In[ ]:

# In[35]:


jaro = jaro.loc[(jaro['Months_Code'] == 7020) & (
    jaro['Element_Code'] == 7271) & (jaro['Area_Code'] < 5000)]
jaro.shape


# Using 'Optional 2'

# In[ ]:

# In[36]:


jaro = optional_2(jaro)
jaro.shape


# #### If optional_1() and/or optional_2() isn't choosen then start from here:

# Making individual variable for group purpose working

# In[ ]:

# In[37]:


jaro = df.copy()


# In[38]:


antarctica_t = jaro1.loc[(jaro1['Area_Code'] == 30) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
antarctica_t_ok = antarctica_t.iloc[:, -59:]


# In[ ]:

# In[39]:


jaro.iloc[:, -59:].isna().sum()


# #### NORTHERN & CENTRAL AMERICA

# In[ ]:

# Making individual variable for group purpose working

# DataFrame with 5 countries from America (Northern & Central

# In[40]:


NAmerica = df.copy()
NAmerica = optional_1(NAmerica)
NAmerica_full= NAmerica [(NAmerica.Continent == 'North America')]
NAmerica_c3 = NAmerica_full[(NAmerica_full.Area == 'Canada')
              | (NAmerica_full.Area == 'United States of America')
                | (NAmerica_full.Area == 'Dominican Republic')]
NAmerica_c3 = NAmerica_c3[(NAmerica_c3.Months == 'Meteorological year')
              & (NAmerica_c3.Element == 'Temperature change')]
NAmerica_c3


# Inp[]:<br>
# reparing data

# In[41]:


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


# In[]:<br>
# Transformation table

# In[42]:


NAmerica_trans = pd.melt(NAmerica_c3, id_vars='Area')
NAmerica_trans = NAmerica_trans.rename(columns={'variable': 'Year',
                              'value': 'Temp'})
NAmerica_trans = NAmerica_trans.sort_values(by=['Area', 'Year'])
NAmerica_trans.Year = pd.to_numeric(NAmerica_trans.Year)
NAmerica_trans.info()


# In[]:<br>
# DataFrame with Forests

# In[43]:


NAmerica_forest = pd.read_csv('forest.csv')
NAmerica_forest = NAmerica_forest[(NAmerica_forest.country_name == 'Canada')
                | (NAmerica_forest.country_name == 'United States')
                | (NAmerica_forest.country_name == 'Dominican Republic')]


# In[44]:


NAmerica_forest = NAmerica_forest.rename(columns={'year': 'Year',
                                'country_name': 'Area',
                                'value': 'Forest'})


# In[45]:


NAmerica_forest.replace(to_replace="United States",
           value="United States of America", inplace=True)


# In[46]:


del NAmerica_forest['country_code']
NAmerica_forest.Year = pd.to_numeric(NAmerica_forest.Year)
NAmerica_forest.isnull().sum()
NAmerica_forest


# In[]:<br>
# DataFrame with CO2

# In[47]:


NAmerica_co2 = pd.read_csv('co2.csv')
NAmerica_co2 = NAmerica_co2[(NAmerica_co2.country_name == 'Canada')
          | (NAmerica_co2.country_name == 'United States')
          | (NAmerica_co2.country_name == 'Dominican Republic')]


# In[48]:


NAmerica_co2 = NAmerica_co2.rename(columns={'year': 'Year',
                          'country_name': 'Area',
                          'value': 'CO2'})


# In[49]:


NAmerica_co2.replace(to_replace="United States",
           value="United States of America", inplace=True)


# In[50]:


del NAmerica_co2['country_code']


# In[51]:


NAmerica_co2.isnull().sum()


# In[52]:


NAmerica_co2.info()


# In[]:<br>
# DataFrame with GDP

# In[53]:


NAmerica_gdp = pd.read_csv('GDP_percapita.csv')


# In[54]:


NAmerica_gdp = NAmerica_gdp.rename(columns={'Country Name':'Area'})


# In[55]:


NAmerica_gdp = NAmerica_gdp[(NAmerica_gdp.Area == 'Canada')
          | (NAmerica_gdp.Area == 'United States')
          | (NAmerica_gdp.Area == 'Dominican Republic')]


# In[56]:


NAmerica_gdp.replace(to_replace="United States",
           value="United States of America", inplace=True)
del NAmerica_gdp['Code']
del NAmerica_gdp['Unnamed: 65']


# In[57]:


NAmerica_gdp


# In[]:<br>
# Transform GDP

# In[58]:


NAmerica_gdp_trans = pd.melt(NAmerica_gdp, id_vars='Area')
NAmerica_gdp_trans = NAmerica_gdp_trans.rename(columns={'variable': 'Year',
                              'value': 'GDP_per_capita'})
NAmerica_gdp_trans = NAmerica_gdp_trans.sort_values(by=['Area', 'Year'])
NAmerica_gdp_trans.Year = pd.to_numeric(NAmerica_gdp_trans.Year)


# In[59]:


NAmerica_gdp_trans


# In[]:<br>
# Join  temperature, forest, co2 and GDP

# In[60]:


NAmerica_tf = pd.merge(NAmerica_trans, NAmerica_forest, on =['Area','Year'], how = 'left')
NAmerica_tfc = pd.merge(NAmerica_tf, NAmerica_co2, on=['Area', 'Year'], how = 'left')
NAmerica_tfcg = pd.merge(NAmerica_tfc, NAmerica_gdp_trans, on=['Area', 'Year'], how = 'left')
NAmerica_tfcg 


# In[]:<br>
#  Temperature

# In[61]:


tfc_Canada = NAmerica_tfcg [(NAmerica_tfcg.Area == 'Canada')]
tfc_US = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
tfc_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.Temp, label = 'Kanada')
plt.plot(tfc_US.Year, tfc_US.Temp, label = 'Stany Zjednoczone')
plt.plot(tfc_Dominican.Year, tfc_Dominican.Temp, label = 'Dominikana')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103')
plt.title('Zmiany temperatur (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  Forest

# In[62]:


tfc_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
tfc_US = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
tfc_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.Forest, label = 'Kanada')
plt.plot(tfc_US.Year, tfc_US.Forest, label = 'Stany Zjednoczone')
plt.plot(tfc_Dominican.Year, tfc_Dominican.Forest, label = 'Dominikana')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Poziom zalesienia')
plt.title('Zalesienie (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  CO2

# In[63]:


tfc_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
tfc_US = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
tfc_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.CO2, label = 'Kanada')
plt.plot(tfc_US.Year, tfc_US.CO2, label = 'Stany Zjednoczone')
plt.plot(tfc_Dominican.Year, tfc_Dominican.CO2, label = 'Dominikana')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Emisja CO^2')
plt.title('Emisja CO^2 (1961-2019)')
plt.legend()
plt.show()


# n[]:<br>
# Correlation_Canada

# In[64]:


corr_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
del corr_Canada['Area']
del corr_Canada['Year']


# In[65]:


corr_Canada= corr_Canada.corr()
sns.heatmap(corr_Canada, annot=True)
plt.show()


# n[]:<br>
# Correlation_USA

# In[66]:


corr_USA = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
del corr_USA['Area']
del corr_USA['Year']


# In[67]:


corr_USA= corr_USA.corr()
sns.heatmap(corr_USA, annot=True)
plt.show()


# n[]:<br>
# Correlation_Dominican

# In[68]:


corr_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
del corr_Dominican['Area']
del corr_Dominican['Year']


# In[69]:


corr_Dominican= corr_Dominican.corr()
sns.heatmap(corr_Dominican, annot=True)
plt.show()


# #### AFRICA<br>
# In[ ]:

# Making individual variable for group purpose working

# DataFrame with 3 countries from Africa

# In[70]:


africa = df.copy()
africa_t = optional_1(africa)
africa_t_full= africa_t [(africa_t.Continent == 'Africa')]
africa_t_c3 = africa_t_full[(africa_t_full.Area == 'Algeria')
                | (africa_t_full.Area == 'United Republic of Tanzania')
                | (africa_t_full.Area == 'Mozambique')]
africa_t_c3 = africa_t_c3[(africa_t_c3.Months == 'Meteorological year')
              & (africa_t_c3.Element == 'Temperature change')]
africa_t_c3


# Inp[]:<br>
# reparing data

# In[71]:


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


# In[]:<br>
# Transformation table

# In[72]:


africa_t_c3_trans = pd.melt(africa_t_c3, id_vars='Area')
africa_t_c3_trans = africa_t_c3_trans.rename(columns={'variable': 'Year',
                              'value': 'Temp'})
africa_t_c3_trans = africa_t_c3_trans.sort_values(by=['Area', 'Year'])
africa_t_c3_trans.Year = pd.to_numeric(africa_t_c3_trans.Year)
africa_t_c3_trans.info()


# In[]:<br>
# DataFrame with Forests

# In[73]:


africa_forest = pd.read_csv('forest.csv')
africa_forest = africa_forest[(africa_forest.country_name == 'Algeria')
                | (africa_forest.country_name == 'Tanzania')
            
                | (africa_forest.country_name == 'Mozambique')]


# In[74]:


africa_forest = africa_forest.rename(columns={'year': 'Year',
                                'country_name': 'Area',
                                'value': 'Forest'})


# In[75]:


del africa_forest['country_code']
africa_forest.Year = pd.to_numeric(africa_forest.Year)
africa_forest.isnull().sum()
africa_forest.info()


# In[]:<br>
# DataFrame with CO2

# In[76]:


africa_co2 = pd.read_csv('co2.csv')
africa_co2 = africa_co2[(africa_co2.country_name == 'Algeria')
          | (africa_co2.country_name == 'Tanzania')
          | (africa_co2.country_name == 'Mozambique')]


# In[77]:


africa_co2 = africa_co2.rename(columns={'year': 'Year',
                          'country_name': 'Area',
                          'value': 'CO2'})


# In[78]:


del africa_co2['country_code']


# In[79]:


africa_co2.isnull().sum()
africa_co2.info()


# In[]:<br>
# DataFrame with GDP

# In[80]:


africa_gdp = pd.read_csv('GDP_percapita.csv')


# In[81]:


africa_gdp = africa_gdp.rename(columns={'Country Name':'Area'})


# In[82]:


africa_gdp = africa_gdp[(africa_gdp.Area == 'Algeria')
          | (africa_gdp.Area == 'Tanzania')
          | (africa_gdp.Area == 'Mozambique')]


# In[83]:


del africa_gdp['Code']
del africa_gdp['Unnamed: 65']


# In[84]:


africa_gdp


# In[]:<br>
# Transform GDP

# In[85]:


africa_gdp_trans = pd.melt(africa_gdp, id_vars='Area')
africa_gdp_trans = africa_gdp_trans.rename(columns={'variable': 'Year',
                              'value': 'GDP_per_capita'})
africa_gdp_trans = africa_gdp_trans.sort_values(by=['Area', 'Year'])
africa_gdp_trans.Year = pd.to_numeric(africa_gdp_trans.Year)


# In[86]:


africa_gdp_trans.Area.unique()


# In[]:<br>
# Join  temperature, forest & co2

# In[87]:


africa_tf = pd.merge(africa_t_c3_trans, africa_forest, on =['Area','Year'], how = 'left')
africa_tfc = pd.merge(africa_tf, africa_co2, on=['Area', 'Year'], how = 'left')
africa_tfcg = pd.merge(africa_tfc, africa_gdp_trans, on =['Area', 'Year'], how = 'left')
africa_tfcg


# In[]:<br>
#  Temperature

# In[88]:


tfcg_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
tfcg_Tanzania = africa_tfcg[(africa_tfcg.Area == 'Tanzania')]
tfcg_Mozambique = africa_tfcg[(africa_tfcg.Area == 'Mozambique')]
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp, label = 'Algieria')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp, label = 'Tanzania')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp, label = 'Mozambik')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103')
plt.title('Zmiany temperatur (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  ALGERIA: Temperature vs GDP

# In[89]:


tfcg_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp, label = 'Algieria_temp')
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.GDP_per_capita, label = 'Algieria_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('AGLIERIA: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  Tanzania: Temperature vs GDP

# In[90]:


tfcg_Tanzania = africa_tfcg[(africa_tfcg.Area == 'Tanzania')]
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp, label = 'Tanzania_temp')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.GDP_per_capita, label = 'Tanzania_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('TANZANIA: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  Mozambique: Temperature vs GDP

# In[91]:


tfcg_Mozambique = africa_tfcg[(africa_tfcg.Area == 'Mozambique')]
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp, label = 'Mozambik_temp')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.GDP_per_capita, label = 'Mozambik_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('MOZAMBIK: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  Forest

# In[92]:


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Forest, label = 'Algieria')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Forest, label = 'Tanzania')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Forest, label = 'Mozambik')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Poziom zalesienia')
plt.title('Zalesienie (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  CO2

# In[93]:


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.CO2, label = 'Algieria')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.CO2, label = 'Tanzania')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.CO2, label = 'Mozambik')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Emisja CO^2')
plt.title('Emisja CO^2 (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  GDP

# In[94]:


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.GDP_per_capita, label = 'Algieria')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.GDP_per_capita, label = 'Tanzania')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.GDP_per_capita, label = 'Mozambik')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('GDP per capita (zmiana)')
plt.title('GDP per capita(1961-2019)')
plt.legend()
plt.show()


# n[]:<br>
# Correlation_Algeria

# In[95]:


corr_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
del corr_Algeria['Area']
del corr_Algeria['Year']


# In[96]:


corr_Algeria = corr_Algeria.corr()
sns.heatmap(corr_Algeria, annot=True)
plt.show()


# n[]:<br>
# Correlation_Tanzania

# In[97]:


corr_Tanzania = africa_tfcg[(africa_tfcg.Area == 'Tanzania')]
del corr_Tanzania['Area']
del corr_Tanzania['Year']


# In[98]:


corr_Tanzania = corr_Tanzania.corr()
sns.heatmap(corr_Tanzania, annot=True)
plt.show()


# n[]:<br>
# Correlation_Mozambique

# In[99]:


corr_Mozambique = africa_tfcg[(africa_tfcg.Area == 'Mozambique')]
del corr_Mozambique['Area']
del corr_Mozambique['Year']


# In[100]:


corr_Mozambique = corr_Mozambique.corr()
sns.heatmap(corr_Mozambique, annot=True)
plt.show()


# #### MATTHIAS

# In[ ]:

# Making individual variable for group purpose working

# In[101]:


mateo = df.copy()


# DataFrame with 5 countries from America (Northern & Central)

# In[102]:


mateo1=optional_1(mateo)


# In[ ]:

# Creating individual Dataframe for countries in Asia

# In[103]:


asia=mateo1[(mateo1.Continent_Code==2) & (mateo1.Months_Code==7020) & (mateo1.Element_Code==7271)]


# In[ ]:

# In[104]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = europe_t_ok.values.T


# In[105]:


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


asia.columns=asia.columns.str.replace('Y', '')
asia['Area'] = asia['Area'].str.replace("'" ,' ')


# In[ ]:

# Dataframe 5 Asia countries

# In[108]:


asia_5=asia[(asia.Area=='Afghanistan') | (asia.Area=='Saudi Arabia') | (asia.Area=='India') |
             (asia.Area=='Republic of Korea') | (asia.Area=='China')]


# In[ ]:

# In[109]:


asia_5.isnull().sum()


# In[ ]:

# X axis from columns 

# In[110]:


x=asia_5.columns[1:].T


# In[ ]:

# Y axis for countries

# In[111]:


y1=asia_5.iloc[0,-59:].values.T # Afganistan
y2=asia_5.iloc[1,-59:].values.T #China
y3=asia_5.iloc[2,-59:].values.T #India                  
y4=asia_5.iloc[3,-59:].values.T #South Korea
y5=asia_5.iloc[4,-59:].values.T #Arabia


# In[ ]:

# In[112]:


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


# #### South America

# In[ ]:

# Making individual variable for group purpose working

# ##### DataFrame with 3 countries from South America 

# ##### Temperature change in 3 countries of South America

# In[18]:


SouthAmerica = df.copy()
SouthAmerica = optional_1(SouthAmerica)
SouthAmerica_whole= SouthAmerica [(SouthAmerica.Continent == 'Shouth America')]
SouthAmerica_temp = SouthAmerica_whole[(SouthAmerica_whole.Area == 'Argentina')| (SouthAmerica_whole.Area == 'Brazil') | (SouthAmerica_whole.Area == 'Peru')]
SouthAmerica_temp = SouthAmerica_temp[(SouthAmerica_temp.Months == 'Meteorological year') & (SouthAmerica_temp.Element == 'Temperature change')]
SouthAmerica_temp

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


SouthAmerica_temp_mdf = pd.melt(SouthAmerica_temp, id_vars='Area')
SouthAmerica_temp_mdf = SouthAmerica_temp_mdf.rename(columns={'variable': 'Year','value': 'Temperature'})
SouthAmerica_temp_mdf= SouthAmerica_temp_mdf.sort_values(by=['Area', 'Year'])
SouthAmerica_temp_mdf


# In[20]:


SouthAmerica_temp_mdf.Year = pd.to_numeric(SouthAmerica_temp_mdf.Year)


# In[ ]:

# Temperature chart

# In[21]:


Argentina_temp = SouthAmerica_temp_mdf [(SouthAmerica_temp_mdf.Area == 'Argentina')]
Brazil_temp = SouthAmerica_temp_mdf[(SouthAmerica_temp_mdf.Area == 'Brazil')]
Peru_temp = SouthAmerica_temp_mdf[(SouthAmerica_temp_mdf.Area == 'Peru')]
plt.plot(Argentina_temp.Year, Argentina_temp.Temperature, 'g*-.', label = 'Argentyna')
plt.plot(Brazil_temp.Year, Brazil_temp.Temperature,'g-',label = 'Brazylia')
plt.plot(Peru_temp.Year, Peru_temp.Temperature, 'g--', label = 'Peru')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.show()


# In[ ]:

# ##### Value of CO2 in 3 countries of South America

# In[22]:


SouthAmerica_CO2 = pd.read_csv('co2.csv')


# In[23]:


del SouthAmerica_CO2['country_code']


# In[24]:


SouthAmerica_CO2 = SouthAmerica_CO2[(SouthAmerica_CO2.country_name == 'Argentina') | (SouthAmerica_CO2.country_name == 'Brazil')
          | (SouthAmerica_CO2.country_name == 'Peru')]
SouthAmerica_CO2


# In[472]:


SouthAmerica_CO2 = SouthAmerica_CO2.rename(columns={'country_name':'Area', 'year':'Year', 'value': 'CO2'})
SouthAmerica_CO2


# In[473]:


SouthAmerica_CO2.Year = pd.to_numeric(SouthAmerica_CO2.Year)


# In[ ]:

# Temperature change and value of CO2

# In[366]:


SouthAmerica_temp_CO2 = pd.merge(SouthAmerica_temp_mdf, SouthAmerica_CO2, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2


# In[ ]:

# Regression - value of CO2

# In[381]:


sns.set_context('paper')
sns.lmplot(data=SouthAmerica_CO2[((SouthAmerica_CO2['Area'] == 'Argentina') 
                                       | (SouthAmerica_CO2['Area'] == 'Brazil')
                                        |(SouthAmerica_CO2['Area'] == 'Peru')) & (SouthAmerica_CO2['Year'])],
            x="Year",
            y="CO2",
            aspect=2.5, 
            hue='Area')
           
plt.show()


# In[ ]:

# ##### GDP per capita in 3 countries of South America

# In[474]:


SouthAmerica_GDP = pd.read_csv('GDP_percapita.csv')


# In[475]:


del SouthAmerica_GDP['Code']
del SouthAmerica_GDP['Unnamed: 65']


# In[476]:


SouthAmerica_GDP = SouthAmerica_GDP.rename(columns={'Country Name':'Area'})


# In[477]:


SouthAmerica_GDP = SouthAmerica_GDP[(SouthAmerica_GDP.Area == 'Argentina') | (SouthAmerica_GDP.Area == 'Brazil')
          | (SouthAmerica_GDP.Area == 'Peru')]
SouthAmerica_GDP


# In[ ]:

# ##### Modified table - GDP per capita

# In[478]:


SouthAmerica_GDP_mdf = pd.melt(SouthAmerica_GDP, id_vars='Area')
SouthAmerica_GDP_mdf = SouthAmerica_GDP_mdf.rename(columns={'variable': 'Year', 'value': 'GDP_per_capita'})
SouthAmerica_GDP_mdf= SouthAmerica_GDP_mdf.sort_values(by=['Area', 'Year'])
SouthAmerica_GDP_mdf


# In[479]:


SouthAmerica_GDP_mdf.Year = pd.to_numeric(SouthAmerica_GDP_mdf.Year)


# In[ ]:

# Regression - GDP per capita

# In[436]:


sns.set_context('paper')
sns.lmplot(data=SouthAmerica_GDP_mdf[((SouthAmerica_GDP_mdf['Area'] == 'Argentina') 
                                       | (SouthAmerica_GDP_mdf['Area'] == 'Brazil')
                                        |(SouthAmerica_GDP_mdf['Area'] == 'Peru')) & (SouthAmerica_GDP_mdf['Year'])],
            x="Year",
            y="GDP_per_capita",
            aspect=2.5, 
            hue='Area')
           
plt.show()


# In[ ]:

# GDP per capita other charts

# In[427]:


sns.set_context('paper')
sns.relplot(data=SouthAmerica_GDP_mdf[(SouthAmerica_GDP_mdf['Area'] == 'Argentina')
                                      | (SouthAmerica_GDP_mdf['Area'] == 'Brazil')
                                       |(SouthAmerica_GDP_mdf['Area'] == 'Peru')],
            x="GDP_per_capita",
            y="Year",
            kind='scatter',
            col='Area')
plt.show()


# In[422]:


Argentina_GDP = SouthAmerica_GDP_mdf [(SouthAmerica_GDP_mdf.Area == 'Argentina')]
Brazil_GDP = SouthAmerica_GDP_mdf[(SouthAmerica_GDP_mdf.Area == 'Brazil')]
Peru_GDP = SouthAmerica_GDP_mdf[(SouthAmerica_GDP_mdf.Area == 'Peru')]
plt.plot(Argentina_GDP.Year, Argentina_GDP.GDP_per_capita, 'g-..', label = 'Argentyna')
plt.plot(Brazil_GDP.Year, Brazil_GDP.GDP_per_capita,'g-',label = 'Brazylia')
plt.bar(Peru_GDP.Year, Peru_GDP.GDP_per_capita, label = 'Peru')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('GDP_per_capita')
plt.title('GDP_per_capita')
plt.legend()
plt.show()


# In[ ]:

# ##### Percent value of forestation in 3 countries of South America

# In[33]:


SouthAmerica_forestation = pd.read_csv('forest.csv')


# In[34]:


del SouthAmerica_forestation['country_code']


# In[35]:


SouthAmerica_forestation = SouthAmerica_forestation[(SouthAmerica_forestation.country_name == 'Argentina') | (SouthAmerica_forestation.country_name == 'Brazil')
          | (SouthAmerica_forestation.country_name == 'Peru')]
SouthAmerica_forestation


# In[36]:


SouthAmerica_forestation = SouthAmerica_forestation.rename(columns={'country_name':'Area', 'year':'Year', 'value': 'Forestation_percent'})
SouthAmerica_forestation


# In[37]:


SouthAmerica_forestation.Year = pd.to_numeric(SouthAmerica_forestation.Year)


# In[ ]:

# Forestation

# In[38]:


Argentina_forestation = SouthAmerica_forestation[(SouthAmerica_forestation.Area == 'Argentina')]
Brazil_forestation = SouthAmerica_forestation[(SouthAmerica_forestation.Area == 'Brazil')]
Peru_forestation = SouthAmerica_forestation[(SouthAmerica_forestation.Area == 'Peru')]
plt.bar(Argentina_forestation.Year, Argentina_forestation.Forestation_percent, label = 'Argentyna')
plt.plot(Brazil_forestation.Year, Brazil_forestation.Forestation_percent,'g-',label = 'Brazylia')
plt.plot(Peru_forestation.Year, Peru_forestation.Forestation_percent, 'g--', label = 'Peru')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Zalesienie_procent')
plt.title('Zalesienie w latach 1990-2019')
plt.legend()
plt.show()


# In[ ]:

# ##### Energy use per capita

# In[485]:


SouthAmerica_energy = pd.read_csv('energy_use_per_capita.csv')


# In[486]:


del SouthAmerica_energy['Code']


# In[487]:


SouthAmerica_energy = SouthAmerica_energy.rename(columns={'Entity':'Area', 
                                     'Primary energy consumption per capita (kWh/person)': 'Energy_use_kWh_per_capita'})


# In[449]:


SouthAmerica_energy = SouthAmerica_energy[(SouthAmerica_energy.Area == 'Argentina') 
                        | (SouthAmerica_energy.Area == 'Brazil')
                            | (SouthAmerica_energy.Area == 'Peru')]
SouthAmerica_energy


# In[488]:


SouthAmerica_energy.Year = pd.to_numeric(SouthAmerica_energy.Year)


# In[ ]:

# Regression - Energy use

# In[453]:


sns.set_context('paper')
sns.lmplot(data=SouthAmerica_energy[((SouthAmerica_energy['Area'] == 'Argentina') 
                                       | (SouthAmerica_energy['Area'] == 'Brazil')
                                        |(SouthAmerica_energy['Area'] == 'Peru')) & (SouthAmerica_energy['Year'])],
            x="Year",
            y="Energy_use_kWh_per_capita",
            aspect=2.5, 
            hue='Area')
           
plt.show()


# In[ ]:

# ##### Urban population (% of total population) in 3 countries of South America

# In[489]:


SouthAmerica_urban = pd.read_csv('share-of-population-urban.csv')


# In[490]:


del SouthAmerica_urban['Code']


# In[491]:


SouthAmerica_urban = SouthAmerica_urban.rename(columns={'Entity':'Area', 
                                     'Urban population (% of total population)': 'Urbanization_rate_percent'})


# In[492]:


SouthAmerica_urban = SouthAmerica_urban[(SouthAmerica_urban.Area == 'Argentina') 
                        | (SouthAmerica_urban.Area == 'Brazil')
                            | (SouthAmerica_urban.Area == 'Peru')]
SouthAmerica_urban


# In[493]:


SouthAmerica_urban.Year = pd.to_numeric(SouthAmerica_urban.Year)


# In[ ]:

# Regression - Urbanization

# In[464]:


sns.set_context('paper')
sns.lmplot(data=SouthAmerica_urban[((SouthAmerica_urban['Area'] == 'Argentina') 
                                       | (SouthAmerica_urban['Area'] == 'Brazil')
                                        |(SouthAmerica_urban['Area'] == 'Peru')) & (SouthAmerica_urban['Year'])],
            x="Year",
            y="Urbanization_rate_percent",
            aspect=2.5, 
            hue='Area')
           
plt.show()


# In[ ]:

# Summarized tabel: Temperature change + CO2 + GDP per capita + Forestation + energy use + urbanization

# In[497]:


SouthAmerica_temp_CO2 = pd.merge(SouthAmerica_temp_mdf, SouthAmerica_CO2, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP = pd.merge(SouthAmerica_temp_CO2, SouthAmerica_GDP_mdf,  on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP_forest = pd.merge(SouthAmerica_temp_CO2_GDP, SouthAmerica_forestation, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP_forest_en = pd.merge(SouthAmerica_temp_CO2_GDP_forest, SouthAmerica_energy, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP_forest_en_urb = pd.merge(SouthAmerica_temp_CO2_GDP_forest_en, SouthAmerica_urban, on =['Area','Year'], how = 'left')
SouthAmerica_temp_CO2_GDP_forest_en_urb


# In[ ]:

# Correlation Argentina

# In[500]:


corr_Argentina = SouthAmerica_temp_CO2_GDP_forest_en_urb[(SouthAmerica_temp_CO2_GDP_forest_en_urb.Area == 'Argentina')]


# In[501]:


del corr_Argentina['Area']
del corr_Argentina['Year']


# In[502]:


corr_Argentina = corr_Argentina.corr()
sns.heatmap(corr_Argentina, annot=True)
plt.show()


# In[ ]:





# In[ ]:

# Correlation Brazil

# In[503]:


corr_Brazil = SouthAmerica_temp_CO2_GDP_forest_en_urb[(SouthAmerica_temp_CO2_GDP_forest_en_urb.Area == 'Brazil')]


# In[504]:


del corr_Brazil['Area']
del corr_Brazil['Year']


# In[505]:


corr_Brazil = corr_Brazil.corr()
sns.heatmap(corr_Brazil, annot=True)
plt.show()


# In[ ]:

# Correlation Peru

# In[506]:


corr_Peru = SouthAmerica_temp_CO2_GDP_forest_en_urb[(SouthAmerica_temp_CO2_GDP_forest_en_urb.Area == 'Peru')]


# In[507]:


del corr_Peru['Area']
del corr_Peru['Year']


# In[508]:


corr_Peru = corr_Peru.corr()
sns.heatmap(corr_Peru, annot=True)
plt.show()


# In[ ]:





# #### Antarctica

# In[ ]:

# Making individual variable for group purpose working

# ##### Temperature change in Antarctica

# In[526]:


Antarctica = df.copy()
Antarctica = optional_1(Antarctica)
Antarctica_temp= Antarctica [(Antarctica.Continent == 'Antarctica')]
Antarctica_temp = Antarctica[(Antarctica.Area == 'Antarctica')]
Antarctica_temp = Antarctica_temp[(Antarctica_temp.Months == 'Meteorological year') & (Antarctica_temp.Element == 'Temperature change')]
Antarctica_temp

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


Antarctica_temp_mdf = pd.melt(Antarctica_temp, id_vars='Area')
Antarctica_temp_mdf = Antarctica_temp_mdf.rename(columns={'variable': 'Year','value': 'Temperature'})
Antarctica_temp_mdf


# In[ ]:

# In[530]:


Antarctica_temp_change = Antarctica_temp_mdf [(Antarctica_temp_mdf.Area == 'Antarctica')]
plt.bar(Antarctica_temp_change.Year, Antarctica_temp_change.Temperature, label = 'Antarktyda')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5) 
plt.xlabel('Rok')
plt.ylabel('Temperatura\u2103')
plt.title('Średnioroczne zmiany temperatury w latach 1961-2019')
plt.legend()
plt.show()


# In[ ]:

# In[ ]:





# In[ ]:





# #### URSULA

# In[ ]:

# Making individual variable for group purpose working

# In[ ]:


urs = df.copy()


# In[ ]:
