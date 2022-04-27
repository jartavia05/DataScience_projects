"""
Python script to predict a English Premier League match result based on poisson distribution
@author: jartavia05

"""

from data_clean import history
from scipy.stats import poisson
import matplotlib.pyplot as plt
import pandas as pd



def get_score(home, away, nsim):
    game_score = history.loc[(history['HomeTeam'] == home) & (history['AwayTeam'] == away) ]
    ave_h_s = game_score['FTHG'].mean()
    ave_a_s = game_score['FTAG'].mean()

    # Stats of the Home Team
    t_ave_h_s = history['FTHG'].loc[history['HomeTeam'] == home].mean()
    t_ave_h_c = history['FTAG'].loc[history['HomeTeam'] == home].mean()

    # Stats of the Away Team
    t_ave_a_s = history['FTAG'].loc[history['AwayTeam'] == away].mean()
    t_ave_a_c = history['FTHG'].loc[history['AwayTeam'] == away].mean()
  
    goals = []
    h_scored = [] 
    a_scored = []
    for i in range(nsim):
  
        if len(game_score) > 3 :
            goals.append(i)
            h_scored.append(poisson.pmf(k=i,mu=ave_h_s))
            a_scored.append(poisson.pmf(k=i,mu=ave_a_s))
            
        else:  #take into account both attacking stat of home and defense stats of away
            goals.append(i)
            h_scored.append(poisson.pmf(k=i,mu=(1/2 * (t_ave_h_s + t_ave_a_c))))
            a_scored.append(poisson.pmf(k=i,mu=(1/2 * (t_ave_a_s + t_ave_h_c))))
    
    match_pred = {'Home': home,'Away': away,'Goals': goals, 'HomeScored': h_scored, 'AwayScored':a_scored}
    match_pred_df = pd.DataFrame(match_pred)
    print(match_pred_df)
    match_pred_df.to_csv('match_simulate.csv')

    return h_scored, a_scored
        


match_simulate = get_score('Man United','Chelsea', 6)
print(match_simulate)

