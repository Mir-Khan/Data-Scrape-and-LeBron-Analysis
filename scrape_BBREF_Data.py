from time import sleep
import requests
import urllib3
from bs4 import BeautifulSoup
import json

# This is also me learning how to web-scrape properly from https://github.com/LearnDataSci/article-resources/blob/master/Ultimate%20Guide%20to%20Web%20Scraping/Part%201%20-%20Requests%20and%20BeautifulSoup/notebook.ipynb

############################Years from User#####################################
user_start_year = 1990  # just want to make sure the start year lets the loop run
user_end_year = 1992  # same story here
loop_cont = True  # a boolean value that'll help the next loop

# 1979 is the last year before the last major statistic, 3-pointers, were actually recorded
while (user_start_year > 1979 or user_end_year < 2020) and loop_cont:
    try:
        user_start_year = int(
            input("What year would you like to start data collection?: "))
        user_end_year = int(
            input("What year would you like to end data collection?: "))
        if user_start_year > 1979 and user_end_year < 2020:
            loop_cont = False
    except ValueError:
        print("Please use an appropriate year. You must use whole numbers and cannot use anything prior to 1979 or after  2019")
        continue

#####################Multiple Advanced Page Scrape###########################
advanced_pages = []
counter = user_start_year
while counter <= user_end_year:
    total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_advanced.html'
    advanced_pages.append(total_input)
    counter += 1

year = user_start_year
data = []


for page in advanced_pages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    for row in rows:
        d = dict()
        # The initial scraping threw back some errors due to the initial structure of the HTML
        if row.select_one('[data-stat=g]').text.strip() != 'G':
            d['Year'] = year
            d['Name'] = row.select_one('[data-stat=player]').text.strip()
            d['Position'] = row.select_one('[data-stat=pos]').text.strip()
            d['Age'] = row.select_one('[data-stat=age]').text.strip()
            d['Team'] = row.select_one('[data-stat=team_id]').text.strip()
            d['Games_Played'] = float(
                row.select_one('[data-stat=g]').text.strip())
            d['Minutes_Played'] = float(
                row.select_one('[data-stat=mp]').text.strip())
            # Some fields gave back empty strings, this is to combat those fields and will be repeated often
            if row.select_one('[data-stat=per]').text.strip() == "":
                d['PER'] = float(0)
            else:
                d['PER'] = float(row.select_one(
                    '[data-stat=per]').text.strip())

            if row.select_one('[data-stat=ts_pct]').text.strip() == "":
                d['TS_Percentage'] = float(0)
            else:
                d['TS_Percentage'] = float(row.select_one(
                    '[data-stat=ts_pct]').text.strip())

            if row.select_one('[data-stat=fg3a_per_fga_pct]').text.strip() == "":
                d['3PAr'] = float(0)
            else:
                d['3PAr'] = float(row.select_one(
                    '[data-stat=fg3a_per_fga_pct]').text.strip())

            if row.select_one('[data-stat=fta_per_fga_pct]').text.strip() == "":
                d['FTr'] = float(0)
            else:
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

            if row.select_one('[data-stat=tov_pct]').text.strip() == "":
                d['TOV_Percentage'] = float(0)
            else:
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
    sleep(3)

with open('advanced_stats.json', 'w') as f:
    json.dump(data, f)

########################Multiple per 36 Pages###################################
per_36_pages = []
counter = user_start_year
while counter <= user_end_year:
    total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_per_minute.html'
    per_36_pages.append(total_input)
    counter += 1

year = user_start_year
data = []

for page in per_36_pages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    for row in rows:
        d = dict()

        if row.select_one('[data-stat=g]').text.strip() != 'G':
            d['Year'] = year
            d['Name'] = row.select_one('[data-stat=player]').text.strip()
            d['Position'] = row.select_one('[data-stat=pos]').text.strip()
            d['Team'] = row.select_one('[data-stat=team_id]').text.strip()
            d['Age'] = row.select_one('[data-stat=age]').text.strip()
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

            if row.select_one('[data-stat=fg_pct]').text.strip() == "":
                d['FG_PCT'] = float(0)
            else:
                d['FG_PCT'] = float(row.select_one(
                    '[data-stat=fg_pct]').text.strip())

            d['3PM_Per_36'] = float(row.select_one(
                '[data-stat=fg3_per_mp]').text.strip())
            d['3PA_Per_36'] = float(row.select_one(
                '[data-stat=fg3a_per_mp]').text.strip())

            if row.select_one('[data-stat=fg3_pct]').text.strip() == "":
                d['3P_PCT'] = float(0)
            else:
                d['3P_PCT'] = float(row.select_one(
                    '[data-stat=fg3_pct]').text.strip())

            d['2PM_Per_36'] = float(row.select_one(
                '[data-stat=fg2_per_mp]').text.strip())
            d['2PA_Per_36'] = float(row.select_one(
                '[data-stat=fg2a_per_mp]').text.strip())

            if row.select_one('[data-stat=fg2_pct]').text.strip() == "":
                d['2P_PCT'] = float(0)
            else:
                d['2P_PCT'] = float(row.select_one(
                    '[data-stat=fg2_pct]').text.strip())

            d['FTM_Per_36'] = float(row.select_one(
                '[data-stat=ft_per_mp]').text.strip())
            d['FTA_Per_36'] = float(row.select_one(
                '[data-stat=fta_per_mp]').text.strip())

            if row.select_one('[data-stat=ft_pct]').text.strip() == "":
                d['FT_PCT'] = float(0)
            else:
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
per_100_poss = []

counter = user_start_year
while counter <= user_end_year:
    total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_per_poss.html'
    per_100_poss.append(total_input)
    counter += 1

year = user_start_year
data = []


for page in per_100_poss:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    for row in rows:
        d = dict()

        if row.select_one('[data-stat=g]').text.strip() != 'G':
            d['Year'] = year
            d['Name'] = row.select_one('[data-stat=player]').text.strip()
            d['Position'] = row.select_one('[data-stat=pos]').text.strip()
            d['Age'] = row.select_one('[data-stat=age]').text.strip()
            d['Team'] = row.select_one('[data-stat=team_id]').text.strip()
            d['Games_Played'] = float(
                row.select_one('[data-stat=g]').text.strip())
            d['Games_Started'] = float(
                row.select_one('[data-stat=gs]').text.strip())
            d['Minutes_Played'] = float(
                row.select_one('[data-stat=mp]').text.strip())
            d['FGM_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=fg_per_poss]').text.strip())
            d['FGA_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=fga_per_poss]').text.strip())

            if row.select_one('[data-stat=fg_pct]').text.strip() == "":
                d['FG_PCT'] = float(0)
            else:
                d['FG_PCT'] = float(row.select_one(
                    '[data-stat=fg_pct]').text.strip())

            d['3PM_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=fg3_per_poss]').text.strip())
            d['3PA_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=fg3a_per_poss]').text.strip())

            if row.select_one('[data-stat=fg3_pct]').text.strip() == "":
                d['3P_PCT'] = float(0)
            else:
                d['3P_PCT'] = float(row.select_one(
                    '[data-stat=fg3_pct]').text.strip())

            d['2PM_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=fg2_per_poss]').text.strip())
            d['2PA_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=fg2a_per_poss]').text.strip())

            if row.select_one('[data-stat=fg2_pct]').text.strip() == "":
                d['2P_PCT'] = float(0)
            else:
                d['2P_PCT'] = float(row.select_one(
                    '[data-stat=fg2_pct]').text.strip())

            d['FTM_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=ft_per_poss]').text.strip())
            d['FTA_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=fta_per_poss]').text.strip())

            if row.select_one('[data-stat=ft_pct]').text.strip() == "":
                d['FT_PCT'] = float(0)
            else:
                d['FT_PCT'] = float(row.select_one(
                    '[data-stat=ft_pct]').text.strip())

            d['DRB_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=drb_per_poss]').text.strip())
            d['ORB_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=orb_per_poss]').text.strip())
            d['TRB_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=trb_per_poss]').text.strip())
            d['AST_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=ast_per_poss]').text.strip())
            d['STL_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=stl_per_poss]').text.strip())
            d['BLK_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=blk_per_poss]').text.strip())
            d['TOV_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=tov_per_poss]').text.strip())
            d['Fouls_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=pf_per_poss]').text.strip())
            d['Points_Per_100_Possessions'] = float(row.select_one(
                '[data-stat=pts_per_poss]').text.strip())

            if row.select_one('[data-stat=off_rtg]').text.strip() == "":
                d['Offensive_Rating'] = float(0)
            else:
                d['Offensive_Rating'] = float(
                    row.select_one('[data-stat=off_rtg]').text.strip())

            if row.select_one('[data-stat=def_rtg]').text.strip() == "":
                d['Defensive_Rating'] = float(0)
            else:
                d['Defensive_Rating'] = float(row.select_one(
                    '[data-stat=def_rtg]').text.strip())

            data.append(d)

    year += 1
    sleep(3)

with open('per_100_possessions.json', 'w') as f:
    json.dump(data, f)

#####################Multiple Total Pages####################################
total_pages = []
counter = user_start_year
while counter <= user_end_year:
    total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_totals.html'
    total_pages.append(total_input)
    counter += 1

year = user_start_year
data = []

for page in total_pages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('tbody tr')

    for row in rows:
        d = dict()

        if row.select_one('[data-stat=g]').text.strip() != 'G':
            d['Year'] = year
            d['Name'] = row.select_one('[data-stat=player]').text.strip()
            d['Position'] = row.select_one('[data-stat=pos]').text.strip()
            d['Age'] = row.select_one('[data-stat=age]').text.strip()
            d['Team'] = row.select_one('[data-stat=team_id]').text.strip()
            d['Games_Played'] = float(
                row.select_one('[data-stat=g]').text.strip())
            d['Games_Started'] = float(
                row.select_one('[data-stat=gs]').text.strip())
            d['Minutes_Played'] = float(
                row.select_one('[data-stat=mp]').text.strip())
            d['FGM_Total'] = float(row.select_one(
                '[data-stat=fg]').text.strip())
            d['FGA_Total'] = float(row.select_one(
                '[data-stat=fga]').text.strip())

            if row.select_one('[data-stat=fg_pct]').text.strip() == "":
                d['FG_PCT'] = float(0)
            else:
                d['FG_PCT'] = float(row.select_one(
                    '[data-stat=fg_pct]').text.strip())

            d['3PM_Total'] = float(row.select_one(
                '[data-stat=fg3]').text.strip())
            d['3PA_Total'] = float(row.select_one(
                '[data-stat=fg3a]').text.strip())

            if row.select_one('[data-stat=fg3_pct]').text.strip() == "":
                d['3P_PCT'] = float(0)
            else:
                d['3P_PCT'] = float(row.select_one(
                    '[data-stat=fg3_pct]').text.strip())

            d['2PM_Total'] = float(row.select_one(
                '[data-stat=fg2]').text.strip())
            d['2PA_Total'] = float(row.select_one(
                '[data-stat=fg2a]').text.strip())

            if row.select_one('[data-stat=fg2_pct]').text.strip() == "":
                d['2P_PCT'] = float(0)
            else:
                d['2P_PCT'] = float(row.select_one(
                    '[data-stat=fg2_pct]').text.strip())

            if row.select_one('[data-stat=efg_pct]').text.strip() == "":
                d['EFG_PCT'] = float(0)
            else:
                d['EFG_PCT'] = float(row.select_one(
                    '[data-stat=efg_pct]').text.strip())

            d['FTM_Total'] = float(row.select_one(
                '[data-stat=ft]').text.strip())
            d['FTA_Total'] = float(row.select_one(
                '[data-stat=fta]').text.strip())

            if row.select_one('[data-stat=ft_pct]').text.strip() == "":
                d['FT_PCT'] = float(0)
            else:
                d['FT_PCT'] = float(row.select_one(
                    '[data-stat=ft_pct]').text.strip())

            d['DRB_Total'] = float(row.select_one(
                '[data-stat=drb]').text.strip())
            d['ORB_Total'] = float(row.select_one(
                '[data-stat=orb]').text.strip())
            d['TRB_Total'] = float(row.select_one(
                '[data-stat=trb]').text.strip())
            d['AST_Total'] = float(row.select_one(
                '[data-stat=ast]').text.strip())
            d['STL_Total'] = float(row.select_one(
                '[data-stat=stl]').text.strip())
            d['BLK_Total'] = float(row.select_one(
                '[data-stat=blk]').text.strip())
            d['TOV_Total'] = float(row.select_one(
                '[data-stat=tov]').text.strip())
            d['Fouls_Total'] = float(row.select_one(
                '[data-stat=pf]').text.strip())
            d['Points_Total'] = float(row.select_one(
                '[data-stat=pts]').text.strip())

            data.append(d)

    year += 1
    sleep(3)

with open('totals.json', 'w') as f:
    json.dump(data, f)
