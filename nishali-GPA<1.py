#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[3]:


course = pd.read_csv('DSC_2CourseData_030819.csv')
term = pd.read_csv('DSC_3TermData_030819.csv')
dem = pd.read_csv('DSC_1Demographic_030819.csv')


# In[4]:


course.columns


# In[5]:


term.columns


# In[6]:


#dropping invalid SubjectID
cleanCourse = term.drop(term[term['SubjectID']<0].index)


# In[7]:


cleanTerm = dem.drop(dem[dem['SubjectID']<0].index)


# In[8]:


#Start Merging
term_dem_merge = pd.merge(cleanTerm, cleanCourse,on=['SubjectID'], how='inner')


# In[9]:


term_dem_merge.iloc[: ,[0,69]]


# In[10]:


gpalowerthen1=term[term['Term GPA']<1]


# In[11]:


gpalowerthen1.head()


# In[12]:


gpa = gpalowerthen1.loc[gpalowerthen1['Term GPA'] != 0]
gpa.head()


# In[13]:


gpa.iloc[[0] ,[0,2]]


# In[14]:


gpa.count()


# In[53]:


studentid =gpa.SubjectID.unique()
count = len(studentid)


# In[54]:


new = gpa['Term GPA'].value_counts(bins=7)


# In[55]:


new


# In[56]:


studentid


# In[80]:


c=0

for studentid in dem['SubjectID']:
    if (dem['Degree Confer Date']isnull())==True:
        c+=1
 


# In[78]:


c/count


# In[ ]:




