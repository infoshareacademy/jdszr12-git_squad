# # Climate catastrophe<br>
# <br>
# ## Data analysis on changes in average temperatures<br>
# <br>
# Project analyzing data on changes in average temperatures. The `csv` file containing the raw data can be found at [kaggle.com](https://www.kaggle.com/datasets/sevgisarac/temperature-change)

# ### Import

# In[ ]:

# In[25]:


import plotly.offline as pyo
import plotly.express as px
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

# =======================

# In[3]:


el_la = pd.read_csv("El-Nino.csv", sep=';', encoding="Windows-1250")
# el_la


# In[4]:


el_la_to_drop = [1950, 1951, 1952, 1953,
                 1954, 1955, 1956, 1957, 1958, 1959, 1960]

for i in range(len(el_la_to_drop)):
    el_la.drop(el_la[el_la['year'] == el_la_to_drop[i]].index, inplace=True)


# In[5]:


el_la.reset_index(drop=True, inplace=True)
# el_la


# In[6]:


# El Niño
# 0.5 START
# 0.5 Weak
# 1.0 Moderate
# 1.5 Strong
# 2.0 Very Strong
# La Niña
# -0.5 START
# -0.5 Weak
# -1.0 Moderate
# -1.5 Strong
# -2.0 Very Strong


# In[7]:


el_la['mean'] = ''


# In[8]:


for i in range(el_la.shape[0]):
    el_la.iloc[i, -1] = round(np.mean(el_la.loc[i][-13:-1]), 1)


# In[9]:


el_la.drop(['January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December'], axis=1, inplace=True)


# In[10]:


# el_la #.reset_index()


# In[11]:


el_la['area'] = 'El Nino - La Nina'


# In[12]:


el_la_p = el_la.pivot(index='area', columns='year', values='mean')

el_la_p = el_la_p.reset_index()


# In[13]:


el_la_p

# ### ================================

# In[]:


