import pandas as pd

def merge_players_every_game(players_every_game, players, teams_id, oddsy):  # dodanie prerp do nazw

    # dodanie pozycji i teamu
    players_every_game_merged = players_every_game.merge(players, left_on='name_clear', right_on='full_name',
                                                         how='left')

    # podzial na home i away (potrzebne do pozniejszego joinowania)
    players_every_game_merged_home = players_every_game_merged[players_every_game_merged['was_home'] == True]
    players_every_game_merged_away = players_every_game_merged[players_every_game_merged['was_home'] == False]

    # dodanie home team id
    oddsy_merged = oddsy.merge(teams_id, left_on='HomeTeam', right_on='name', how='left').drop('name',
                                                                                               1)  # usuniecie klucza
    oddsy_merged = oddsy_merged.rename(columns={'id': 'id_HomeTeam'})

    # dodanie away team id
    oddsy_merged = oddsy_merged.merge(teams_id, left_on='AwayTeam', right_on='name', how='left').drop('name',
                                                                                                      1)  # usuniecie klucza
    oddsy_merged = oddsy_merged.rename(columns={'id': 'id_AwayTeam'})

    # dodanie home
    wszystko_home = pd.merge(players_every_game_merged_home, oddsy_merged, how='left',
                             left_on=['team', 'opponent_team'], right_on=['id_HomeTeam', 'id_AwayTeam'])

    # nazwanie AVH AVG oraZ AVGA
    wszystko_home = wszystko_home.rename(columns={'AvgH': 'odds_win', 'AvgD': 'odds_draw', 'AvgA': 'odds_lose'})
    wszystko_home = wszystko_home.reindex(sorted(wszystko_home.columns), axis=1)

    # dodanie away
    wszystko_away = pd.merge(players_every_game_merged_away, oddsy_merged, how='left',
                             left_on=['team', 'opponent_team'], right_on=['id_AwayTeam', 'id_HomeTeam'])

    # nazwanie AVH AVG oraZ AVGA
    wszystko_away = wszystko_away.rename(columns={'AvgH': 'odds_lose', 'AvgD': 'odds_draw', 'AvgA': 'odds_win'})
    wszystko_away = wszystko_away.reindex(sorted(wszystko_away.columns), axis=1)

    # poloczenie wszystkiego
    wszystko = pd.concat([wszystko_home, wszystko_away])

    wszystko['prob_win'] = wszystko['odds_win'] - wszystko['odds_draw']

    # usuniecie wierszy ktore sie nie poloczyly
    wszystko = wszystko.dropna()

    return wszystko