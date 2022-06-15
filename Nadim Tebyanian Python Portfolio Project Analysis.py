#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv('Student Mental health.csv')


# In[4]:


print(df)


# In[7]:


to_drop = ['Timestamp']


# In[9]:


#drop unneeded column
df.drop(to_drop, inplace=True, axis=1)


# In[10]:


print(df)


# In[40]:


df.info()


# In[24]:


import pandas as pd
import numpy as np
df=pd.read_csv('Student Mental health.csv', header=0)


# In[25]:


df


# In[29]:


#Dropping a column
to_drop = ['Timestamp']
df.drop(to_drop, inplace=True, axis=1)


# In[30]:


df


# In[5]:


#finding the index 
print(df.columns)


# In[11]:


#Younger students experience Depression
print(df[['Age', 'Do you have Depression?']])


# In[34]:


print(df.iloc[2:10])


# In[39]:


import pandas as pd
df=pd.read_csv('Student Mental health.csv', header=0)
for index, row in df.iterrows():
    print(row[5:6])


# In[39]:


df.loc[df['Choose your gender'] == "Male"]


# In[26]:


df.loc[df['Choose your gender'] == "Female"]


# In[29]:


df.describe()


# In[34]:


df.sort_values('What is your CGPA?', ascending=False)


# In[41]:


df.sort_values(['What is your CGPA?', 'What is your course?'], ascending=[1,0])


# In[14]:


df.iloc[:, 4:9]


# In[21]:


cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
df.head(10)


# In[8]:


import pandas as pd
df = pd.read_csv('Student Mental health.csv')


# In[18]:


df.groupby(['What is your CGPA?']).mean()


# In[19]:


df.groupby(['Choose your gender']).count()


# In[37]:


#Creating a basic chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('Student mental health.csv')
df.plot.line()
df.describe()
summary.round()


# In[38]:


summary.to_csv("summary.csv")


# In[51]:


#Creating a bar chart
ax = df['What is your CGPA?'].hist(figsize=(9,7))
ax.set_title('Student GPA')
ax.set_ylabel('Individuals')


# In[77]:


#Creating my own graph
y = [20,40,60,80,100]
plt.title('Student GPA', fontdict={'fontsize': 29})
plt.plot(y, marker=".", markersize=15, markeredgecolor='red')
plt.xlabel('Grade Scale')
plt.ylabel('Individuals')
plt.show()

