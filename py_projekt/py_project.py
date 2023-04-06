# %% [markdown]
# # Climate catastrophe
# 
# ## Data analysis on changes in average temperatures
# 
# Project analyzing data on changes in average temperatures. The `csv` file containing the raw data can be found at [kaggle.com](https://www.kaggle.com/datasets/sevgisarac/temperature-change)

# %% [markdown]
# ### Import

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ### DataFrame

# %%
# default value
pd.set_option("display.width", 80)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# %%
df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="Windows-1250") #index_col=False

df.head(37)

# %%
df.shape

# %%
df = df.rename(columns={"Area Code": "Area_Code",
                        "Months Code": "Months_Code",
                        "Element Code": "Element_Code"})

# %%
# Optional 
continent = pd.read_csv("_Countries_Continents.csv", names=['Area', 'Contintnt', 'Contintnt_Code'], encoding="UTF-8")

df = pd.merge(left=continent, right=df, on='Area', how='inner')
df.shape

# %%
# !!!!!!! usunięcie wierszy z standard deviation (kod 6078) wszędzie
df = df.loc[(df['Element_Code'] == 7271) & (df['Area_Code'] < 5000)]

# %%
df.shape

# %%
# !!!!!!! liczy prawidłową std do podstawienia w fillna (liczy po wierszu)
rig = df.loc[3][-59:].std() - df.loc[3][-59:].mean()
round(np.abs(rig),3)

# %%
df.shape[0]

# %%
m = round(df.loc[4198][-59:].mean(),3)
m

# %%
# pętla iteruje każdy wiersz w dataframe
for i in range(df.shape[0]-1):
    m = round(df.iloc[i,-59:].mean(),3) # oblicznie średniej dla wiersza (nawej jeśli są NaN/null'e)
    df.iloc[i,-59:] = df.iloc[i,-59:].fillna(m)
    #df2.iloc[0,-6:] = df2.iloc[0,-6:].fillna(m)

# %%
#df.to_csv('Countries_Continents_All.csv', index=False)

# %%
# First Y1961
#df.loc[342][9]
# Last Y2019
#df.loc[342][67]

# %%
df.loc[2]

# %%


# %%
df.loc[3][-59:].std()

# %%
df.loc[3][-59:].mean()

# %%
#df2.iloc[:, 4].fillna(df2.mean(axis=1))
#df.loc[342][-59:].fillna(df.loc[342+1][-59:])
#df.fillna(method='ffill', inplace=True)
#df.loc[342][-59:]

# %%
#df.iloc[342,-59:].fillna(df.loc[342][-59:].where(df['Element_Code'] == 6078))

# %%
#jaro = jaro.loc[(jaro['Months_Code'] == 7020) & (jaro['Element_Code'] == 7271) & (jaro['Area_Code'] < 5000)]

#df2.iloc[:, 4].fillna(df2.mean(axis=1))

# jaro.replace(to_replace=np.nan)

# jaro.replace(to_replace=np.nan, value=
#              jaro.loc[(jaro['Element_Code'] == 6078) &
#                       (jaro[''] == ) &
#                       (jaro[''] == )
#                      ]
#             )

# for i in range(jaro.shape[0]):
#     if (jaro.loc[i][-59:].isna()) != False:
#         print(f'{i}:\t {jaro.loc[i][0]}\t  NaN: {jaro.loc[i][-59:].isna().sum()}')

jaro.loc[10][-59:] # wyświetla wartości/value dla samych roczników (od Y1961 do Y2019) dla indexu nr 10

# %% [markdown]
# ## Jaro

# %%
pd.set_option('display.max_rows', None)

# %%
jaro = df.copy()

# %%
jaro = jaro.loc[(jaro['Months_Code'] == 7020) & (jaro['Element_Code'] == 7271) & (jaro['Area_Code'] < 5000)]

# %%
jaro.shape

# %%
# Replacing comas in string for future additional csv file (to read it correctly)
jaro['Area'].str.replace(',','')

# %%
# Replacing quote in string for '_Area.csv' additional file (to read it correctly)
jaro['Area'].str.replace('\"','').to_csv('_Area.csv', index=False, header=False)

# %%
# To country list in '_Area.csv', for each country was added manualy :
# continent name & continent number columns.
# Everything saved in '_Countries_Continents.csv' file

# %%
continent = pd.read_csv("_Countries_Continents.csv", names=['Area', 'Contintnt', 'Contintnt_Code'], encoding="UTF-8")
continent.head(5)

# %%
continent.shape

# %%
#continent.loc[continent['Continent Code']==2] # v
jaro = pd.merge(left=continent, right=jaro, on='Area', how='inner')
jaro.shape

# %%
jaro.head(1)

# %%


# %%
jaro1.tail(55)

# %%
jaro.loc[10][-59:].isna()

# %%
df.loc[342][6]

# %%
#jaro = jaro.loc[(jaro['Months_Code'] == 7020) & (jaro['Element_Code'] == 7271) & (jaro['Area_Code'] < 5000)]

jaro.replace(to_replace=np.nan)

jaro.replace(to_replace=np.nan, value=
             jaro.loc[(jaro['Element_Code'] == 6078) &
                      (jaro[''] == ) &
                      (jaro[''] == )
                     ]
            )

# for i in range(jaro.shape[0]):
#     if (jaro.loc[i][-59:].isna()) != False:
#         print(f'{i}:\t {jaro.loc[i][0]}\t  NaN: {jaro.loc[i][-59:].isna().sum()}')

jaro.loc[10][-59:] # wyświetla wartości/value dla samych roczników (od Y1961 do Y2019) dla indexu nr 10

# %%
# Counting NaN/Null with row index (where year is value)
# and country name (plus sum in every Year columns)
# for future purpose of cleaning

#pd33.isna().sum()
#pd33.loc[83][-59:].isna().sum()
for i in range(jaro.shape[0]):
    if (jaro.loc[i][-59:].isna().sum()) != 0:
        print(f'{i}:\t {jaro.loc[i][0]}\t  NaN: {jaro.loc[i][-59:].isna().sum()}')

# %%


# %%
#pd33.loc[10][-59:].isna() # wskazuje ostatnie 59 (same roczniki)
#pd33.loc[10][11] # wskazuje konkretny
pd33.loc[10].isna() # Y1961 (pierwszy)
#pd33.loc[10][67] # Y2019 (ostatni)
#pd33.loc[10][9:67]

#def replace_nan(val):
# for i in range(pd33.shape[0]):
#     for j in range(pd33.shape[1]):
#         if pd33.loc[i][j] == np.nan:
#             print("true")
#             if pd33.loc[i][9] == nan:
#             elif pd33.loc[i][9]

# %%
import numpy as np
import pandas as pd

GFG_dict = { 'G1': [10, 20, 30, 40, np.nan, 14, 17, 11, 21, 22, 23, 25],
             'G2': [15, 14, 17, 11, 21, 22, 23, 25,25, np.NaN, np.NaN, 29],
             'G3': [15, 14, 17, 11, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN],
             'G4': [np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, 14, 17, 11, 21],
             'G5': [15, 14, np.NaN, np.NaN, np.NaN, 22, 23, 25,25, np.NaN, np.NaN, 29]}  
# Create a DataFrame from dictionary
gfg = pd.DataFrame(GFG_dict)
  
#Finding the mean of the column having NaN
mean_value1=gfg['G1'].mean()
mean_value2=gfg['G2'].mean()
mean_value3=gfg['G3'].mean()  
mean_value4=gfg['G4'].mean()
mean_value5=gfg['G5'].mean()

# Replace NaNs in column S2 with the
# mean of values in the same column
gfg['G1'].fillna(value=mean_value1, inplace=True)
gfg['G2'].fillna(value=mean_value2, inplace=True)
gfg['G3'].fillna(value=mean_value3, inplace=True)
gfg['G4'].fillna(value=mean_value4, inplace=True)
gfg['G5'].fillna(value=mean_value4, inplace=True)
print('Updated Dataframe:')
print(gfg)

# %%
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
  
Dataset = pd.read_csv("property data.csv")
X = Dataset.iloc[:, 1].values.reshape(-1, 1)
  
# To calculate mean use imputer class
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(X)
X = imputer.transform(X)
print(X)

# %%


# %%
# import re

# string = '                     Cocos (Keeling) Islands'
# new_string = re.sub(r'^\s+(?=[a-zA-Z])|\s+$', '', string)
# print(new_string)

# %%
#df1['Area'].replace(r'^\s+(?=[a-zA-Z])|\s+$', '', regex=True)

# %%
#df1.isna().sum()

#df1.loc[df1[0]]
#df1.insert(loc=0, column="", value="")

# %% [markdown]
# # ANIA

# %%


# %%


# %%
#df21 = df0.loc[:,['Area Code','Area']]
#print(df21)
#df22 = df21.drop_duplicates(subset=['Area'], keep='first')
#df22
#df22.to_csv('_Area_Code.csv', index=False, header=False)

# %%
#df0.isnull().sum()

# %%
#x = 0
#df8 = df0[df0.isna().any(axis=1)].loc[:, ['Area Code', 'Months', 'Y2019']].groupby(['Area Code'])['Y2019'].agg(x+1 if df0.loc['Y2019'])
#df8
#counts = df0[:].value_counts(dropna=False)
#counts

# %%
# def is_large(x):
#     return np.sum(x == None)

# %%
# df7 = df0.groupby(['Area', 'Month'])['Y2019'].agg([, np.mean, is_large])
# df7
#df6 = df0[df0.iloc[:, -59:] != None]
#df6
#df5 = df0[(df0.iloc[:, -59:] != None) | (df0.iloc[:, -59:] != 0) | (df0.iloc[:, -59:] != 'NaN')]
#df5.iloc[:, -59:]
#df0.iloc[:, -59:]

# %% [markdown]
# =======================================================================================================

# %% [markdown]
# Droping `isNewBuilt` column & rename columns (for matplotlib purpose)

# %%

#df0.drop('isNewBuilt', inplace=True, axis=1)
#df0.head()

# %%
# df = df0.rename(columns={"squareMeters": "Metry_kwadratowe",
#                    "numberOfRooms": "Liczba_pokoi",
#                    "hasYard": "Podworko",
#                    "hasPool": "Basen",
#                    "floors": "Pietra",
#                    "cityCode": "Kod_pocztowy",
#                    "cityPartRange": "Prestiz",
#                    "numPrevOwners": "Liczba_poprzednich_wlascicieli",
#                    "made": "Zbudowany",
#                    "hasStormProtector": "Instalacja_odgromowa",
#                    "basement": "Piwnica",
#                    "attic": "Strych",
#                    "garage": "Garaz",
#                    "hasStorageRoom": "Magazyn",
#                    "hasGuestRoom": "Goscinny",
#                    "price": "Cena"})

# %%
#df.isna().sum()

# %%
#df.fillna(0, inplace=True)

# %% [markdown]
# ### Data check

# %%
#print(f'Shape: {df.shape}\n\n{df.index}')

# %%
#df.info()

# %%
#analysis=df.describe()
#analysis

# %% [markdown]
# ### Data normalization
# * Square Meters

# %%
# mean_meters = analysis.loc['mean','Metry_kwadratowe']
# min_meters = round(mean_meters - analysis.loc['std','Metry_kwadratowe'],0)
# max_meters = round(mean_meters+ analysis.loc['std','Metry_kwadratowe'],0)

# print(f'Square meters to remove: \n - under: {min_meters//2}, \n - above: {max_meters*2}')

# %%
# df = df[(df.Metry_kwadratowe > min_meters//2) & (df.Metry_kwadratowe < max_meters*2)]
# #df

# %% [markdown]
# * Number of rooms

# %%
# mean_rooms = analysis.loc['mean','Liczba_pokoi']
# min_rooms = round(mean_rooms - analysis.loc['std','Liczba_pokoi'],0)
# max_rooms = round(mean_rooms+ analysis.loc['std','Liczba_pokoi'],0)

# print(f'Number of rooms to remove: \n - under: {min_rooms//2}')

# %%
# df = df[(df.Liczba_pokoi > min_rooms//2)]
# #df.tail(50)

# %% [markdown]
# * Floors

# %%
# mean_floors = analysis.loc['mean','Pietra']
# min_floors = round(mean_floors - analysis.loc['std','Pietra'],0)
# max_floors = round(mean_floors+ analysis.loc['std','Pietra'],0)

# print(f'Floors to remove: \n - under: {min_floors//2}, \n - above: {max_floors*2}')

# %%
# df = df[(df.Pietra > min_floors//2)]
# #df.head(50)

# %% [markdown]
# #### Previous owners & Made - without normalization (narrow range)

# %% [markdown]
# * Basement

# %%
# mean_basement = analysis.loc['mean','Piwnica']
# min_basement = round(mean_basement - analysis.loc['std','Piwnica'],0)
# max_basement = round(mean_basement+ analysis.loc['std','Piwnica'],0)

# print(f'Basement to remove: \n - under: {min_basement//2}, \n - above: {max_basement*2} \n and if Basement > Square_Meters')

# %%
# df = df[(df.Piwnica > min_basement//2) & (df.Piwnica < df.Metry_kwadratowe)]
# #df.head(50)

# %% [markdown]
# * Attic

# %%
# mean_attic = analysis.loc['mean','Strych']
# min_attic = round(mean_attic - analysis.loc['std','Strych'],0)
# max_attic = round(mean_attic + analysis.loc['std','Strych'],0)

# print(f'Attic to remove: \n - under: {min_attic//2}, \n - above: {max_attic*2} \n and if Attic > Square_Meters')

# %%
# df = df[(df.Strych > min_attic//2) & (df.Strych < df.Metry_kwadratowe)]
# #df.head(50)

# %% [markdown]
# * garage

# %%
# mean_garage = analysis.loc['mean','Garaz']
# min_garage = round(mean_garage - analysis.loc['std','Garaz'],0)
# max_garage = round(mean_garage + analysis.loc['std','Garaz'],0)

# print(f'Garage to remove: \n - under: {min_garage//2}, \n - above: {max_garage*2} \n and if jesli Garage > Square_Meters')

# %%
# df = df[(df.Garaz > min_garage//2) & (df.Garaz < df.Metry_kwadratowe)]
# #df.head(50)

# %% [markdown]
# #### Reseting index & printing shape

# %%
# df = df.reset_index()

# %% [markdown]
# #### Export DataFrame to new `csv` file

# %%
# df.to_csv("PariCleaned.csv", index=False)

# %%
# print(f'Shape: {df.shape}')


