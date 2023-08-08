#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


titanic=sns.load_dataset('titanic')
titanic


# # Age of titanic people
# 

# In[5]:


sns.kdeplot(data=titanic,x='age',hue='class',multiple='stack',palette='Greens')
plt.title('Age of titanic people',color='green',fontweight='bold',fontsize=20)
plt.xlabel('Age',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel("denstiy",color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # prices according to gender
# 

# In[7]:


sns.histplot(data=titanic,x='fare',binwidth=25,kde=True,hue='sex',palette='hot')
plt.title('fare of trip',color='green',fontweight='bold',fontsize=20)
plt.xlabel('fare',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel("count",color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # ages according to class

# In[8]:


sns.histplot(data=titanic,x='age',hue='pclass',kde=True,palette='seismic')
plt.title('Age vs class',color='blue',fontweight='bold',fontsize=20)
plt.xlabel('Age',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel("count",color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # titanic people

# In[9]:


sns.kdeplot(data=titanic,x='survived',hue='who')
plt.title('titanic people',color='green',fontweight='bold',fontsize=20)
plt.xlabel('survived',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel("denstiy",color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # titanic people according to gender

# In[77]:


sns.relplot(data=titanic,x='survived',y='age',kind='line',hue='who',col='sex',)
plt.show()


# # people according to embark town
# 

# In[46]:


sns.histplot(data=titanic,x='age',hue='embark_town',kde=True,linewidth=2,palette='plasma',multiple='stack')
plt.title('Age vs embark town',color='blue',fontweight='bold',fontsize=20)
plt.xlabel('Age',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel("count",color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # people according to age
# 

# In[74]:


sns.histplot(data=titanic,x='age',multiple='layer',kde=True)
plt.title('people vs age',color='blue',fontweight='bold',fontsize=20)
plt.xlabel('age',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel('count',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # people according to survived
# 

# In[73]:


sns.histplot(data=titanic,x='age',hue='survived',palette="spring",multiple="dodge")
plt.title(' people vs survived',color='green',fontweight='bold',fontsize=20)
plt.xlabel('Survived',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel('Age',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# In[12]:


male_surv=titanic[(titanic['survived']==1)&(titanic['who']=='man')]
male_surv


# # survied male according to class

# In[14]:


sns.scatterplot(data=male_surv,x='survived',y='age',hue='class',palette='cool')
plt.title("Survived male according to class",color='green',fontweight='bold',fontsize=20)
plt.xlabel('Survived',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel("Age",color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # survived male according to embark town
# 

# In[15]:


sns.relplot(data=male_surv,x='survived',y='age',hue='embark_town',palette='winter',kind='scatter')
plt.title("Survived male according to embark town",color='green',fontweight='bold',fontsize=20)
plt.xlabel('Survived',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel("Age",color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# In[16]:


female_surv=titanic[(titanic['survived']==1)&(titanic['who']=='woman')]
female_surv


# # survived women according to age

# In[24]:


sns.kdeplot(data=female_surv,x='age',linewidth=2)
plt.title('survived women vs age',color='green',fontweight='bold',fontsize=20)
plt.xlabel('age',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel('density',color='green',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # survived women according  to class 

# In[62]:


sns.histplot(data=female_surv,x='age',hue="class",palette='spring',multiple='dodge')
plt.title('survived women vs class',color='blue',fontweight='bold',fontsize=20)
plt.xlabel('age',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel('count',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # survived women according to age

# In[60]:


sns.histplot(data=female_surv,x='age',hue='embark_town',multiple='dodge',kde=True,linewidth=2)
plt.title('survived women vs age',color='blue',fontweight='bold',fontsize=20)
plt.xlabel('age',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel('count',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# # survived women according to embark town

# In[49]:


sns.histplot(data=female_surv,x='age',hue='embark_town',multiple='dodge',kde=True,)
plt.title('survived women vs embark town',color='blue',fontweight='bold',fontsize=20)
plt.xlabel('age',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.ylabel('count',color='blue',fontweight='bold',fontsize=14,labelpad=10)
plt.show()


# In[76]:


plt.pie(titanic['survived'].value_counts(),labels=['alive','dead'],shadow=True,explode=[0.2,0],autopct="%.0f%%")
plt.show()


# In[ ]:




