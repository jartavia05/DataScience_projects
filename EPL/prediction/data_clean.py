"""
Python script to load and clean the data
@author: jartavia05
source: Historical results: https://www.kaggle.com/thefc17/epl-results-19932018

"""


from itertools import count
from statistics import mean
import pandas as pd


history = pd.read_csv('dataset/history.csv')
teams = pd.unique(history['HomeTeam'])

# Get the history file filtered by seasons from 2010 to 2018. 
seasons = []
for x in list(range(10,18)): seasons.append('{}-{}'.format(2000+x,x+1))
history = history.loc[history['Season'].isin(seasons)]

# Calculate the average goals
ave_home = history['FTHG'].mean()
ave_away = history['FTAG'].mean()
ave = mean(history['FTHG'] + history['FTAG'])


print(teams)
#print(ave_home)
#print(ave_away)
#print(ave)