temp = pd.read_csv(
    "Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="Windows-1250")


# In[]:


temp['Months'].unique()


# In[]:


temp.columns = temp.columns.str.replace('Y', '')
temp.drop('Unit', axis=1, inplace=True)
temp = temp.rename(columns={"Area Code": "area_code",
                            "Area": "area",
                            "Months Code": "months_code",
                            "Months": "months",
                            "Element Code": "element_code",
                            "Element": "element"})
# temp['Months'] = temp['Months'].replace("Dec–Jan–Feb", "Winter")
# temp['Months'] = temp['Months'].replace("Mar–Apr–May", "Spring")
# temp['Months'] = temp['Months'].replace("Jun–Jul–Aug", "Summer")
# temp['Months'] = temp['Months'].replace("Sep–Oct–Nov", "Autumn")


# In[]:


# Select the row that contains USSR in the area column
ussr_row = temp.loc[temp['area'] == 'USSR']
# ussr_row.loc[:,'1961':'2019'].isna()


# In[]:


# for loop array
ussr_area = ['Armenia', 'Azerbaijan', 'Belarus', 'Estonia',
             'Georgia', 'Kazakhstan', 'Kyrgyzstan', 'Latvia',
             'Lithuania', 'Republic of Moldova', 'Russian Federation',
             'Tajikistan', 'Turkmenistan', 'Ukraine', 'Uzbekistan']

# Check NAN, from-to which year to update from ussr_row variable
# for i in range(len(ussr_area)):
#     print(temp.loc[temp['area'] == ussr_area[i]].loc[:,'1961':'2019'].isna())


# Non loop verision
# armenia_row = temp.loc[temp['area'] == 'Armenia']
# armenia_row.loc[:,'1961':'2019'].isna()


# In[]:


# Copy the non-NAN values from USSR row to appropriate NAN value
# in years columns in appropriate country-area row (from ussr_area array)
for i in range(len(ussr_area)):
    temp.loc[temp['area'] == ussr_area[i],
             '1961':'1991'] = ussr_row.loc[:, '1961':'1991'].values

# Non loop verision
# temp.loc[temp['area'] == 'Armenia', '1961':'1991'] = ussr_row.loc[:,'1961':'1991'].values


# In[]:


# Select the row that contains Belgium-Luxembourg in the area column
belgium_lux_row = temp.loc[temp['area'] == 'Belgium-Luxembourg']
# belgium_lux_row.loc[:,'1961':'2019'].isna()


# In[]:


# for loop array
bel_lux_area = ['Belgium', 'Luxembourg']

# Check NAN, from-to which year to update from bel_lux_area variable
# for i in range(len(bel_lux_area)):
#     print(temp.loc[temp['area'] == bel_lux_area[i]].loc[:,'1961':'2019'].isna())


# In[]:


# Copy the non-NAN values from Belgium-Luxembourg row to appropriate NAN value
# in years columns in appropriate country-area row (from bel_lux_area array)
for i in range(len(bel_lux_area)):
    temp.loc[temp['area'] == bel_lux_area[i],
             '1961':'1999'] = belgium_lux_row.loc[:, '1961':'1999'].values


# In[]:


# Select the row that contains Czechoslovakia in the area column
czechoslovakia_row = temp.loc[temp['area'] == 'Czechoslovakia']
# czechoslovakia_row.loc[:,'1961':'2019'].isna()


# In[]:


# for loop array
czechoslovakia_area = ['Czechia', 'Slovakia']

# Check NAN, from-to which year to update from czechoslovakia_area variable
# for i in range(len(czechoslovakia_area)):
#     print(temp.loc[temp['area'] == czechoslovakia_area[i]].loc[:,'1961':'2019'].isna())


# In[]:


# Copy the non-NAN values from Czechoslovakia row to appropriate NAN value
# in years columns in appropriate country-area row (from czechoslovakia_area array)
for i in range(len(czechoslovakia_area)):
    temp.loc[temp['area'] == czechoslovakia_area[i],
             '1961':'1992'] = czechoslovakia_row.loc[:, '1961':'1992'].values


# In[]:


# Select the row that contains Yugoslav SFR in the area column
yugoslav_row = temp.loc[temp['area'] == 'Yugoslav SFR']
# yugoslav_row.loc[:,'1961':'2019'].isna()


# In[]:


# for loop array
yugoslav_area = ['Croatia', 'Slovenia', 'Bosnia and Herzegovina',
                 'North Macedonia', 'Serbia and Montenegro']

# Check NAN, from-to which year to update from yugoslav_area variable
# for i in range(len(yugoslav_area)):
#     print(temp.loc[temp['area'] == yugoslav_area[i]].loc[:,'1961':'2019'].isna())


# In[]:


# Copy the non-NAN values from Yugoslav SFR row to appropriate NAN value
# in years columns in appropriate country-area row (from yugoslav_area array)
for i in range(len(yugoslav_area)):
    temp.loc[temp['area'] == yugoslav_area[i],
             '1961':'1991'] = yugoslav_row.loc[:, '1961':'1991'].values


# In[]:


# Select the row that contains Serbia and Montenegro in the area column
s_m_row = temp.loc[temp['area'] == 'Serbia and Montenegro']
# s_m_row.loc[:,'1961':'2019'].isna()


# In[]:


# for loop array
s_m_area = ['Montenegro', 'Serbia']

# Check NAN, from-to which year to update from s_m_area variable
# for i in range(len(s_m_area)):
#     print(temp.loc[temp['area'] == s_m_area[i]].loc[:,'1961':'2019'].isna())


# In[]:


# Copy the non-NAN values from Serbia and Montenegro row to appropriate NAN value
# in years columns in appropriate country-area row (from s_m_area array)
for i in range(len(s_m_area)):
    temp.loc[temp['area'] == s_m_area[i],
             '1961':'2005'] = s_m_row.loc[:, '1961':'2005'].values


# In[]:


# Select the row that contains Sudan (former) in the area column
sudan_f_row = temp.loc[temp['area'] == 'Sudan (former)']
# sudan_f_row.loc[:,'1961':'2019'].isna()


# In[]:


# for loop array
sudan_f_area = ['Sudan', 'South Sudan']

# Check NAN, from-to which year to update from sudan_f_area variable
# for i in range(len(sudan_f_area)):
#     print(temp.loc[temp['area'] == sudan_f_area[i]].loc[:,'1961':'2019'].isna())


# In[]:


# Copy the non-NAN values from Sudan (former) row to appropriate NAN value
# in years columns in appropriate country-area row (from sudan_f_area array)
for i in range(len(sudan_f_area)):
    temp.loc[temp['area'] == sudan_f_area[i],
             '1961':'2010'] = sudan_f_row.loc[:, '1961':'2010'].values


# In[]:


# Select the row that contains Ethiopia PDR in the area column
ethiopia_pdr_row = temp.loc[temp['area'] == 'Ethiopia PDR']
# ethiopia_pdr_row.loc[:,'1961':'2019'].isna()


# In[]:


# Check NAN, from-to which year to update
#temp.loc[temp['area'] == 'Ethiopia'].loc[:,'1961':'2019'].isna()


# In[]:


# Copy the non-NAN values from Ethiopia PDR row to appropriate NAN value in years columns in Ethiopia row
temp.loc[temp['area'] == 'Ethiopia',
         '1961':'1992'] = ethiopia_pdr_row.loc[:, '1961':'1992'].values


# In[]:


temp_c_to_drop = ['USSR', 'Belgium-Luxembourg', 'Czechoslovakia',
                  'Yugoslav SFR', 'Serbia and Montenegro', 'Sudan (former)', 'Ethiopia PDR']

for i in range(len(temp_c_to_drop)):
    temp.drop(temp[temp['area'] == temp_c_to_drop[i]].index, inplace=True)


# In[]:


for i in range(temp.shape[0]):
    temp.iloc[i, -59:] = temp.iloc[i, -59:].bfill(axis='rows')
    temp.iloc[i, -59:] = temp.iloc[i, -59:].ffill(axis='rows')


# In[]:


# del in temp, co2, forest, gdp, urban pop
t_drop_rows = ['Anguilla', 'Belgium-Luxembourg', 'China mainland', 'China Taiwan Province of',
               'Christmas Island', 'Cocos (Keeling) Islands', 'Cook Islands', 'Czechoslovakia',
               'Ethiopia PDR', 'Falkland Islands (Malvinas)', 'French Guiana',
               'French Southern and Antarctic Territories', 'Guadeloupe', 'Holy See', 'Martinique',
               'Mayotte', 'Midway Island', 'Montserrat', 'Netherlands Antilles (former)', 'Niue',
               'Norfolk Island', 'Pitcairn Islands', 'Réunion', 'Saint Helena Ascension and Tristan da Cunha',
               'Saint Pierre and Miquelon', 'Serbia and Montenegro', 'South Georgia and the South Sandwich Islands',
               'Sudan (former)', 'Svalbard and Jan Mayen Islands', 'Tokelau', 'USSR', 'Wake Island',
               'Wallis and Futuna Islands', 'Yugoslav SFR']

for i in range(len(t_drop_rows)):
    temp.drop(temp[temp['area'] == t_drop_rows[i]].index, inplace=True)


# In[]:


t_rename = {'Bolivia (Plurinational State of)': 'Bolivia',
            'Bosnia and Herzegovina': 'Bosnia and Herz.',
            'Brunei Darussalam': 'Brunei',
            'Caribbean': 'Caribbean small states',
            'Central African Republic': 'Central African Rep.',
            'Congo': 'Congo',
            'Côte d\'Ivoire': 'Côte d\'Ivoire',
            'Democratic Republic of the Congo': 'Dem. Rep. Congo',
            'Dominican Republic': 'Dominican Rep.',
            'Equatorial Guinea': 'Eq. Guinea',
            'Eswatini': 'eSwatini',
            'Falkland Islands (Malvinas)': 'Falkland Is.',
            'French Southern and Antarctic Territories': 'Fr. S. Antarctic Lands',
            'Iran (Islamic Republic of)': 'Iran',
            'Lao People\'s Democratic Republic': 'Laos',
            'Micronesia (Federated States of)': 'Micronesia Fed. Sts.',
            'Republic of Moldova': 'Moldova',
            'Democratic People\'s Republic of Korea': 'North Korea',
            'Pacific Islands Trust Territory': 'Pacific island small states',
            'Réunion': 'Reunion',
            'Russian Federation': 'Russia',
            'South Sudan': 'S. Sudan',
            'Slovakia': 'Slovakia',
            'Solomon Islands': 'Solomon Is.',
            'Republic of Korea': 'South Korea',
            'Saint Kitts and Nevis': 'St. Kitts and Nevis',
            'Saint Lucia': 'St. Lucia',
            'Saint Vincent and the Grenadines': 'St. Vincent and the Grenadines',
            'Syrian Arab Republic': 'Syria',
            'China Taiwan Province of': 'Taiwan',
            'United Republic of Tanzania': 'Tanzania',
            'Venezuela (Bolivarian Republic of)': 'Venezuela',
            'Viet Nam': 'Vietnam',
            'United States Virgin Islands': 'Virgin Islands (U.S.)'}

temp['area'] = temp['area'].replace(t_rename)

# =====================================================================================

# In[]:


# El Nino / La Nina (1961-2019)
el_la_plot = el_la_p.iloc[:, -59:]

# Whole World temperatures (1961-2019)
world_t = temp.loc[(temp['area_code'] == 5000) & (
    temp['element_code'] == 7271) & (temp['months_code'] == 7020)]

# world_t.iloc[:,-59:].isna().sum()
world_t_ok = world_t.iloc[:, -59:]


# In[]:


x = world_t_ok.columns
y1 = world_t_ok.values.T
el_la_row = el_la_plot.iloc[0]  # get first row
el_la_array = el_la_row.to_numpy()  # convert row to numpy array
y2 = el_la_array.T
plt.plot(x, y1, label='World')
plt.plot(x, y2, label='El Nino / La Nina')
plt.axhline(y=0.0, color='r', linestyle='-')
ymax = np.max(y2)
ymin = np.min(y2)
for i in range(len(y2)):
    if y2[i] == ymax:
        plt.axvspan(x[i], x[i+1], alpha=0.2, color='red')
    elif y2[i] == ymin:
        plt.axvspan(x[i], x[i+1], alpha=0.2, color='blue')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()

# =====================================================================================


# In[84]:


pyo.init_notebook_mode()

country_iso3 = pd.read_csv(
    'https://raw.githubusercontent.com/infoshareacademy/jdszr12-git_squad/main/py_projekt/FAOSTAT_data_11-24-2020.csv', encoding="UTF-8")


# In[85]:


country_iso3.columns


# In[86]:


country_iso3.drop(columns=['Country Code', 'M49 Code',
                  'ISO2 Code', 'Start Year', 'End Year'], inplace=True)
country_iso3.rename(
    columns={'Country': 'country_name', 'ISO3 Code': 'country_code'}, inplace=True)


# In[87]:


iso3_drop_rows = ['Anguilla', 'Belgium-Luxembourg', 'Bermuda', 'China mainland', 'China Taiwan Province of',
                  'Christmas Island', 'Cocos (Keeling) Islands', 'Cook Islands', 'Czechoslovakia',  'Ethiopia PDR',
                  'Falkland Islands (Malvinas)', 'French Guiana', 'French Southern Territories', 'Guadeloupe',
                  'Guam', 'Holy See', 'Martinique', 'Mayotte', 'Midway Island', 'Montserrat',
                  'Netherlands Antilles (former)', 'Niue', 'Norfolk Island', 'Pitcairn', 'Réunion',
                  'Saint Helena, Ascension and Tristan da Cunha', 'Saint Pierre and Miquelon', 'Serbia and Montenegro',
                  'Sudan (former)', 'Svalbard and Jan Mayen Islands', 'Tokelau', 'USSR', 'Wake Island',
                  'Wallis and Futuna Islands', 'Yugoslav SFR', 'Africa', 'Åland Islands', 'Americas',
                  'Annex I countries', 'Antarctic Region', 'Asia', 'Australia and New Zealand',
                  'Bonaire, Sint Eustatius and Saba', 'Bouvet Island', 'British Indian Ocean Territory', 'Caribbean',
                  'Central America', 'Central Asia', 'Central Asia and Southern Asia', 'China, mainland',
                  'East Asia (excluding China)', 'Eastern Africa', 'Eastern Asia', 'Eastern Asia and South-eastern Asia',
                  'Eastern Europe', 'Europe', 'European Union (27)', 'European Union (28)', 'Germany Fr', 'Germany Nl',
                  'Heard and McDonald Islands', 'High-income economies', 'Jersey', 'Johnston Island',
                  'Land Locked Developing Countries', 'Latin America and the Caribbean', 'Least Developed Countries',
                  'Low income economies', 'Low Income Food Deficit Countries', 'Lower-middle-income economies',
                  'Melanesia', 'Micronesia', 'Middle Africa', 'Net Food Importing Developing Countries',
                  'Non-Annex I countries', 'North Africa (excluding Sudan)', 'Northern Africa', 'Northern America',
                  'Northern America and Europe', 'Northern Europe', 'Northern Mariana Islands', 'Oceania',
                  'Oceania excluding Australia and New Zealand', 'OECD', 'Pacific Islands Trust Territory', 'Polynesia',
                  'Saint Barthélemy', 'Saint-Martin (French part)', 'Serbia (excluding Kosovo)',
                  'Small Island Developing States', 'South America', 'South Asia (excluding India)',
                  'South Georgia and the South Sandwich Islands', 'South-eastern Asia', 'Southern Africa', 'Southern Asia',
                  'Southern Europe', 'Sub-Saharan Africa', 'Sub-Saharan Africa (including Sudan)',
                  'United States Minor Outlying Islands', 'Upper-middle-income economies', 'Western Africa', 'Western Asia',
                  'Western Asia and Northern Africa', 'Western Europe', 'Western Sahara', 'World', 'Yemen Ar Rp', 'Yemen Dem']

for i in range(len(iso3_drop_rows)):
    country_iso3.drop(
        country_iso3[country_iso3['country_name'] == iso3_drop_rows[i]].index, inplace=True)


# In[88]:


df_temp = temp.copy()


# In[89]:


df_temp = df_temp.loc[df_temp.element == 'Temperature change']
df_temp.drop(columns=['area_code', 'months_code',
             'element_code', 'element'], inplace=True)
df_temp.rename(columns={'area': 'country_name'}, inplace=True)


# In[90]:


df_temp_drop_rows = ['Africa', 'Americas', 'Annex I countries', 'Asia', 'Australia and New Zealand',
                     'Caribbean small states', 'Central America', 'Central Asia', 'Eastern Africa', 'Eastern Asia',
                     'Eastern Europe', 'Europe', 'European Union', 'Land Locked Developing Countries', 'Least Developed Countries',
                     'Low Income Food Deficit Countries', 'Melanesia', 'Micronesia', 'Middle Africa',
                     'Net Food Importing Developing Countries', 'Non-Annex I countries', 'Northern Africa',
                     'Northern America', 'Northern Europe', 'Oceania', 'OECD', 'Polynesia', 'Small Island Developing States',
                     'South America', 'South-Eastern Asia', 'Southern Africa', 'Southern Asia', 'Southern Europe',
                     'Western Africa', 'Western Asia', 'Western Europe', 'Western Sahara', 'World', 'Caribbean',
                     'China mainland', 'Pacific Islands Trust Territory', 'South Georgia and the South Sandwich Islands']

for i in range(len(df_temp_drop_rows)):
    df_temp.drop(df_temp[df_temp['country_name'] ==
                 df_temp_drop_rows[i]].index, inplace=True)


# In[91]:


df_temp_rename = {'Bolivia': 'Bolivia (Plurinational State of)',
                  'Bosnia and Herz.': 'Bosnia and Herzegovina',
                  'Brunei': 'Brunei Darussalam',
                  'Central African Rep.': 'Central African Republic',
                  'Taiwan': 'China, Taiwan Province of',
                  'China Hong Kong SAR': 'China, Hong Kong SAR',
                  'China Macao SAR': 'China, Macao SAR',
                  'Dem. Rep. Congo': 'Democratic Republic of the Congo',
                  'Dominican Rep.': 'Dominican Republic',
                  'Eq. Guinea': 'Equatorial Guinea',
                  'eSwatini': 'Eswatini',
                  'Falkland Is.': 'Falkland Islands (Malvinas)',
                  'Fr. S. Antarctic Lands': 'French Southern Territories',
                  'Iran': 'Iran (Islamic Republic of)',
                  'Laos': 'Lao People\'s Democratic Republic',
                  'Micronesia Fed. Sts.': 'Micronesia (Federated States of)',
                  'Republic of Moldova': 'Moldova',
                  'North Korea': 'Democratic People\'s Republic of Korea',
                  'Pacific Islands Trust Territory': 'Pacific island small states',
                  'Reunion': 'Réunion',
                  'Russia': 'Russian Federation',
                  'S. Sudan': 'South Sudan',
                  'Solomon Is.': 'Solomon Islands',
                  'South Korea': 'Republic of Korea',
                  'St. Kitts and Nevis': 'Saint Kitts and Nevis',
                  'St. Lucia': 'Saint Lucia',
                  'St. Vincent and the Grenadines': 'Saint Vincent and the Grenadines',
                  'Syria': 'Syrian Arab Republic',
                  'Tanzania': 'United Republic of Tanzania',
                  'Venezuela': 'Venezuela (Bolivarian Republic of)',
                  'Vietnam': 'Viet Nam',
                  'United Kingdom': 'United Kingdom of Great Britain and Northern Ireland',
                  'Virgin Islands (U.S.)': 'United States Virgin Islands'}

df_temp['country_name'] = df_temp['country_name'].replace(df_temp_rename)


# In[92]:


df_temp.reset_index(drop=True, inplace=True)
df_temp


# In[93]:


df_temp = pd.merge(df_temp, country_iso3, how='inner', on='country_name')


# In[94]:


# df_temp


# In[95]:


df_temp = df_temp.melt(id_vars=["country_code", "country_name", "months"],
                       value_vars=[str(n) for n in range(1961, 2019+1)],
                       var_name="years",
                       value_name="temp_changes")


# In[96]:


m_year = df_temp.months == 'Meteorological year'

year_var = df_temp.loc[m_year, [
    'country_code', 'country_name', 'years', 'temp_changes']].reset_index(drop=True)

fig = px.choropleth(
    year_var,
    locations='country_code',
    animation_frame='years',
    color='temp_changes',
    color_continuous_scale='balance',
    range_color=[-2, 2.5],
    hover_name='country_name',
    hover_data=dict(country_code=None),
    labels=dict(
        years='Year',
        temp_changes="Temperature Change (\u2103)"))
fig.update_layout(
    title='World Temperature Change from 1961 to 2019',
    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='top',
    dragmode=False,
    width=1000,
    height=600)
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 250
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 80
fig.show()


# #### NORTHERN & CENTRAL AMERICA

# In[ ]:

# Making individual variable for group purpose working

# DataFrame with 5 countries from America (Northern & Central

# In[40]:


NAmerica = df.copy()
NAmerica = optional_1(NAmerica)
NAmerica_full = NAmerica[(NAmerica.Continent == 'North America')]
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


NAmerica_gdp = NAmerica_gdp.rename(columns={'Country Name': 'Area'})


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


NAmerica_tf = pd.merge(NAmerica_trans, NAmerica_forest,
                       on=['Area', 'Year'], how='left')
NAmerica_tfc = pd.merge(NAmerica_tf, NAmerica_co2, on=[
                        'Area', 'Year'], how='left')
NAmerica_tfcg = pd.merge(NAmerica_tfc, NAmerica_gdp_trans, on=[
                         'Area', 'Year'], how='left')
NAmerica_tfcg


# In[]:<br>
#  Temperature

# In[61]:


tfc_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
tfc_US = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
tfc_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.Temp, label='Kanada', color='#00035b')
plt.plot(tfc_US.Year, tfc_US.Temp, label='Stany Zjednoczone', color='#0343df')
plt.plot(tfc_Dominican.Year, tfc_Dominican.Temp,
         label='Dominikana', color='#a2cffe')
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
plt.plot(tfc_Canada.Year, tfc_Canada.Forest, label='Kanada', color='#00035b')
plt.plot(tfc_US.Year, tfc_US.Forest,
         label='Stany Zjednoczone', color='#0343df')
plt.plot(tfc_Dominican.Year, tfc_Dominican.Forest,
         label='Dominikana', color='#a2cffe')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Poziom zalesienia')
plt.title('Zalesienie (1990-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  CO2

# In[63]:


tfc_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
tfc_US = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
tfc_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
plt.plot(tfc_Canada.Year, tfc_Canada.CO2, label='Kanada', color='#00035b')
plt.plot(tfc_US.Year, tfc_US.CO2, label='Stany Zjednoczone', color='#0343df')
plt.plot(tfc_Dominican.Year, tfc_Dominican.CO2,
         label='Dominikana', color='#a2cffe')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Emisja CO^2')
plt.title('Emisja CO^2 (1961-2019)')
plt.legend()
plt.show()

# In[]:
# Kanada: temp vs CO2

fig, ax1 = plt.subplots()

ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#00035b')
ax1.plot(tfc_Canada.Year, tfc_Canada.Temp, label='Kanada', color='#00035b')
ax1.tick_params(axis='y', labelcolor='#00035b')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# we already handled the x-label with ax1
ax2.set_ylabel('CO^2', color='black')
ax2.plot(tfc_Canada.Year, tfc_Canada.CO2, label='Kanada', color='black')
ax2.tick_params(axis='y', labelcolor='black')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Kanada: zmiany temperatury vs emisja CO^2 (1961-2019)')

plt.show()

# In[]:
# USA: temp vs CO2

fig, ax1 = plt.subplots()

ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#0343df')
ax1.plot(tfc_US.Year, tfc_US.Temp, label='USA', color='#0343df')
ax1.tick_params(axis='y', labelcolor='#0343df')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# we already handled the x-label with ax1
ax2.set_ylabel('CO^2', color='black')
ax2.plot(tfc_US.Year, tfc_US.CO2, label='USA', color='black')
ax2.tick_params(axis='y', labelcolor='black')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('USA: zmiany temperatury vs emisja CO^2 (1961-2019)')

plt.show()


# In[]:
# Dominikana: temp vs CO2

fig, ax1 = plt.subplots()

ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#a2cffe')
ax1.plot(tfc_Dominican.Year, tfc_Dominican.Temp,
         label='Dominikana', color='#a2cffe')
ax1.tick_params(axis='y', labelcolor='#a2cffe')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


# we already handled the x-label with ax1
ax2.set_ylabel('CO^2', color='black')
ax2.plot(tfc_Dominican.Year, tfc_Dominican.CO2,
         label='Dominikana', color='black')
ax2.tick_params(axis='y', labelcolor='black')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Dominikana: zmiany temperatury vs emisja CO^2 (1961-2019)')

plt.show()


# n[]:<br>
# Correlation_Canada

# In[64]:


corr_Canada = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Canada')]
del corr_Canada['Area']
del corr_Canada['Year']


# In[65]:


corr_Canada = corr_Canada.corr()
sns.heatmap(corr_Canada, annot=True)
plt.show()


# n[]:<br>
# Correlation_USA

# In[66]:


corr_USA = NAmerica_tfcg[(NAmerica_tfcg.Area == 'United States of America')]
del corr_USA['Area']
del corr_USA['Year']


# In[67]:


corr_USA = corr_USA.corr()
sns.heatmap(corr_USA, annot=True)
plt.show()


# n[]:<br>
# Correlation_Dominican

# In[68]:


corr_Dominican = NAmerica_tfcg[(NAmerica_tfcg.Area == 'Dominican Republic')]
del corr_Dominican['Area']
del corr_Dominican['Year']


# In[69]:


corr_Dominican = corr_Dominican.corr()
sns.heatmap(corr_Dominican, annot=True)
plt.show()


# #### AFRICA<br>
# In[ ]:

# Making individual variable for group purpose working

# DataFrame with 3 countries from Africa

# In[70]:


africa = df.copy()
africa_t = optional_1(africa)
africa_t_full = africa_t[(africa_t.Continent == 'Africa')]
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


africa_gdp = africa_gdp.rename(columns={'Country Name': 'Area'})


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


africa_tf = pd.merge(africa_t_c3_trans, africa_forest,
                     on=['Area', 'Year'], how='left')
africa_tfc = pd.merge(africa_tf, africa_co2, on=['Area', 'Year'], how='left')
africa_tfcg = pd.merge(africa_tfc, africa_gdp_trans,
                       on=['Area', 'Year'], how='left')
africa_tfcg


# In[]:<br>
#  Temperature

# In[88]:


tfcg_Algeria = africa_tfcg[(africa_tfcg.Area == 'Algeria')]
tfcg_Tanzania = africa_tfcg[(africa_tfcg.Area == 'Tanzania')]
tfcg_Mozambique = africa_tfcg[(africa_tfcg.Area == 'Mozambique')]
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp,
         label='Algieria', color='#000000')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp,
         label='Tanzania', color='#929591')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp,
         label='Mozambik', color='#d8dcd6')
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
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp, label='Algieria_temp')
plt.plot(tfcg_Algeria.Year, tfcg_Algeria.GDP_per_capita, label='Algieria_GDP')
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
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp, label='Tanzania_temp')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.GDP_per_capita, label='Tanzania_GDP')
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
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp, label='Mozambik_temp')
plt.plot(tfcg_Mozambique.Year,
         tfcg_Mozambique.GDP_per_capita, label='Mozambik_GDP')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Temperatura \u2103 \n GDP per capita')
plt.title('MOZAMBIK: Zmiany temperatur vs GDP per capita (1961-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  Forest

# In[92]:


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.Forest,
         label='Algieria', color='#000000')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Forest,
         label='Tanzania', color='#929591')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Forest,
         label='Mozambik', color='#d8dcd6')
plt.yscale('log')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('Poziom zalesienia')
plt.title('Zalesienie (1990-2019)')
plt.legend()
plt.show()


# In[]:<br>
#  CO2

# In[93]:


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.CO2,
         label='Algieria', color='#000000')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.CO2,
         label='Tanzania', color='#929591')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.CO2,
         label='Mozambik', color='#d8dcd6')
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


plt.plot(tfcg_Algeria.Year, tfcg_Algeria.GDP_per_capita,
         label='Algieria', color='#000000')
plt.plot(tfcg_Tanzania.Year, tfcg_Tanzania.GDP_per_capita,
         label='Tanzania', color='#929591')
plt.plot(tfcg_Mozambique.Year, tfcg_Mozambique.GDP_per_capita,
         label='Mozambik', color='#d8dcd6')
plt.subplots_adjust(left=-0.5)
plt.xlabel('Rok')
plt.ylabel('GDP per capita (zmiana)')
plt.title('GDP per capita(1961-2019)')
plt.legend()
plt.show()

# In[]:
# Algeria: temp vs CO2

fig, ax1 = plt.subplots()

ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#000000')
ax1.plot(tfcg_Algeria.Year, tfcg_Algeria.Temp,
         label='Algeria', color='#000000')
ax1.tick_params(axis='y', labelcolor='#000000')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


ax2.set_ylabel('CO^2', color='red')  # we already handled the x-label with ax1
ax2.plot(tfcg_Algeria.Year, tfcg_Algeria.CO2, label='Algeria', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Algeria: zmiany temperatury vs emisja CO^2 (1961-2019)')

plt.show()


# In[]:
# Tanzania: temp vs CO2

fig, ax1 = plt.subplots()

ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#929591')
ax1.plot(tfcg_Tanzania.Year, tfcg_Tanzania.Temp,
         label='Tanzania', color='#929591')
ax1.tick_params(axis='y', labelcolor='#929591')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


ax2.set_ylabel('CO^2', color='red')  # we already handled the x-label with ax1
ax2.plot(tfcg_Tanzania.Year, tfcg_Tanzania.CO2, label='Tanzania', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Tanzania: zmiany temperatury vs emisja CO^2 (1961-2019)')

plt.show()

# In[]:
# Mozambik: temp vs CO2

fig, ax1 = plt.subplots()

ax1.set_xlabel('Rok')
ax1.set_ylabel('Temperatura', color='#d8dcd6')
ax1.plot(tfcg_Mozambique.Year, tfcg_Mozambique.Temp,
         label='Mozambik', color='#d8dcd6')
ax1.tick_params(axis='y', labelcolor='#d8dcd6')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


ax2.set_ylabel('CO^2', color='red')  # we already handled the x-label with ax1
ax2.plot(tfcg_Mozambique.Year, tfcg_Mozambique.CO2,
         label='Mozambik', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Mozambik: zmiany temperatury vs emisja CO^2 (1961-2019)')

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


# #### ASIA

# In[ ]:

# Making individual variable for group purpose working

#In[]:


mateo = df.copy()


# DataFrame with 5 countries from America (Northern & Central)

#In[]:


mateo1 = optional_1(mateo)


# In[ ]:

# Creating individual Dataframe for countries in Asia

#In[]:


asia = mateo1[(mateo1.Continent_Code == 2) & (
    mateo1.Months_Code == 7020) & (mateo1.Element_Code == 7271)]


# In[ ]:

#In[]:


get_ipython().run_line_magic('matplotlib', 'inline')
x = world_t_ok.columns
y1 = world_t_ok.values.T
y2 = asia_t_ok.values.T

#In[ ]:

x = x.astype(np.int64)

# Smoothing plost for Asia and world
#In[]:

bspl_w = splrep(x,y1,s=4)   
bspl_w_y1 = splev(x,bspl_w)

bspl_a = splrep(x,y2,s=4)   
bspl_a_y2 = splev(x,bspl_a)
#In[]:


plt.plot(x, bspl_w_y1, label='World')
plt.plot(x, bspl_a_y2, label='Europe')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()


# Droping unnecessary columns

#In[]:


asia = asia.drop(columns=['Continent',
                          'Continent_Code',
                          'Area_Code',
                          'Months_Code',
                          'Months',
                          'Element_Code',
                          'Element',
                          'Unit'])


# In[ ]:

# Repalcing unnecessary marks with space

#In[]:


asia.columns = asia.columns.str.replace('Y', '')
asia['Area'] = asia['Area'].str.replace("'", ' ')


# In[ ]:

# Dataframe 3 Asia countries

#In[]:


asia_3 = asia[(asia.Area == 'India') | (asia.Area == 'Philippines') |
               (asia.Area == 'China')]


# In[ ]:

#In[]:


asia_3.isnull().sum()


# In[ ]:

# Transform teble

#In[]:


asia_3_tmp = pd.melt(asia_3, id_vars='Area')


# In[ ]:

# Renameing columns

#In[]:


asia_3_tmp = asia_3_tmp.rename(columns={'variable': 'Year',
                                        'value': 'Temp'})


#In[ ]:

asia_3_tmp = asia_3_tmp.sort_values(by=['Area', 'Year'])

# Making x variables
#In[]:

asia_3_tmp.Year = pd.to_numeric(asia_3_tmp.Year)


#In[]:

x_mat = asia_3_tmp.Year.unique()

# Making y variables for 3 Asia countries

# In[]:

y1_tmp = asia_3_tmp[asia_3_tmp.Area == 'China'].iloc[:, 2].values.T
y2_tmp = asia_3_tmp[asia_3_tmp.Area == 'India'].iloc[:, 2].values.T
y3_tmp = asia_3_tmp[asia_3_tmp.Area == 'Philippines'].iloc[:, 2].values.T

# Preparing plots for smoothing

# In[]:

bspl1 = splrep(x_mat, y1_tmp, s=4)
bspl_y1 = splev(x_mat, bspl1)

bspl2 = splrep(x_mat, y2_tmp, s=4)
bspl_y2 = splev(x_mat, bspl2)

bspl3 = splrep(x_mat, y3_tmp, s=12)
bspl_y3 = splev(x_mat, bspl3)

#In[ ]:

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x_mat, bspl_y1, label='Chiny')
plt.plot(x_mat, bspl_y2, label='Indie')
plt.plot(x_mat, bspl_y3, label='Filipiny')


plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show()

# CO2 table for Asia
#In[]:

dfco2=pd.read_csv('co2.csv', encoding="Windows-1250")

#In[]:

asia_co2=dfco2[((dfco2.country_name== 'China') |
                (dfco2.country_name== 'India') | 
                (dfco2.country_name== 'Philippines')) & (dfco2.year > 1960 )]

#In[]:

asia_co2=asia_co2.rename(columns={'country_name' : 'Area',
                                  'year' : 'Year',
                                  'value' : 'CO2'})
#In[]:

asia_co2=asia_co2.drop(columns=['country_code'])

#Switch to bilons CO2 values
#In[]:

asia_co2.CO2 = round(asia_co2.CO2/1000000,2)

# Merge temp and CO2
#In[]:

asia_co2.Year = pd.to_numeric(asia_co2.Year)

#In[]:

asia_all = pd.merge(asia_3_tmp, asia_co2, on = ['Area','Year'], how = 'left')

#Forest table for Asia
#In[]:

df_for = pd.read_csv('forest.csv')

#In[]:

asia_forest = df_for[((df_for.country_name == 'China') |
                (df_for.country_name == 'India') | 
                (df_for.country_name == 'Philippines'))]

#In[]:

asia_forest = asia_forest.rename(columns = {'country_name' : 'Area',
                                            'year' : 'Year',
                                            'value' : 'Zalesienie'})

#In[]:

asia_forest = asia_forest.drop(columns=['country_code'])

#In[]:

asia_forest.Year = pd.to_numeric(asia_forest.Year)

#In[]:

asia_all = pd.merge(asia_all, asia_forest, on=['Area', 'Year'], how = 'left')

#GDP percapita table for Asia

#In[]:

df_gdp = pd.read_csv('GDP_percapita.csv')

#In[]:

df_gdp = df_gdp.rename(columns = {'Country Name' : 'Area'})

#In[]:

asia_gdp=df_gdp[(df_gdp.Area == 'China') |
                (df_gdp.Area == 'India') | 
                (df_gdp.Area == 'Philippines')]

#In[]:

asia_gdp = asia_gdp.drop(columns=['Code',
                                  '1960',
                                  'Unnamed: 65'])

#In[]:

asia_gdp = pd.melt(asia_gdp, id_vars = 'Area')

#In[]:

asia_gdp =asia_gdp.rename(columns= {'variable' : 'Year',
                                       'value' : 'GDP' })

#In[]:

asia_gdp = asia_gdp.sort_values(by= ['Area','Year'])

#In[]:

asia_gdp.Year = pd.to_numeric(asia_gdp.Year)

#In[]:

asia_all = pd.merge(asia_all, asia_gdp, on=['Area', 'Year'], how = 'left')

#Urbanization table for Asia
#In[]:

df_urban = pd.read_csv('share-of-population-urban.csv')

#In[]:

asia_urban = df_urban[((df_urban.Entity == 'China') |
                      (df_urban.Entity == 'India') |
                      (df_urban.Entity == 'Philippines')) & (df_urban.Year > 1960)]

#In[]:

asia_urban = asia_urban.rename(columns = {'Entity' : 'Area',
                                          'Urban population (% of total population)' : 'Urbanization_%'})

#In[]:

asia_urban = asia_urban.drop(columns = ['Code'])

#In[]:

asia_all = pd.merge(asia_all, asia_urban, on = ['Area', 'Year'], how = 'left')

#Correlation table for China
#In[]:

china = asia_all[asia_all.Area == 'China']

#In[]:

corr_china = china.drop(columns = ['Area', 'Year'])

#In[]:

corr_china1 = corr_china

#In[]:

corr_china1.rename(columns = {'Temp' : 'Temperatura', 
                              'Zalesienie' : 'Poziom zalesienia', 
                              'GDP' : 'PKB per capita', 
                              'Urbanization_%': 'Poziom urbanizacji'}, inplace = True)

#In[]:

corr_china1 = corr_china1.corr()
sns.heatmap(corr_china1, annot=True, cmap = 'Greens')
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 15)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 15)
sns.set(font_scale = 1.6)
plt.xticks(rotation = 90)
plt.title('Chiny')
plt.show()

#Correlation table for India
#In[]:

india = asia_all[asia_all.Area == 'India']

#In[]:

corr_india = india.drop(columns = ['Area', 'Year'])

#In[]:

corr_india1 = corr_india

#In[]:

corr_india1.rename(columns = {'Temp' : 'Temperatura', 
                              'Zalesienie' : 'Poziom zalesienia', 
                              'GDP' : 'PKB per capita', 
                              'Urbanization_%': 'Poziom urbanizacji'}, inplace = True)

#In[]:

corr_india1 = corr_india1.corr()
sns.heatmap(corr_india1, annot=True, cmap = 'Greens')
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 15)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 15)
sns.set(font_scale = 1.6)
plt.xticks(rotation = 90)
plt.title('Indie')
plt.show()

#Correlation table for Philipines
#In[]:

phil = asia_all[asia_all.Area == 'Philippines']

#In[]:

corr_phil = phil.drop(columns = ['Area', 'Year'])

#In[]:

corr_phil1 = corr_phil

#In[]:

corr_phil1.rename(columns = {'Temp' : 'Temperatura', 
                             'Zalesienie' : 'Poziom zalesienia', 
                             'GDP' : 'PKB per capita', 
                             'Urbanization_%': 'Poziom urbanizacji'}, inplace = True)

#In[]:

corr_phil1 = corr_phil1.corr()
sns.heatmap(corr_phil1, annot=True, cmap = 'Greens')
plt.tick_params(axis='x', labelcolor='#000000', labelsize = 15)
plt.tick_params(axis='y', labelcolor='#000000', labelsize = 15)
sns.set(font_scale = 1.6)
plt.xticks(rotation = 90)
plt.title('Filipiny')
plt.show()

#CO2 emission plots
#In[]:

y1_co2 = china.CO2
y2_co2 = india.CO2
y3_co2 = phil.CO2

#In[]:

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(x_mat, y1_co2, label='Chiny')
plt.bar(x_mat, y2_co2, label='Indie', color='orange')
plt.bar(x_mat, y3_co2, label='Filipiny', color='green')

plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('CO2')
plt.title('Emisja CO2 (1961-2019)')
plt.legend()
plt.show()

#In[]:

fig, ax1 = plt.subplots()

plt.xticks(rotation=90)

ax1.set_ylabel('CO2 [bln t]', color='#FF6600') 
ax1.bar(x_mat, y1_co2, color='#FF6600')
ax1.tick_params(axis='y', labelcolor='#FF6600')

ax2 = ax1.twinx() 

ax2.set_ylabel('Temp', color='black')
ax2.plot(x_mat, bspl_y1, color='black')
ax2.tick_params(axis='y', labelcolor='black')
plt.ylim([-1, 2.5])

fig.tight_layout()  


plt.subplots_adjust(left=-0.5)
plt.title('Chiny zmiany temperatury i emisji CO2 (1961-2019)')
plt.show()

#In[]:

fig, ax1 = plt.subplots()

plt.xticks(rotation=90)

ax1.set_ylabel('CO2', color='orange')  
ax1.bar(x_mat, y2_co2, color='orange')
ax1.tick_params(axis='y', labelcolor='orange')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temp', color='red')
ax2.plot(x_mat, bspl_y2, color='red')
ax2.tick_params(axis='y', labelcolor='red')


fig.tight_layout()  


plt.subplots_adjust(left=-0.5)
plt.title('Indie zmiany temperatury i emisji CO2 (1961-2019)')
plt.show()

#In[]:

fig, ax1 = plt.subplots()

plt.xticks(rotation=90)

ax1.set_ylabel('CO2', color='limegreen')  
ax1.bar(x_mat, y3_co2, color='limegreen')
ax1.tick_params(axis='y', labelcolor='limegreen')

ax2 = ax1.twinx()  

ax2.set_ylabel('Temp', color='red')
ax2.plot(x_mat, bspl_y3, color='red')
ax2.tick_params(axis='y', labelcolor='red')


fig.tight_layout()  


plt.subplots_adjust(left=-0.5)
plt.title('Filipiny zmiany temperatury i emisji CO2')
plt.show()

# Forestation plots for Asia
#In[]:

y1_for = china.Zalesienie
y2_for = india.Zalesienie
y3_for = phil.Zalesienie

#In[]:

get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot(x_mat, y3_for, label='Filipiny', color='darkgreen')
plt.bar(x_mat, y2_for, label='Indie', color='orange')
plt.bar(x_mat, y1_for, label='Chiny', color='royalblue')

plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('forest')
plt.title('Zalesienie (1990-2019)')
plt.legend()
plt.show()

#In[]:

sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='China'],
            x="Zalesienie",
            y="CO2",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Greens')
plt.xlabel('Zalesienie [%]')
plt.ylabel('CO2 [bln t]')
plt.title('Chiny')
plt.show()

#In[]:

sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='India'],
            x="Zalesienie",
            y="Temp",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Greens')

#In[]:

sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='Philippines'],
            x="Zalesienie",
            y="Temp",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Greens')

#Urbanization plots for Asia
#In[]:

sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='China'],
            x="Urbanization_%",
            y="CO2",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Greys')


#In[]:

sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='India'],
            x="Urbanization_%",
            y="CO2",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Greys')


#In[]:

sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='Philippines'],
            x="Urbanization_%",
            y="CO2",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Greys')

#GDP plots for Asia
#In[]:
sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='China'],
            x="GDP",
            y="CO2",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Blues')
plt.xlabel('PKB per capita [$]')
plt.ylabel('CO2 [bln t]')
plt.title('Chiny')
plt.show()

#In[]:

sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='India'],
            x="GDP",
            y="CO2",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Blues')
plt.xlabel('PKB per capita [$]')
plt.ylabel('CO2 [bln t]')
plt.title('Chiny')
plt.show()

#In[]:

sns.set_context('paper')
sns.lmplot(data=asia_all[asia_all['Area']=='Philippines'],
            x="GDP",
            y="CO2",
            aspect=2.5,
            col='Area',
            hue = 'Area',
            palette = 'Blues')
plt.xlabel('PKB per capita [$]')
plt.ylabel('CO2 [bln t]')
plt.title('Chiny')
plt.show()


# #### South America

# In[ ]:

# Making individual variable for group purpose working

# ##### DataFrame with 3 countries from South America

# ##### Temperature change in 3 countries of South America

# In[18]:


SouthAmerica = df.copy()
SouthAmerica = optional_1(SouthAmerica)
SouthAmerica_whole = SouthAmerica[(SouthAmerica.Continent == 'Shouth America')]
SouthAmerica_temp = SouthAmerica_whole[(SouthAmerica_whole.Area == 'Argentina') | (
    SouthAmerica_whole.Area == 'Brazil') | (SouthAmerica_whole.Area == 'Peru')]
SouthAmerica_temp = SouthAmerica_temp[(SouthAmerica_temp.Months == 'Meteorological year') & (
    SouthAmerica_temp.Element == 'Temperature change')]
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
SouthAmerica_temp_mdf = SouthAmerica_temp_mdf.rename(
    columns={'variable': 'Year', 'value': 'Temperature'})
SouthAmerica_temp_mdf = SouthAmerica_temp_mdf.sort_values(by=['Area', 'Year'])
SouthAmerica_temp_mdf


# In[20]:


SouthAmerica_temp_mdf.Year = pd.to_numeric(SouthAmerica_temp_mdf.Year)


# In[ ]:

# Temperature chart

# In[21]:


Argentina_temp = SouthAmerica_temp_mdf[(
    SouthAmerica_temp_mdf.Area == 'Argentina')]
Brazil_temp = SouthAmerica_temp_mdf[(SouthAmerica_temp_mdf.Area == 'Brazil')]
Peru_temp = SouthAmerica_temp_mdf[(SouthAmerica_temp_mdf.Area == 'Peru')]
plt.plot(Argentina_temp.Year, Argentina_temp.Temperature,
         'g*-.', label='Argentyna')
plt.plot(Brazil_temp.Year, Brazil_temp.Temperature, 'g-', label='Brazylia')
plt.plot(Peru_temp.Year, Peru_temp.Temperature, 'g--', label='Peru')
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


SouthAmerica_CO2 = SouthAmerica_CO2.rename(
    columns={'country_name': 'Area', 'year': 'Year', 'value': 'CO2'})
SouthAmerica_CO2


# In[473]:


SouthAmerica_CO2.Year = pd.to_numeric(SouthAmerica_CO2.Year)


# In[ ]:

# Temperature change and value of CO2

# In[366]:


SouthAmerica_temp_CO2 = pd.merge(SouthAmerica_temp_mdf, SouthAmerica_CO2, on=[
                                 'Area', 'Year'], how='left')
SouthAmerica_temp_CO2


# In[ ]:

# Regression - value of CO2

# In[381]:


sns.set_context('paper')
sns.lmplot(data=SouthAmerica_CO2[((SouthAmerica_CO2['Area'] == 'Argentina')
                                  | (SouthAmerica_CO2['Area'] == 'Brazil')
                                  | (SouthAmerica_CO2['Area'] == 'Peru')) & (SouthAmerica_CO2['Year'])],
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


SouthAmerica_GDP = SouthAmerica_GDP.rename(columns={'Country Name': 'Area'})


# In[477]:


SouthAmerica_GDP = SouthAmerica_GDP[(SouthAmerica_GDP.Area == 'Argentina') | (SouthAmerica_GDP.Area == 'Brazil')
                                    | (SouthAmerica_GDP.Area == 'Peru')]
SouthAmerica_GDP


# In[ ]:

# ##### Modified table - GDP per capita

# In[478]:


SouthAmerica_GDP_mdf = pd.melt(SouthAmerica_GDP, id_vars='Area')
SouthAmerica_GDP_mdf = SouthAmerica_GDP_mdf.rename(
    columns={'variable': 'Year', 'value': 'GDP_per_capita'})
SouthAmerica_GDP_mdf = SouthAmerica_GDP_mdf.sort_values(by=['Area', 'Year'])
SouthAmerica_GDP_mdf


# In[479]:


SouthAmerica_GDP_mdf.Year = pd.to_numeric(SouthAmerica_GDP_mdf.Year)


# In[ ]:

# Regression - GDP per capita

# In[436]:


sns.set_context('paper')
sns.lmplot(data=SouthAmerica_GDP_mdf[((SouthAmerica_GDP_mdf['Area'] == 'Argentina')
                                      | (SouthAmerica_GDP_mdf['Area'] == 'Brazil')
                                      | (SouthAmerica_GDP_mdf['Area'] == 'Peru')) & (SouthAmerica_GDP_mdf['Year'])],
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
                                      | (SouthAmerica_GDP_mdf['Area'] == 'Peru')],
            x="GDP_per_capita",
            y="Year",
            kind='scatter',
            col='Area')
plt.show()


# In[422]:


Argentina_GDP = SouthAmerica_GDP_mdf[(
    SouthAmerica_GDP_mdf.Area == 'Argentina')]
Brazil_GDP = SouthAmerica_GDP_mdf[(SouthAmerica_GDP_mdf.Area == 'Brazil')]
Peru_GDP = SouthAmerica_GDP_mdf[(SouthAmerica_GDP_mdf.Area == 'Peru')]
plt.plot(Argentina_GDP.Year, Argentina_GDP.GDP_per_capita,
         'g-..', label='Argentyna')
plt.plot(Brazil_GDP.Year, Brazil_GDP.GDP_per_capita, 'g-', label='Brazylia')
plt.bar(Peru_GDP.Year, Peru_GDP.GDP_per_capita, label='Peru')
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


SouthAmerica_forestation = SouthAmerica_forestation.rename(
    columns={'country_name': 'Area', 'year': 'Year', 'value': 'Forestation_percent'})
SouthAmerica_forestation


# In[37]:


SouthAmerica_forestation.Year = pd.to_numeric(SouthAmerica_forestation.Year)


# In[ ]:

# Forestation

# In[38]:


Argentina_forestation = SouthAmerica_forestation[(
    SouthAmerica_forestation.Area == 'Argentina')]
Brazil_forestation = SouthAmerica_forestation[(
    SouthAmerica_forestation.Area == 'Brazil')]
Peru_forestation = SouthAmerica_forestation[(
    SouthAmerica_forestation.Area == 'Peru')]
plt.bar(Argentina_forestation.Year,
        Argentina_forestation.Forestation_percent, label='Argentyna')
plt.plot(Brazil_forestation.Year,
         Brazil_forestation.Forestation_percent, 'g-', label='Brazylia')
plt.plot(Peru_forestation.Year,
         Peru_forestation.Forestation_percent, 'g--', label='Peru')
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


SouthAmerica_energy = SouthAmerica_energy.rename(columns={'Entity': 'Area',
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
                                     | (SouthAmerica_energy['Area'] == 'Peru')) & (SouthAmerica_energy['Year'])],
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


SouthAmerica_urban = SouthAmerica_urban.rename(columns={'Entity': 'Area',
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
                                    | (SouthAmerica_urban['Area'] == 'Peru')) & (SouthAmerica_urban['Year'])],
           x="Year",
           y="Urbanization_rate_percent",
           aspect=2.5,
           hue='Area')

plt.show()


# In[ ]:

# Summarized tabel: Temperature change + CO2 + GDP per capita + Forestation + energy use + urbanization

# In[497]:


SouthAmerica_temp_CO2 = pd.merge(SouthAmerica_temp_mdf, SouthAmerica_CO2, on=[
                                 'Area', 'Year'], how='left')
SouthAmerica_temp_CO2_GDP = pd.merge(
    SouthAmerica_temp_CO2, SouthAmerica_GDP_mdf,  on=['Area', 'Year'], how='left')
SouthAmerica_temp_CO2_GDP_forest = pd.merge(
    SouthAmerica_temp_CO2_GDP, SouthAmerica_forestation, on=['Area', 'Year'], how='left')
SouthAmerica_temp_CO2_GDP_forest_en = pd.merge(
    SouthAmerica_temp_CO2_GDP_forest, SouthAmerica_energy, on=['Area', 'Year'], how='left')
SouthAmerica_temp_CO2_GDP_forest_en_urb = pd.merge(
    SouthAmerica_temp_CO2_GDP_forest_en, SouthAmerica_urban, on=['Area', 'Year'], how='left')
SouthAmerica_temp_CO2_GDP_forest_en_urb


# In[ ]:

# Correlation Argentina

# In[500]:


corr_Argentina = SouthAmerica_temp_CO2_GDP_forest_en_urb[(
    SouthAmerica_temp_CO2_GDP_forest_en_urb.Area == 'Argentina')]


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


corr_Brazil = SouthAmerica_temp_CO2_GDP_forest_en_urb[(
    SouthAmerica_temp_CO2_GDP_forest_en_urb.Area == 'Brazil')]


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


corr_Peru = SouthAmerica_temp_CO2_GDP_forest_en_urb[(
    SouthAmerica_temp_CO2_GDP_forest_en_urb.Area == 'Peru')]


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
Antarctica_temp = Antarctica[(Antarctica.Continent == 'Antarctica')]
Antarctica_temp = Antarctica[(Antarctica.Area == 'Antarctica')]
Antarctica_temp = Antarctica_temp[(Antarctica_temp.Months == 'Meteorological year') & (
    Antarctica_temp.Element == 'Temperature change')]
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
Antarctica_temp_mdf = Antarctica_temp_mdf.rename(
    columns={'variable': 'Year', 'value': 'Temperature'})
Antarctica_temp_mdf


# In[ ]:

# In[530]:


Antarctica_temp_change = Antarctica_temp_mdf[(
    Antarctica_temp_mdf.Area == 'Antarctica')]
plt.bar(Antarctica_temp_change.Year,
        Antarctica_temp_change.Temperature, label='Antarktyda')
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
