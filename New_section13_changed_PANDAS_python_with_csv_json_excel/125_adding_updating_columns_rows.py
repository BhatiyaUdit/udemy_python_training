#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[2]:


# adding data to the data frame 
# to add column format = > df['new_column_name'] = ['value1','value2',.... till number of rows]
#
# NOTE: this operation is inplace 
# 
# to add a row NO straight forward method
#
#
# first transpose the DF object to get the columns in place of rows and rows in place of columns
# then add a cloumn with above format to the transposed df with values as needed in the row
# re-traspose the get the updated df
#
#
#
# use df.shape to get the number of rows and columns
# df.shape[0] will give the number of rows


# to increase the elements in the list we can multiply the whole list with a number ['c'] * 6


# In[3]:


df_csv = pandas.read_csv("./../sample_files/supermarkets.csv")


# In[4]:


df_csv


# In[5]:


df_csv['new_column'] = ['sample value 2'] * df_csv.shape[0]


# In[6]:


df_csv


# In[7]:


### updating a column 

# to update a column we can use column as an index and use any value
df_csv['new_column'] = df_csv['new_column'] + '---' + df_csv['Name']
df_csv




# In[8]:


# *******************************************************************************************
# ******    Adding Row **********************************************************************


# In[9]:


df_transposed = df_csv.T
df_transposed


# In[10]:


df_transposed['7'] = ['7','new Add', 'new city', 'new State', 'new Country', 'new Name', 'new Enplpoyedd', 'new sameple value']


# In[11]:


df_transposed


# In[12]:


df_csv = df_transposed.T
df_csv


# In[ ]:




