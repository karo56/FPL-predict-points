def players_to_plot_prepare(players, teams_id):
    data_to_plot = players[['web_name', 'total_points', 'team', 'now_cost', 'element_type', 'selected_by_percent']]

    # dodanie teams_id
    buff = teams_id[['id', 'name']]
    data_to_plot = data_to_plot.merge(teams_id, left_on='team', right_on='id', how='left').drop('team', 1)
    data_to_plot = data_to_plot.rename(columns={'name': 'team'})

    # podzial na pozycje
    goalkeepers_to_polot = data_to_plot[data_to_plot['element_type'] == 1].reset_index()
    defenders_to_polot = data_to_plot[data_to_plot['element_type'] == 2]
    midfielders_to_polot = data_to_plot[data_to_plot['element_type'] == 3]
    strikers_to_polot = data_to_plot[data_to_plot['element_type'] == 4]

    return goalkeepers_to_polot, defenders_to_polot, midfielders_to_polot, strikers_to_polot


def roi_teams(players, teams_id):
    # wybranie odpowiednich kolumn
    players = players[['web_name', 'total_points', 'team', 'now_cost', 'minutes']]

    # zagrana polowa sezonu 38 *90 /2
    buff = players[players['minutes'] > 1710].reset_index()

    # podzial na teamy
    roi_teams_data = players.groupby(['team']).agg({'total_points': 'sum', 'now_cost': 'sum'}).reset_index()
    roi_teams_data = roi_teams_data.merge(teams_id, left_on='team', right_on='id', how='left').drop(['team', 'id'], 1)

    roi_teams_data['roi'] = roi_teams_data['total_points'] / roi_teams_data['now_cost']

    return roi_teams_data