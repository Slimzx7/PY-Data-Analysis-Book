
# coding: utf-8

# In[40]:

import csv
import pandas as pd

names = pd.read_csv('c:Desktop/PY DataAnalysis/ch02/names/yob1880.txt', names = ['Name', 'Sex', 'Births'])
    #f_contents = f.read()
print(names.head(10))


# In[42]:

names.groupby('Sex').Births.sum()


# In[51]:

years = range(1880, 2011)
pieces =[]
columns = ['Name', 'Sex', 'Births']
for year in years:
    path = 'c:Desktop/PY DataAnalysis/ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path, names = columns)
    frame['Year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index=True)


# In[53]:

print(names.head(10))


# In[69]:

total_births = names.pivot_table(columns='Sex', index=['Year'], aggfunc=sum)
print(total_births.head(10))


# In[ ]:



