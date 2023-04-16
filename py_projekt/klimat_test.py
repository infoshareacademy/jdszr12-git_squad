#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pd.set_option("display.width", 80)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[3]:


df=pd.read_csv('https://raw.githubusercontent.com/infoshareacademy/jdszr12-git_squad/main/py_projekt/Environment_Temperature_change_E_All_Data_NOFLAG.csv' , encoding="Windows-1250")
df


# In[4]:


df = df.rename(columns={"Area Code": "Area_Code",
                        "Months Code": "Months_Code",
                        "Element Code": "Element_Code"})


# In[5]:


df['Area'] = df['Area'].str.replace(',',' ')


# In[6]:


df['Area'] = df['Area'].str.replace('\"','')


# In[7]:


mateo=df.copy()


# In[8]:


def optional_1(mateo):
    continent = pd.read_csv("https://raw.githubusercontent.com/infoshareacademy/jdszr12-git_squad/main/py_projekt/_Countries_Continents.csv", names=['Area', 'Continent', 'Continent_Code'], encoding="UTF-8")
    mateo = pd.merge(left=continent, right=df, on='Area', how='inner')
    return mateo


# In[9]:


mateo1=optional_1(mateo)
mateo1


# In[10]:


mateo1.columns=mateo1.columns.str.replace('Y', '')


# In[11]:


mateo1['Area'] = mateo1['Area'].str.replace("'" ,' ')


# In[12]:


asia=mateo1[(mateo1.Continent_Code==2) & (mateo1.Months_Code==7020) & (mateo1.Element_Code==7271)]
asia


# In[13]:


asia=asia.drop(columns=['Continent',
                            'Continent_Code',
                             'Area_Code',
                             'Months_Code',
                             'Months',
                             'Element_Code',
                             'Element',
                             'Unit'])


# In[14]:


asia


# In[15]:


asia_5=asia[(asia.Area=='Afghanistan') | (asia.Area=='Saudi Arabia') | (asia.Area=='India') |
             (asia.Area=='Democratic People s Republic of Korea') | (asia.Area=='China')]
asia_5


# In[16]:


asia_5.isnull().sum()


# In[17]:


x=asia_5.columns[1:].T


# In[18]:


y1=asia_5.iloc[0,-59:].values.T # Afganistan


# In[19]:


y2=asia_5.iloc[1,-59:].values.T #Chiny


# In[20]:


y3=asia_5.iloc[2,-59:].values.T #South Korea


# In[21]:


y4=asia_5.iloc[3,-59:].values.T #India


# In[22]:


y5=asia_5.iloc[4,-59:].values.T #Arabia


# In[23]:


plt.plot(x, y1, label='Afganistan')
plt.plot(x, y2, label='Chiny')
plt.plot(x, y3, label='South Korea')
plt.plot(x, y4, label='Indie')
plt.plot(x, y5, label='Arabia')
plt.xticks(rotation=90)
plt.subplots_adjust(left=-0.5)
plt.xlabel('year')
plt.ylabel('temp \u2103')
plt.title('Temperatures (1961-2019)')
plt.legend()
plt.show();

