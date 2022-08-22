import pandas as pd
import pytest
from FPL_data_analyze.read_data import *
from FPL_data_analyze.prepare_data import *
from FPL_data_analyze.merge_data import *



###testowanie read_data
def test_reading_data():
    players_dic, gw_dic, oddsy_dic, teams_id_dic = read_all_files(pathfile="C:\\Users\\User\\PycharmProjects\\projekt_zaliczeniowy\\Fantasy-Premier-League-master\\data")
    assert len(players_dic) == 5
    assert len(gw_dic) == 3
    assert len(oddsy_dic) == 5
    assert len(teams_id_dic) == 2

def test_choose_year():
    players_dic, gw_dic, oddsy_dic, teams_id_dic = read_all_files(pathfile="C:\\Users\\User\\PycharmProjects\\projekt_zaliczeniowy\\Fantasy-Premier-League-master\\data")
    players, players_every_game, oddsy, teams_id = choose_year('2019-20',players_dic,gw_dic,oddsy_dic,teams_id_dic)

    isempty_players = players.empty
    isempty_players_every_game = players_every_game.empty
    isempty_oddsy = oddsy.empty
    isempty_teams_id = teams_id.empty

    assert isempty_players == False
    assert isempty_players_every_game == False
    assert isempty_oddsy == False
    assert isempty_teams_id == False


def test_data():
    players_dic, gw_dic, oddsy_dic, teams_id_dic = read_all_files(pathfile="C:\\Users\\User\\PycharmProjects\\projekt_zaliczeniowy\\Fantasy-Premier-League-master\\data")
    players, players_every_game, oddsy, teams_id = choose_year('2016-17',players_dic,gw_dic,oddsy_dic,teams_id_dic)

    assert players_every_game == None
    assert teams_id == None



def test_players_every_game_prepare():
    test_gw = pd.DataFrame([("imie", 3, "2019-08-31T14:00:00Z" ,4 ,5)], columns=['name', 'opponent_team', 'kickoff_time', 'was_home', 'total_points'])
    # test_players = pd.DataFrame([(1, 2), (3, 4)], columns=["A", "B"])
    players_every_game = players_every_game_prepare(test_gw)

    assert players_every_game.shape[1] == 7

def test_teams_id_prepare():
    test_teams_id = pd.DataFrame([(3,"Sheffield Utd"),(4,"Spurs"),(7,'Man Utd')],
                           columns=['id', 'name'])

    id_teams = teams_id_prepare(test_teams_id)
    assert id_teams.iat[0, 1] == 'Sheffield United'
    assert id_teams.iat[1, 1] == 'Tottenham'
    assert id_teams.iat[2, 1] == 'Man United'


def test_players_prepare():
    test_players = pd.DataFrame([("imie", 3, "Karol", "Muck", 5)],
                           columns=['team', 'element_type', 'first_name', 'second_name', 'now_cost'])

    players = players_prepare(test_players)
    print(players)
    assert players.iloc[0]["full_name"] == "Karol Muck"

def test_merge_players_every_game():
    test_players = pd.DataFrame([(1, 3, "Shkodran", "Mustafi", 51, "Shkodran Mustafi")],
                           columns=['team', 'element_type', 'first_name', 'second_name', 'now_cost', 'full_name'])

    test_teams_id = pd.DataFrame([(1, "Liverpool"), (2, "Norwich"), (3, 'Bournemouth')],
                            columns=['id', 'name'])

    test_players_every_game = pd.DataFrame(
        [("Shkodran Mustafi222", 1, "2019-08-31T14:00:00Z", False, 3, "Shkodran Mustafi")],
        columns=['name', 'opponent_team', 'kickoff_time', 'was_home', 'total_points', 'name_clear'])

    test_oddsy = pd.DataFrame([("09/08/2019", "Liverpool", "Liverpool", 1, 2, 3)],
                         columns=['Date', 'HomeTeam', 'AwayTeam', 'AvgH', 'AvgD', 'AvgA'])

    wszystko = merge_players_every_game(test_players_every_game, test_players, test_teams_id, test_oddsy)

    isempty = wszystko.empty

    assert isempty == False
    assert wszystko.shape[1] == 21
