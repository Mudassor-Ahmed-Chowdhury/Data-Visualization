# -*- coding: utf-8 -*-
"""LR DV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nK6hGNEfQojYW02L0G5hYRd8gDv32fzQ
"""

import io
import pandas as pd

from google.colab import files
uploaded = files.upload()

#!pip install -q xlrd

df = pd.read_excel('Video_Store.xlsx')

df

store = pd.read_excel('Video_Store.xlsx') 
print(store.head())





import matplotlib.pyplot as plt

fig, ax = plt.subplots() 

# scatter the income against age
ax.scatter(store['Income'], store['Age'])
# set a title and labels
ax.set_title('Video store Dataset')
ax.set_xlabel('Income')
ax.set_ylabel('Age')

# create color dictionary
colors = {'M':'r', 'F':'b'}
# create a figure and axis
fig, ax = plt.subplots()
# plot each data-point
for i in range(len(store['Age'])):
  ax.scatter(store['Age'][i], store['Income'][i],color=colors[store['Gender'][i]])

# set a title and labels
ax.set_title('Video store Dataset')
ax.set_xlabel('Age')
ax.set_ylabel('Income')

fig, ax = plt.subplots()

# scatter the rentals against income
ax.scatter(store['Rentals'], store['Income'])
# set a title and labels
ax.set_title('Video store Dataset')
ax.set_xlabel('Rentals')
ax.set_ylabel('Income')

colors = {'M':'r', 'F':'b'}

fig, ax = plt.subplots()

for i in range(len(store['Rentals'])):
  ax.scatter(store['Rentals'][i], store['Income'][i],color=colors[store['Gender'][i]])

# set a title and labels
ax.set_title('Video store Dataset')
ax.set_xlabel('Rentals')
ax.set_ylabel('Income')



fig, ax = plt.subplots() 
# scatter the visit against age
ax.scatter(store['AvgPerVisit'], store['Age'])
# set a title and labels
ax.set_title('Video store Dataset')
ax.set_xlabel('AvgPerVisit')
ax.set_ylabel('Age')

colors = {'M':'r', 'F':'b'}

fig, ax = plt.subplots()

for i in range(len(store['AvgPerVisit'])):
  ax.scatter(store['AvgPerVisit'][i], store['Age'][i],color=colors[store['Gender'][i]])

# set a title and labels
ax.set_title('Video store Dataset')
ax.set_xlabel('AvgPerVisit')
ax.set_ylabel('Age')

"""# Line PLot"""

columns = store.columns.drop(['Genre', 'ID', 'Gender'])

columns

columns = store.columns.drop(['Genre', 'ID', 'Gender'])
# create x data
x_data = range(0, store.shape[0])
# create figure and axis
fig, ax = plt.subplots()
# plot each column
for column in columns:
    ax.plot(x_data, store[column], label=column)
# set title and legend
ax.set_title('VideoStore Dataset')
ax.legend()

columns

x_data

store.shape[1]

#Histogram
df.plot.hist(subplots=True, layout=(4,4), figsize=(10, 10), bins=20)















