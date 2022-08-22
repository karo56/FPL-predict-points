import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def roi_plot(roi_teams):
    avg_roi = roi_teams['roi'].mean()
    plt.figure(figsize=(20, 10))
    plt.bar(roi_teams['name'], roi_teams['roi'])
    plt.axhline(y=avg_roi, color='r', linestyle='-')
    plt.xticks(rotation=60)


def corr_plot(wszystko, possition=1):
    data_to_plot = wszystko[wszystko['element_type'] == possition].reset_index()

    pionts_corr = data_to_plot[['total_points', 'was_home', 'prob_win', 'odds_draw', 'now_cost']]
    corr = pionts_corr.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.title("correlation for {} element type".format(possition))


def super_plot(data):
    minsize = 1
    maxsize = 300

    plt.figure(figsize=(160, 160))

    sns.relplot('now_cost', 'total_points', data=data, hue='team', size='selected_by_percent',
                sizes=(minsize, maxsize))

    for _, row in data[['web_name', 'now_cost', 'total_points', 'selected_by_percent']].iterrows():
        if row['selected_by_percent'] > 8:
            xy = row[['now_cost', 'total_points']]  # /1e6
            xytext = xy + (0.02, 5)
            plt.annotate(row['web_name'], xy, xytext)
    plt.show()