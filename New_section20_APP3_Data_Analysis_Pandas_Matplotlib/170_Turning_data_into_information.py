"""
Turning Data into information

    -> Average Rating
    -> Average Rating for a particular course
    -> Average Rating for a particular period
    -> Average Rating for a particular course in a particular period
    -> Average of uncommented Ratings --> df['column'].isnull()
    -> Average of commented Ratings
    -> Number of uncommented Ratings
    -> Number of commented Ratings
    -> Number of comments containing a certain word
    -> Average of commented ratings with "accent" in comment "

"""
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
from datetime import datetime
from pytz import utc


# In[2]:


data = pandas.read_csv("./data/reviews.csv", parse_dates = ['Timestamp'])
data[data['Timestamp']> datetime(2020, 7, 1, tzinfo=utc)]


# ## 1. Average Rating

# In[3]:


data['Rating'].mean()


# ## 2. Average Rating of Particular Course

# In[6]:


data[data['Course Name'] == 'The Python Mega Course: Build 10 Real World Applications']['Rating'].mean()


# ## 3. Average Rating for a particular period

# In[7]:


# For entire year 2020
data[(data['Timestamp'] >= datetime(2020, 1,1 , tzinfo=utc)) &
     (data['Timestamp'] <= datetime(2020, 12 ,31 , tzinfo=utc))]


# In[8]:


d = data[(data['Timestamp'] >= datetime(2020, 1,1 , tzinfo=utc)) &
     (data['Timestamp'] <= datetime(2020, 12 ,31 , tzinfo=utc))]
d['Rating'].mean()


# ## 4. Average Rating for a particular course in a particular period

# In[9]:


d = data[(data['Timestamp'] >= datetime(2020, 1,1 , tzinfo=utc)) &
     (data['Timestamp'] <= datetime(2020, 12 ,31 , tzinfo=utc)) &
     (data['Course Name'] == 'The Python Mega Course: Build 10 Real World Applications')]
d['Rating'].mean()


# ## 5. Average of uncommented Ratings

# In[14]:


d = data[(data['Comment'].isnull())]
d['Rating'].mean()


# ## 6. Average of commented Ratings

# In[15]:


d = data[(data['Comment'].notnull())]
d['Rating'].mean()


# ## 7. Number of Uncommented Ratings

# In[16]:


d = data[(data['Comment'].isnull())]
d['Rating'].count()


# ## 8. Number of Commented Ratings

# In[17]:


d = data[(data['Comment'].notnull())]
d['Rating'].count()


# ## 9. Number of comments containing a certain word

# In[21]:


d = data[(data['Comment'].notnull()) &
        (data['Comment'].str.contains('accent'))]


# In[26]:


d = data[(data['Comment'].str.contains('accent', na=False))]
d['Rating'].count()


# ## 10. Average of commented ratings with "accent" in comment

# In[27]:


d = data[(data['Comment'].str.contains('accent', na=False))]
d['Rating'].mean()


# In[ ]:




