"""
Python script to predict a English Premier League match result based on poisson distribution
@author: jartavia05

"""

from data_clean import history
from scipy.stats import poisson
import matplotlib.pyplot as plt
import pandas as pd


def get_match_score(home, away, nsim):
    teams_history = history.loc[(history['HomeTeam'] == home) & (history['AwayTeam'] == away) ]
    ave_h_s = 0 if teams_history['FTHG'].empty else teams_history['FTHG'].mean()
    ave_a_s = 0 if teams_history['FTAG'].empty else teams_history['FTAG'].mean()

    # Stats of the Home Team
    t_ave_h_s = 0 if teams_history['FTHG'].empty else teams_history['FTHG'].loc[history['HomeTeam'] == home].mean()
    t_ave_h_c = 0 if teams_history['FTAG'].empty else teams_history['FTAG'].loc[history['HomeTeam'] == home].mean()

    # Stats of the Away Team
    t_ave_a_s = 0 if teams_history['FTAG'].empty else teams_history['FTAG'].loc[history['AwayTeam'] == away].mean()
    t_ave_a_c = 0 if teams_history['FTHG'].empty else teams_history['FTHG'].loc[history['AwayTeam'] == away].mean()
  
    goals = []
    score_pred = []
    score_prob = []
    for i in range(nsim):  
        if len(teams_history) > 3 :            
            for j in range(nsim):
                goals.append(i)
                score_pred.append('"{}-{}"'.format(i,j))
                score_prob.append(poisson.pmf(k=i,mu=ave_h_s) + poisson.pmf(k=j,mu=ave_a_s))
        else:  # take into account both attacking stat of home and defense stats of away
            for k in range(nsim):
                goals.append(i)
                score_pred.append('{}-{}'.format(i,k))
                score_prob.append(poisson.pmf(k=i,mu=(1/2 * (t_ave_h_s + t_ave_a_c))) + poisson.pmf(k=j,mu=(1/2 * (t_ave_a_s + t_ave_h_c))))

    
    match_score = pd.DataFrame({'Home': home,'Away': away,'Goals': goals, 'score_pred': score_pred, 'prob': score_prob}).sort_values(by='prob', ascending=False).head(5)
    match_score.to_csv('match_simulate_{}_vs_{}.csv'.format(home, away))
    print(match_score)    

    return match_score
        
match_simulate = get_match_score('Man United','Chelsea', 6)
print(match_simulate)

