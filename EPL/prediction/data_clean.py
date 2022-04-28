"""
Python script to load and clean the data
@author: jartavia05
source: Historical results: https://www.kaggle.com/datasets/irkaal/english-premier-league-results

"""


from itertools import count
import pandas as pd


history = pd.read_csv('EPL/dataset/epl_history.csv')
teams = pd.unique(history['HomeTeam'])

# Get the history file filtered by seasons from 2010 to 2022. 
seasons = []
for x in list(range(10,22)): seasons.append('{}-{}'.format(2000+x,x+1))
history = history.loc[history['Season'].isin(seasons)]

# Calculate the average goals
ave_home = history['FTHG'].mean()
ave_away = history['FTAG'].mean()
ave = history['FTHG'].mean() + history['FTAG'].mean()

print(teams)
