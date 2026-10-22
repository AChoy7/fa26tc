import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('/Users/miguelmaliksi/fa26tc/fa26tc/Miguel/PlayerStatistics.csv')
jordan = dataset[(dataset['firstName'] == 'Michael') & (dataset['lastName'] == 'Jordan')]
lebron = dataset[(dataset['firstName'] == 'LeBron') & (dataset['lastName'] == 'James')]

players = pd.concat([jordan, lebron])
players = players[players['gameType'] == 'Regular Season']
players = players[players['numMinutes'] > 0].copy()
players['player'] = players['firstName'] + ' ' + players['lastName']


points = players.groupby('player')['points'].mean().reset_index()
sns.barplot(data=points, x='player', y='points', hue='player')
plt.title('Average Points Per Game')
plt.xlabel('Player')
plt.ylabel('Points')
plt.show()


players['year'] = pd.to_datetime(players['gameDate']).dt.year
yearly = players.groupby(['player', 'year'])['points'].mean().reset_index()
sns.lineplot(data=yearly, x='year', y='points', hue='player')
plt.title('Points Over Time')
plt.xlabel('Year')
plt.ylabel('Average Points')
plt.show()

sns.scatterplot(data=players, x='assists', y='points', hue='player', alpha=0.4)
plt.title('Assists vs Points')
plt.xlabel('Assists')
plt.ylabel('Points')
plt.show()


sns.histplot(data=players, x='points', hue='player', bins=20,
             stat='percent', common_norm=False, alpha=0.5)
plt.title('Points Scored in Games')
plt.xlabel('Points')
plt.ylabel('Percentage of Games')
plt.show()


sns.boxplot(data=players, x='player', y='reboundsTotal', hue='player')
plt.title('Rebounds Per Game')
plt.xlabel('Player')
plt.ylabel('Rebounds')
plt.show()
