import os
import pandas as pd
pd.options.mode.chained_assignment = None                                                                                                                                                                                                                                                                               

def read_all_files(pathfile="C:\\Users\\User\\PycharmProjects\\projekt_zaliczeniowy\\Fantasy-Premier-League-master\\data"):
    # dodatnie slownika z poszczegolnymi latami
    years = list(os.listdir(pathfile))

    players_dic = {}
    gw_dic = {}
    oddsy_dic = {}
    teams_id_dic = {}

    for subdir, dirs, files in os.walk(pathfile):
        for file in files:

            if file == 'players_raw.csv':
                file_path = os.path.join(subdir, file)
                buff = pd.read_csv(file_path)

                for year in years:
                    if year in file_path:
                        players_dic[year] = buff

            if file == 'merged_gw.csv':
                file_path = os.path.join(subdir, file)
                buff = pd.read_csv(file_path, encoding="ISO-8859-1")

                for year in years:
                    if year in file_path:
                        gw_dic[year] = buff

            if file == 'odds.csv':
                file_path = os.path.join(subdir, file)
                buff = pd.read_csv(file_path, encoding="ISO-8859-1")

                for year in years:
                    if year in file_path:
                        oddsy_dic[year] = buff

            if file == 'teams.csv':
                file_path = os.path.join(subdir, file)
                buff = pd.read_csv(file_path, encoding="ISO-8859-1")

                for year in years:
                    if year in file_path:
                        teams_id_dic[year] = buff

    return players_dic, gw_dic, oddsy_dic, teams_id_dic



def choose_year(year, players_dic, gw_dic, oddsy_dic, teams_id_dic):
    try:
        players = players_dic[year]
    except:
        players = None
        print("We dont have {} year in players data".format(year))

    try:
        players_every_game = gw_dic[year]
    except:
        players_every_game = None
        print("We dont have {} year in players_raw data".format(year))

    try:
        oddsy = oddsy_dic[year]
    except:
        oddsy = None
        print("We dont have {} year in odds data".format(year))

    try:
        teams_id = teams_id_dic[year]
    except:
        teams_id = None
        print("We dont have {} year in teams_id data".format(year))

    return players, players_every_game, oddsy, teams_id

