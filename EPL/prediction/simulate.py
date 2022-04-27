from data_clean import history, ave, ave_away, ave_home, teams
from scipy.stats import poisson



# Get score of a match

def get_score(home, away):
    game_score = history.loc[(history['HomeTeam'] == home) & (history['AwayTeam'] == away) ]
    # Only use this method if we have at least 4 matches
    if len(game_score) > 3 :
       # print('yeah, there are more than 3')
        h_scored = poisson.cdf(k=ave_home/90,mu=game_score['FTHG'].mean())
        a_scored = poisson.cdf(k=ave_away/90,mu=game_score['FTAG'].mean())
        print(len(game_score))
    
    return [h_scored, a_scored]

ave_score = get_score('Man United','Liverpool')
print(ave_score)