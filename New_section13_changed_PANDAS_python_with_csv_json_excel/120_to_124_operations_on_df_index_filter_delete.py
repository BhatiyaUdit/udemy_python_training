#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
df_csv = pandas.read_csv("./../sample_files/supermarkets.csv")


# In[2]:


df_csv


# In[4]:


# operation 1 --> if data does not have header will add header with numbers
df_csv = pandas.read_csv("./../sample_files/supermarkets.csv", header=None)
df_csv


# In[7]:


# now df_csv have header we can rename this header as column names  (use = operator)
df_csv.columns = ['ID', 'Address', 'City','State','country', 'name', 'count']
df_csv


# In[8]:


# operation 2 setting a particular column as index for the data ex ID
df_csv = pandas.read_csv("./../sample_files/supermarkets.csv")
df_csv.set_index("ID")


# In[9]:


# Operation 2 has made ID index temporarily on the df because it is not an inplace operation
# df_csv is not modified
df_csv


# In[10]:


# to make index permanent we need to use inplace flag as True
df_csv.set_index("ID", inplace=True)


# In[11]:


df_csv


# In[13]:


# operation 3 filtering data using label based indexing
# df.loc["row_start":"row_end" , "column_start" : "column_end"]
df_csv.loc["3":"5", "State" : "Name"]


# In[14]:


# if we want all before "5" row name
df_csv.loc[:"5", "State" : "Name"]


# In[15]:


#if we want all after State
df_csv.loc[:"5", "State":]


# In[17]:


# Operation 4 position based indexing
# df.iloc[start_row_index : end_row_index+1 , start_column_index : end_column_index+1]
df_csv.iloc[1:3, 1:3]


# In[19]:


# same playing around can be done on positions
df_csv.iloc[3:,:4]


# In[21]:


# Operation 5 Deleting rows and columns
# df_csv.drop("Row/Column name(s)", 0/1) -> 0 for rows , 1 for columns
df_csv.drop("City", 1)


# In[22]:


# data is not actually dropped as drop is also not inplace
df_csv


# In[27]:


# we can also pass a list as an arg for dropping the data
df_csv.drop(["City", "State"], 1)


# In[28]:


df_csv


# In[30]:


# Row with the name of the index as "2" will be deleted
df_csv.drop(2, 0)


# In[31]:


# dynamically drop rows after 2 
#df_csv.drop([2:], 0)


# In[32]:


df_csv.drop(df_csv.index[2:], 0)


# In[34]:


# drop all before column 3 
# df_csv.columns will return a list of column names and we are asking index [:3] meaning names of 0,1,2 columns will be returned
# and 0,1,2 columns will be deleted
df_csv.drop(df_csv.columns[:3], 1)


# In[ ]:




