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
jaro.columns = jaro.columns.str.replace('Y', '')
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

antarctica_t = jaro1.loc[(jaro1['Area_Code'] == 30) & (
    jaro1['Element_Code'] == 7271) & (jaro1['Months_Code'] == 7020)]
# oceania_t.iloc[:,-59:].isna().sum()
antarctica_t_ok = antarctica_t.iloc[:, -59:]

# In[ ]:


jaro.iloc[:, -59:].isna().sum()

# #### NORTHERN & CENTRAL AMERICA

# In[ ]:


# Making individual variable for group purpose working

# DataFrame with 5 countries from America (Northern & Central)
anna = df.copy()
anna_t = optional_1(anna)
anna_t_full= anna_t [(anna_t.Continent == 'North America')]
anna_t_c5 = anna_t_full[(anna_t_full.Area == 'Canada')
              | (anna_t_full.Area == 'United States of America')
         
              | (anna_t_full.Area == 'Dominican Republic')]
anna_t_c5 = anna_t_c5[(anna_t_c5.Months == 'Meteorological year')
              & (anna_t_c5.Element == 'Temperature change')]
anna_t_c5
# In[ ]:
anna_t_c5.isnull().sum()

# Inp[]:
#Preparing data
anna_t_c5.columns = anna_t_c5.columns.str.replace('Y', '')
del anna_t_c5['Area_Code']
del anna_t_c5['Months_Code']
del anna_t_c5['Months']
del anna_t_c5['Element']
del anna_t_c5['Unit']
del anna_t_c5['Element_Code']
del anna_t_c5['Continent']
del anna_t_c5['Continent_Code']
anna_t_c5

# In[]:
# Transformation table
anna_t_c5_trans = pd.melt(anna_t_c5, id_vars='Area')
anna_t_c5_trans = anna_t_c5_trans.rename(columns={'variable': 'Year',
                              'value': 'Temp'})
anna_t_c5_trans = anna_t_c5_trans.sort_values(by=['Area', 'Year'])
anna_t_c5_trans.Year = pd.to_numeric(anna_t_c5_trans.Year)
anna_t_c5_trans.info()

# In[]:
# DataFrame with Forests
anna_forest = pd.read_csv('forest.csv')
anna_forest = anna_forest[(anna_forest.country_name == 'Canada')
                | (anna_forest.country_name == 'United States')
            
                | (anna_forest.country_name == 'Dominican Republic')]

anna_forest = anna_forest.rename(columns={'year': 'Year',
                                'country_name': 'Area',
                                'value': 'Forest'})

anna_forest.replace(to_replace="United States",
           value="United States of America", inplace=True)

del anna_forest['country_code']
anna_forest.Year = pd.to_numeric(anna_forest.Year)
anna_forest.isnull().sum()
anna_forest

# In[]:
# DataFrame with CO2
anna_co2 = pd.read_csv('co2.csv')
anna_co2 = anna_co2[(anna_co2.country_name == 'Canada')
          | (anna_co2.country_name == 'United States')
          | (anna_co2.country_name == 'Dominican Republic')]

anna_co2 = anna_co2.rename(columns={'year': 'Year',
                          'country_name': 'Area',
                          'value': 'CO2'})

anna_co2.replace(to_replace="United States",
           value="United States of America", inplace=True)

del anna_co2['country_code']

anna_co2.isnull().sum()

anna_co2.info()


# In[]:
# Join  temperature, forest & co2

tf = pd.merge(anna_t_c5_trans, anna_forest, on =['Area','Year'], how = 'left')
tfc = pd.merge(tf, anna_co2, on=['Area', 'Year'], how = 'left')
tfc


# In[]:
## Temperature
tfc_Canada = tfc[(tfc.Area == 'Canada')]
tfc_US = tfc[(tfc.Area == 'United States of America')]
tfc_Dominican = tfc[(tfc.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.Temp, label = 'Kanada')
plt.plot(tfc_US.Year, tfc_US.Temp, label = 'Stany Zjednoczone')
plt.plot(tfc_Dominican.Year, tfc_Dominican.Temp, label = 'Dominikana')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103')
plt.title('Zmiany temperatur (1961-2019)')
plt.legend()
plt.show()

# In[]:
## Forest
tfc_Canada = tfc[(tfc.Area == 'Canada')]
tfc_US = tfc[(tfc.Area == 'United States of America')]
tfc_Dominican = tfc[(tfc.Area == 'Dominican Republic')]
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

# In[]:
## CO2
tfc_Canada = tfc[(tfc.Area == 'Canada')]
tfc_US = tfc[(tfc.Area == 'United States of America')]
tfc_Dominican = tfc[(tfc.Area == 'Dominican Republic')]
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


###### AFRICA
# In[ ]:


# Making individual variable for group purpose working

# DataFrame with 3 countries from Africa
africa = df.copy()
africa_t = optional_1(africa)
africa_t_full= africa_t [(africa_t.Continent == 'Africa')]
africa_t_c3 = africa_t_full[(africa_t_full.Area == 'Algeria')
                | (africa_t_full.Area == 'United Republic of Tanzania')
                | (africa_t_full.Area == 'Mozambique')]
africa_t_c3 = africa_t_c3[(africa_t_c3.Months == 'Meteorological year')
              & (africa_t_c3.Element == 'Temperature change')]
africa_t_c3

# Inp[]:
#Preparing data
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

# In[]:
# Transformation table
africa_t_c3_trans = pd.melt(africa_t_c3, id_vars='Area')
africa_t_c3_trans = africa_t_c3_trans.rename(columns={'variable': 'Year',
                              'value': 'Temp'})
africa_t_c3_trans = africa_t_c3_trans.sort_values(by=['Area', 'Year'])
africa_t_c3_trans.Year = pd.to_numeric(africa_t_c3_trans.Year)
africa_t_c3_trans.info()

# In[]:
# DataFrame with Forests
africa_forest = pd.read_csv('forest.csv')
africa_forest = africa_forest[(africa_forest.country_name == 'Algeria')
                | (africa_forest.country_name == 'Tanzania')
            
                | (africa_forest.country_name == 'Mozambique')]

africa_forest = africa_forest.rename(columns={'year': 'Year',
                                'country_name': 'Area',
                                'value': 'Forest'})


del africa_forest['country_code']
africa_forest.Year = pd.to_numeric(africa_forest.Year)
africa_forest.isnull().sum()
africa_forest.info()

# In[]:
# DataFrame with CO2
africa_co2 = pd.read_csv('co2.csv')
africa_co2 = africa_co2[(africa_co2.country_name == 'Algeria')
          | (africa_co2.country_name == 'Tanzania')
          | (africa_co2.country_name == 'Mozambique')]

africa_co2 = africa_co2.rename(columns={'year': 'Year',
                          'country_name': 'Area',
                          'value': 'CO2'})


del africa_co2['country_code']

africa_co2.isnull().sum()
africa_co2.info()


# In[]:
# DataFrame with GDP
africa_gdp = pd.read_csv('gdp_per_capita_growth.csv')

africa_gdp = africa_gdp.rename(columns={'Country Name':'Area'})

africa_gdp = africa_gdp[(africa_gdp.Area == 'Algeria')
          | (africa_gdp.Area == 'Tanzania')
          | (africa_gdp.Area == 'Mozambique')]

del africa_gdp['Code']
del africa_gdp['Unnamed: 65']

africa_gdp

# In[]:
# Transform GDP

africa_gdp_trans = pd.melt(africa_gdp, id_vars='Area')
africa_gdp_trans = africa_gdp_trans.rename(columns={'variable': 'Year',
                              'value': 'GDP_per_capita'})
africa_gdp_trans = africa_gdp_trans.sort_values(by=['Area', 'Year'])
africa_gdp_trans.Year = pd.to_numeric(africa_gdp_trans.Year)

africa_gdp_trans.Area.unique()



# In[]:
# Join  temperature, forest & co2

africa_tf = pd.merge(africa_t_c3_trans, africa_forest, on =['Area','Year'], how = 'left')
africa_tfc = pd.merge(africa_tf, africa_co2, on=['Area', 'Year'], how = 'left')
africa_tfcg = pd.merge(africa_tfc, africa_gdp_trans, on =['Area', 'Year'], how = 'left')
africa_tfcg

# In[]:
## Temperature
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



# In[]:
## ALGERIA: Temperature vs GDP
tfcg_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp, label = 'Algieria_temp')
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.GDP_per_capita, label = 'Algieria_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('AGLIERIA: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()

# In[]:
## Tanzania: Temperature vs GDP
tfcg_Tanzania = africa_tfcg[(africa_tfcg.Area == 'Tanzania')]
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp, label = 'Tanzania_temp')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.GDP_per_capita, label = 'Tanzania_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('TANZANIA: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()

# In[]:
## Mozambique: Temperature vs GDP
tfcg_Mozambique = africa_tfcg[(africa_tfcg.Area == 'Mozambique')]
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp, label = 'Mozambik_temp')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.GDP_per_capita, label = 'Mozambik_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('MOZAMBIK: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()

# In[]:
## Forest

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

# In[]:
## CO2

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

# In[]:
## GDP

plt.plot(tfcg_Algeria.Year, tfcg_Algeria.GDP_per_capita, label = 'Algieria')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.GDP_per_capita, label = 'Tanzania')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.GDP_per_capita, label = 'Mozambik')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('GDP per capita (zmiana)')
plt.title('GDP per capita(1961-2019)')
plt.legend()
plt.show()

#In[]:
##Correlation_Algeria
africa_tfcg.columns
corr_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
del corr_Algeria['Area']
del corr_Algeria['Year']

corr_Algeria = corr_Algeria.corr()
corr_Algeria
sns.heatmap(corr_Algeria, annot=True)
plt.show()




# #### MATTHIAS

# In[ ]:


# Making individual variable for group purpose working
mateo = df.copy()

# DataFrame with 5 countries from America (Northern & Central)

mateo1=optional_1(mateo)


# In[ ]:

# Creating individual Dataframe for countries in Asia

asia=mateo1[(mateo1.Continent_Code==2) & (mateo1.Months_Code==7020) & (mateo1.Element_Code==7271)]

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

# In[ ]:


# Dataframe 5 Asia countries

asia_5=asia[(asia.Area=='Afghanistan') | (asia.Area=='Saudi Arabia') | (asia.Area=='India') |
             (asia.Area=='Republic of Korea') | (asia.Area=='China')]

# In[ ]:

asia_5.isnull().sum()

# In[ ]:

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