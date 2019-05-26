from time import sleep
import requests
import urllib3
from bs4 import BeautifulSoup
import json

# This is also me learning how to web-scrape properly
# Functions taken from https://github.com/LearnDataSci/article-resources/blob/master/Ultimate%20Guide%20to%20Web%20Scraping/Part%201%20-%20Requests%20and%20BeautifulSoup/notebook.ipynb

#############################Functions#########################################


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


def open_html(path):
    with open(path, 'rb') as f:
        return f.read()


#####################Multiple Advanced Page Scrape###########################
# Advanced stats from 2010-2018
advanced_pages = [
    r'https://www.basketball-reference.com/leagues/NBA_2010_advanced.html',
    r'https://www.basketball-reference.com/leagues/NBA_2011_advanced.html',
    r'https://www.basketball-reference.com/leagues/NBA_2012_advanced.html',
    r'https://www.basketball-reference.com/leagues/NBA_2013_advanced.html',
    r'https://www.basketball-reference.com/leagues/NBA_2014_advanced.html',
    r'https://www.basketball-reference.com/leagues/NBA_2015_advanced.html',
    r'https://www.basketball-reference.com/leagues/NBA_2016_advanced.html',
    r'https://www.basketball-reference.com/leagues/NBA_2017_advanced.html',
    r'https://www.basketball-reference.com/leagues/NBA_2018_advanced.html'
]

data = []
year = 2010  # This can be changed to whatever the starting year is

for page in advanced_pages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    for row in rows:
        d = dict()
        # The initial scraping threw back some errors, this is to address those specific erros
        if row.select_one('[data-stat=g]').text.strip() != 'G' and row.select_one('[data-stat=per]').text.strip() != "" and row.select_one('[data-stat=ts_pct]').text.strip() != "":
            d['Year'] = year
            d['Name'] = row.select_one('[data-stat=player]').text.strip()
            d['Position'] = row.select_one('[data-stat=pos]').text.strip()
            d['Team'] = row.select_one('[data-stat=team_id]').text.strip()
            d['Games_Played'] = float(
                row.select_one('[data-stat=g]').text.strip())
            d['Minutes_Played'] = float(
                row.select_one('[data-stat=mp]').text.strip())
            d['PER'] = float(row.select_one('[data-stat=per]').text.strip())
            d['TS_Percentage'] = float(row.select_one(
                '[data-stat=ts_pct]').text.strip())
            d['3PAr'] = float(row.select_one(
                '[data-stat=fg3a_per_fga_pct]').text.strip())
            d['FTr'] = float(row.select_one(
                '[data-stat=fta_per_fga_pct]').text.strip())
            d['ORB_Percentage'] = float(row.select_one(
                '[data-stat=orb_pct]').text.strip())
            d['DRB_Percentage'] = float(row.select_one(
                '[data-stat=drb_pct]').text.strip())
            d['TRB_Percentage'] = float(row.select_one(
                '[data-stat=trb_pct]').text.strip())
            d['AST_Percentage'] = float(row.select_one(
                '[data-stat=ast_pct]').text.strip())
            d['STL_Percentage'] = float(row.select_one(
                '[data-stat=stl_pct]').text.strip())
            d['BLK_Percentage'] = float(row.select_one(
                '[data-stat=blk_pct]').text.strip())
            d['TOV_Percentage'] = float(row.select_one(
                '[data-stat=tov_pct]').text.strip())
            d['USG_Percentage'] = float(row.select_one(
                '[data-stat=usg_pct]').text.strip())
            d['OWS'] = float(row.select_one('[data-stat=ows]').text.strip())
            d['DWS'] = float(row.select_one('[data-stat=dws]').text.strip())
            d['WS'] = float(row.select_one('[data-stat=ws]').text.strip())
            d['OBPM'] = float(row.select_one('[data-stat=obpm]').text.strip())
            d['DBPM'] = float(row.select_one('[data-stat=dbpm]').text.strip())
            d['BPM'] = float(row.select_one('[data-stat=bpm]').text.strip())
            d['VORP'] = float(row.select_one('[data-stat=vorp]').text.strip())

            data.append(d)

    year += 1
    sleep(5)

with open('advanced_stats.json', 'w') as f:
    json.dump(data, f)

########################Multiple per 36 Pages###################################
# Per 36 Minutes stats from 2010-2018
per_36_pages = [
    r'https://www.basketball-reference.com/leagues/NBA_2010_per_minute.html',
    r'https://www.basketball-reference.com/leagues/NBA_2011_per_minute.html',
    r'https://www.basketball-reference.com/leagues/NBA_2012_per_minute.html',
    r'https://www.basketball-reference.com/leagues/NBA_2013_per_minute.html',
    r'https://www.basketball-reference.com/leagues/NBA_2014_per_minute.html',
    r'https://www.basketball-reference.com/leagues/NBA_2015_per_minute.html',
    r'https://www.basketball-reference.com/leagues/NBA_2016_per_minute.html',
    r'https://www.basketball-reference.com/leagues/NBA_2017_per_minute.html',
    r'https://www.basketball-reference.com/leagues/NBA_2018_per_minute.html'
]

data = []
year = 2010  # This can be changed to whatever the starting year is

for page in per_36_pages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    for row in rows:
        d = dict()

        if row.select_one('[data-stat=g]').text.strip() != 'G' and row.select_one('[data-stat=fg3_pct]').text.strip() != "" and row.select_one('[data-stat=ft_pct]').text.strip() != "" and row.select_one('[data-stat=fg2_pct]').text.strip() != "":
            d['Year'] = year
            d['Name'] = row.select_one('[data-stat=player]').text.strip()
            d['Position'] = row.select_one('[data-stat=pos]').text.strip()
            d['Team'] = row.select_one('[data-stat=team_id]').text.strip()
            d['Games_Played'] = float(
                row.select_one('[data-stat=g]').text.strip())
            d['Games_Started'] = float(
                row.select_one('[data-stat=gs]').text.strip())
            d['Minutes_Played'] = float(
                row.select_one('[data-stat=mp]').text.strip())
            d['FGM_Per_36'] = float(row.select_one(
                '[data-stat=fg_per_mp]').text.strip())
            d['FGA_Per_36'] = float(row.select_one(
                '[data-stat=fga_per_mp]').text.strip())
            d['FG_PCT'] = float(row.select_one(
                '[data-stat=fg_pct]').text.strip())
            d['3PM_Per_36'] = float(row.select_one(
                '[data-stat=fg3_per_mp]').text.strip())
            d['3PA_Per_36'] = float(row.select_one(
                '[data-stat=fg3a_per_mp]').text.strip())
            d['3P_PCT'] = float(row.select_one(
                '[data-stat=fg3_pct]').text.strip())
            d['2PM_Per_36'] = float(row.select_one(
                '[data-stat=fg2_per_mp]').text.strip())
            d['2PA_Per_36'] = float(row.select_one(
                '[data-stat=fg2a_per_mp]').text.strip())
            d['2P_PCT'] = float(row.select_one(
                '[data-stat=fg2_pct]').text.strip())
            d['FTM_Per_36'] = float(row.select_one(
                '[data-stat=ft_per_mp]').text.strip())
            d['FTA_Per_36'] = float(row.select_one(
                '[data-stat=fta_per_mp]').text.strip())
            d['FT_PCT'] = float(row.select_one(
                '[data-stat=ft_pct]').text.strip())
            d['DRB_Per_36'] = float(row.select_one(
                '[data-stat=drb_per_mp]').text.strip())
            d['ORB_Per_36'] = float(row.select_one(
                '[data-stat=orb_per_mp]').text.strip())
            d['TRB_Per_36'] = float(row.select_one(
                '[data-stat=trb_per_mp]').text.strip())
            d['AST_Per_36'] = float(row.select_one(
                '[data-stat=ast_per_mp]').text.strip())
            d['STL_Per_36'] = float(row.select_one(
                '[data-stat=stl_per_mp]').text.strip())
            d['BLK_Per_36'] = float(row.select_one(
                '[data-stat=blk_per_mp]').text.strip())
            d['TOV_Per_36'] = float(row.select_one(
                '[data-stat=tov_per_mp]').text.strip())
            d['Fouls_Per_36'] = float(row.select_one(
                '[data-stat=pf_per_mp]').text.strip())
            d['Points_Per_36'] = float(row.select_one(
                '[data-stat=pts_per_mp]').text.strip())

            data.append(d)

    year += 1
    sleep(3)

with open('per_36.json', 'w') as f:
    json.dump(data, f)

#####################Multiple per Game Pages####################################
# Per 36 Minutes stats from 2010-2018
per_game = [
    r'https://www.basketball-reference.com/leagues/NBA_2010_per_game.html',
    r'https://www.basketball-reference.com/leagues/NBA_2011_per_game.html',
    r'https://www.basketball-reference.com/leagues/NBA_2012_per_game.html',
    r'https://www.basketball-reference.com/leagues/NBA_2013_per_game.html',
    r'https://www.basketball-reference.com/leagues/NBA_2014_per_game.html',
    r'https://www.basketball-reference.com/leagues/NBA_2015_per_game.html',
    r'https://www.basketball-reference.com/leagues/NBA_2016_per_game.html',
    r'https://www.basketball-reference.com/leagues/NBA_2017_per_game.html',
    r'https://www.basketball-reference.com/leagues/NBA_2018_per_game.html'
]

data = []
year = 2010  # This can be changed to whatever the starting year is

for page in per_game:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    for row in rows:
        d = dict()

        if row.select_one('[data-stat=g]').text.strip() != 'G' and row.select_one('[data-stat=fg3_pct]').text.strip() != "" and row.select_one('[data-stat=ft_pct]').text.strip() != "" and row.select_one('[data-stat=fg2_pct]').text.strip() != "":
            d['Year'] = year
            d['Name'] = row.select_one('[data-stat=player]').text.strip()
            d['Position'] = row.select_one('[data-stat=pos]').text.strip()
            d['Team'] = row.select_one('[data-stat=team_id]').text.strip()
            d['Games_Played'] = float(
                row.select_one('[data-stat=g]').text.strip())
            d['Games_Started'] = float(
                row.select_one('[data-stat=gs]').text.strip())
            d['Minutes_Played_Per_Game'] = float(
                row.select_one('[data-stat=mp_per_g]').text.strip())
            d['FGM_Per_Game'] = float(row.select_one(
                '[data-stat=fg_per_g]').text.strip())
            d['FGA_Per_Game'] = float(row.select_one(
                '[data-stat=fga_per_g]').text.strip())
            d['FG_PCT'] = float(row.select_one(
                '[data-stat=fg_pct]').text.strip())
            d['3PM_Per_Game'] = float(row.select_one(
                '[data-stat=fg3_per_g]').text.strip())
            d['3PA_Per_Game'] = float(row.select_one(
                '[data-stat=fg3a_per_g]').text.strip())
            d['3P_PCT'] = float(row.select_one(
                '[data-stat=fg3_pct]').text.strip())
            d['2PM_Per_Game'] = float(row.select_one(
                '[data-stat=fg2_per_g]').text.strip())
            d['2PA_Per_Game'] = float(row.select_one(
                '[data-stat=fg2a_per_g]').text.strip())
            d['2P_PCT'] = float(row.select_one(
                '[data-stat=fg2_pct]').text.strip())
            d['EFG_PCT'] = float(row.select_one(
                '[data-stat=efg_pct]').text.strip())
            d['FTM_Per_Game'] = float(row.select_one(
                '[data-stat=ft_per_g]').text.strip())
            d['FTA_Per_Game'] = float(row.select_one(
                '[data-stat=fta_per_g]').text.strip())
            d['FT_PCT'] = float(row.select_one(
                '[data-stat=ft_pct]').text.strip())
            d['DRB_Per_Game'] = float(row.select_one(
                '[data-stat=drb_per_g]').text.strip())
            d['ORB_Per_Game'] = float(row.select_one(
                '[data-stat=orb_per_g]').text.strip())
            d['TRB_Per_Game'] = float(row.select_one(
                '[data-stat=trb_per_g]').text.strip())
            d['AST_Per_Game'] = float(row.select_one(
                '[data-stat=ast_per_g]').text.strip())
            d['STL_Per_Game'] = float(row.select_one(
                '[data-stat=stl_per_g]').text.strip())
            d['BLK_Per_Game'] = float(row.select_one(
                '[data-stat=blk_per_g]').text.strip())
            d['TOV_Per_Game'] = float(row.select_one(
                '[data-stat=tov_per_g]').text.strip())
            d['Fouls_Per_Game'] = float(row.select_one(
                '[data-stat=pf_per_g]').text.strip())
            d['Points_Per_Game'] = float(row.select_one(
                '[data-stat=pts_per_g]').text.strip())

            data.append(d)

    year += 1
    sleep(3)

with open('per_game.json', 'w') as f:
    json.dump(data, f)
