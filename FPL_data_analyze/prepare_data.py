import pandas as pd
pd.options.mode.chained_assignment = None
# dodanie czystego klucza i połączenie graczy z

# dodanie czystego klucza i połączenie graczy z
def players_every_game_prepare(gw_players):
    # wybor tylko potrzebnych kolumn
    players_every_game = gw_players[['name', 'opponent_team', 'kickoff_time', 'was_home', 'total_points']]

    # dodanie kolumny z datą
    players_every_game['date'] = players_every_game['kickoff_time'].str[:10]

    # usawnienie czasu tak jak w odds
    players_every_game['date'] = pd.to_datetime(players_every_game.date)
    players_every_game['date'] = players_every_game['date'].dt.strftime('%d/%m/%Y')

    # dodanie czystego klucza
    players_every_game = players_every_game.sort_values(by=['name'])
    players_every_game['name_clear'] = players_every_game['name'].str.replace('\d+', '')
    players_every_game['name_clear'] = players_every_game['name_clear'].str[:-1]
    players_every_game['name_clear'] = players_every_game['name_clear'].str.replace('_', ' ')

    return players_every_game


def teams_id_prepare(teams_id):
    teams_id = teams_id[['id', 'name']]

    # zmiana man utd na machester united oraz spurs na tottenham oraz Man United oraz # Sheffield United
    teams_id['name'] = teams_id['name'].replace(['Sheffield Utd'], 'Sheffield United')
    teams_id['name'] = teams_id['name'].replace(['Spurs'], 'Tottenham')
    teams_id['name'] = teams_id['name'].replace(['Man Utd'], 'Man United')

    return teams_id


def odssy_prepare(oddsy):
    oddsy = oddsy[['Date', 'HomeTeam', 'AwayTeam', 'AvgH', 'AvgD', 'AvgA']]
    return oddsy


def players_prepare(players):
    players = players[['team', 'element_type', 'first_name', 'second_name', 'now_cost']]
    players['full_name'] = players[['first_name', 'second_name']].agg(' '.join, axis=1)

    return players
