#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df_csv = pandas.read_csv("./../sample_files/supermarkets.csv")


# In[3]:


print(df_csv)


# In[7]:


df_json = pandas.read_json("./../sample_files/supermarkets.json")


# In[8]:


print(df_json)


# In[12]:


df_excel = pandas.read_excel("./../sample_files/supermarkets.xlsx", sheet_name=0)


# In[13]:


print(df_excel)


# In[14]:


df_txt_comma = pandas.read_csv("./../sample_files/supermarkets-commas.txt")


# In[30]:


print(df_txt_comma)


# In[16]:


df_txt_semi1 = pandas.read_csv("./../sample_files/supermarkets-semi-colons.txt")


# In[17]:


print(df_txt_semi1)


# In[21]:


df_txt_semi2 = pandas.read_csv("./../sample_files/supermarkets-semi-colons.txt", sep =";")


# In[24]:


print(df_txt_semi2)


# In[23]:


print(df_txt_semi1)


# In[ ]:




