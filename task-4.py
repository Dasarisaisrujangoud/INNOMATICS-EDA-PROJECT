#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("data.xlsx - Sheet1.csv")


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.info()


# In[132]:


df.describe()


# In[133]:


df.isnull()


# In[135]:


df.drop_duplicates()


# #  What is an average salary?

# In[7]:


mean_sal=df['Salary'].mean()


# In[8]:


mean_sal


# In[9]:


plt.hist(df["Salary"])


# In[10]:


sns.boxplot(df["Salary"])


# In[11]:


q1=df["Salary"].quantile(0.25)
q3=df["Salary"].quantile(0.75)
iqr=q3-q1
l_b=q1-1.5*iqr
u_b=q3+1.5*iqr
filter_data=df[(df["Salary"]>=l_b) & (df["Salary"]<=u_b)]


# In[12]:


filter_data


# In[56]:


sns.boxplot(filter_data['Salary'])
plt.figure(figsize=(5, 5))
plt.show()


# # whose date of  joining is between 2010 to 2015 has  average,minimum,maximum ofsalary?

# In[14]:


df["DOJ"]=pd.to_datetime(df["DOJ"])


# In[15]:


df.info()


# In[16]:


doj=df[(df["DOJ"]>="01/01/10") & (df["DOJ"]<="01/01/15") ]


# In[17]:


doj


# In[18]:


doj["Salary"].describe()


# In[19]:


doj["Salary"].mean()


# In[20]:


doj["Salary"].min()


# In[21]:


doj["Salary"].max()


# In[22]:


plt.hist(doj["Salary"])


# # what is the Maximum salary of females?

# In[23]:


female=df[df["Gender"]=="f"]


# In[24]:


female


# In[25]:


female["Salary"].max()


# In[26]:


female["Salary"].mean()


# In[27]:


sns.kdeplot(female["Salary"],shade=True)


# # find highest slary state
# 

# In[28]:


sns.boxplot(x=df["Salary"],y=df["CollegeState"])


# In[29]:


max_salary_by_state = df.groupby('CollegeState')['Salary'].max()
print(max_salary_by_state)


# Observation:
# Rajasthan state has highest slary

# # who had highest salary male or female?

# In[30]:


male=df[df["Gender"]=="m"]


# In[31]:


male


# In[32]:


male["Salary"].max()


# In[33]:


male["Salary"].mean()


# In[34]:


male["Salary"].min()


# In[35]:


female["Salary"].max()


# In[36]:


female["Salary"].mean()


# In[37]:


sns.histplot(df["Gender"])


# In[38]:


f=female["Salary"]


# In[39]:


m=male["Salary"]


# In[40]:


plt.bar(df["Gender"],df["Salary"])


# Observation:
# males had highest salary

# # Which designation has the highest salary?

# In[41]:


d=list(df["Designation"])


# In[42]:


list=np.array(d)


# In[43]:


s=np.unique(list)


# In[44]:


s


# In[45]:


max_sal=df.groupby('Designation')["Salary"].max()


# In[46]:


max_sal


# In[47]:


max_sal.idxmax()


# In[48]:


f=df[df["Designation"]=='automation engineer']


# In[49]:


f["Salary"].max()


# In[50]:


df.info()


# In[51]:


year=df["DOJ"].value_counts()


# In[52]:


year


# In[53]:


sns.scatterplot(year)
plt.xlabel("Year")
plt.ylabel("Count")
plt.figure(figsize=(10, 5))
plt.show()


# # Bonus questions
# 

# # Times of India article dated Jan 18, 2019 states that “After doing your Computer Science Engineering if you take up jobs as a Programming Analyst, Software Engineer, Hardware Engineer and Associate Engineer you can earn up to 2.5-3 lakhs as a fresh graduate.” Test this claim with the data given to you.
# 

# In[83]:


avg_sal= df[df['Designation'].str.contains('Software Engineer', case=False)]


# In[85]:


avg_sal["Salary"].mean()


# In[86]:


avg_sal1= df[df['Designation'].str.contains('Hardware Engineer', case=False)]


# In[87]:


avg_sal1["Salary"].mean()


# In[89]:


avg_sal2= df[df['Designation'].str.contains('Associate Engineer', case=False)]


# In[90]:


avg_sal2["Salary"].mean()


# In[91]:


avg_sal3= df[df['Designation'].str.contains('Programming Analyst', case=False)]


# In[95]:


avg_sal3["Salary"].mean()


# # 2. Is there a relationship between gender and specialization? (i.e. Does the preference of Specialization depend on the Gender?)
# 

# In[136]:


males_df=df[df["Gender"]=="m"]
males_df


# In[99]:


males_df
specialization=males_df["Specialization"].value_counts()
specialization


# In[137]:


specialization=males_df["Specialization"].value_counts()
s=specialization.idxmax()
n_m=specialization.max()
print(s,n_m)


# In[138]:


females_df=df[df["Gender"]=="f"]
specialization=females_df["Specialization"].value_counts()
s_f=specialization.idxmax()
n_f=specialization.max()
print(s_f,n_f)


# In[ ]:




