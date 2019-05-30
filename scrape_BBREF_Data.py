from time import sleep
import requests
import urllib3
from bs4 import BeautifulSoup
import json
import choice

# Functions


def userYears():
    user_start_year = 1990  # just want to initialize this variable for the while loop
    user_end_year = 1992  # same story here
    loop_cont = True  # a boolean value that'll help the next loop

    while loop_cont:
        try:
            start = int(
                input("What year would you like to start data collection?: "))
            end = int(
                input("What year would you like to end data collection?: "))
            if user_start_year > 1979 and user_end_year < 2020:
                loop_cont = False
        except ValueError:
            print("Please use an appropriate year. You must use whole numbers and cannot use anything prior to 1979 or after  2019")
            continue

    return start, end


def per_game_scrape(reg_play, start_year, end_year):
    tp = "perG"
    page_list = list_creator(reg_play, start_year, end_year, tp)

    def actual_scrape(start_year, end_year, page_list, fileNameEnd):
        data = []
        file_start = start_year  # did this for the file name
        for page in page_list:
            r = requests.get(page)
            soup = BeautifulSoup(r.content, 'html.parser')
            rows = soup.select('tbody tr')

            for row in rows:
                d = dict()

                if row.select_one('[data-stat=g]').text.strip() != 'G':
                    d['Year'] = start_year
                    d['Name'] = row.select_one(
                        '[data-stat=player]').text.strip()
                    d['Position'] = row.select_one(
                        '[data-stat=pos]').text.strip()
                    d['Age'] = row.select_one('[data-stat=age]').text.strip()
                    d['Team'] = row.select_one(
                        '[data-stat=team_id]').text.strip()
                    d['Games_Played'] = float(
                        row.select_one('[data-stat=g]').text.strip())
                    d['Games_Started'] = float(
                        row.select_one('[data-stat=gs]').text.strip())

                    if row.select_one('[data-stat=mp_per_g]').text.strip() == "":
                        d['Minutes_Played_Per_Game'] = float(0)
                    else:
                        d['Minutes_Played_Per_Game'] = float(
                            row.select_one('[data-stat=mp_per_g]').text.strip())

                    if row.select_one('[data-stat=fg_per_g]').text.strip() == "":
                        d['FGM_Per_Game'] = float(0)
                    else:
                        d['FGM_Per_Game'] = float(row.select_one(
                            '[data-stat=fg_per_g]').text.strip())

                    if row.select_one('[data-stat=fga_per_g]').text.strip() == "":
                        d['FGA_Per_Game'] = float(0)
                    else:
                        d['FGA_Per_Game'] = float(row.select_one(
                            '[data-stat=fga_per_g]').text.strip())

                    if row.select_one('[data-stat=fg_pct]').text.strip() == "":
                        d['FG_PCT'] = float(0)
                    else:
                        d['FG_PCT'] = float(row.select_one(
                            '[data-stat=fg_pct]').text.strip())

                    if row.select_one('[data-stat=fg3_per_g]').text.strip() == "":
                        d['3PM_Per_Game'] = float(0)
                    else:
                        d['3PM_Per_Game'] = float(row.select_one(
                            '[data-stat=fg3_per_g]').text.strip())

                    if row.select_one('[data-stat=fg3a_per_g]').text.strip() == "":
                        d['3PA_Per_Game'] = float(0)
                    else:
                        d['3PA_Per_Game'] = float(row.select_one(
                            '[data-stat=fg3a_per_g]').text.strip())

                    if row.select_one('[data-stat=fg3_pct]').text.strip() == "":
                        d['3P_PCT'] = float(0)
                    else:
                        d['3P_PCT'] = float(row.select_one(
                            '[data-stat=fg3_pct]').text.strip())

                    if row.select_one('[data-stat=fg2_per_g]').text.strip() == "":
                        d['2PM_Per_Game'] = float(0)
                    else:
                        d['2PM_Per_Game'] = float(row.select_one(
                            '[data-stat=fg2_per_g]').text.strip())

                    if row.select_one('[data-stat=fg2a_per_g]').text.strip() == "":
                        d['2PA_Per_Game'] = float(0)
                    else:
                        d['2PA_Per_Game'] = float(row.select_one(
                            '[data-stat=fg2a_per_g]').text.strip())

                    if row.select_one('[data-stat=fg2_pct]').text.strip() == "":
                        d['2P_PCT'] = float(0)
                    else:
                        d['2P_PCT'] = float(row.select_one(
                            '[data-stat=fg2_pct]').text.strip())

                    if row.select_one('[data-stat=ft_per_g]').text.strip() == "":
                        d['FTM_Per_Game'] = float(0)
                    else:
                        d['FTM_Per_Game'] = float(row.select_one(
                            '[data-stat=ft_per_g]').text.strip())

                    if row.select_one('[data-stat=fta_per_g]').text.strip() == "":
                        d['FTA_Per_Game'] = float(0)
                    else:
                        d['FTA_Per_Game'] = float(row.select_one(
                            '[data-stat=fta_per_g]').text.strip())

                    if row.select_one('[data-stat=ft_pct]').text.strip() == "":
                        d['FT_PCT'] = float(0)
                    else:
                        d['FT_PCT'] = float(row.select_one(
                            '[data-stat=ft_pct]').text.strip())

                    if row.select_one('[data-stat=drb_per_g]').text.strip() == "":
                        d['DRB_Per_Game'] = float(0)
                    else:
                        d['DRB_Per_Game'] = float(row.select_one(
                            '[data-stat=drb_per_g]').text.strip())

                    if row.select_one('[data-stat=orb_per_g]').text.strip() == "":
                        d['ORB_Per_Game'] = float(0)
                    else:
                        d['ORB_Per_Game'] = float(row.select_one(
                            '[data-stat=orb_per_g]').text.strip())

                    if row.select_one('[data-stat=trb_per_g]').text.strip() == "":
                        d['TRB_Per_Game'] = float(0)
                    else:
                        d['TRB_Per_Game'] = float(row.select_one(
                            '[data-stat=trb_per_g]').text.strip())

                    if row.select_one('[data-stat=ast_per_g]').text.strip() == "":
                        d['AST_Per_Game'] = float(0)
                    else:
                        d['AST_Per_Game'] = float(row.select_one(
                            '[data-stat=ast_per_g]').text.strip())

                    if row.select_one('[data-stat=stl_per_g]').text.strip() == "":
                        d['STL_Per_Game'] = float(0)
                    else:
                        d['STL_Per_Game'] = float(row.select_one(
                            '[data-stat=stl_per_g]').text.strip())

                    if row.select_one('[data-stat=blk_per_g]').text.strip() == "":
                        d['BLK_Per_Game'] = float(0)
                    else:
                        d['BLK_Per_Game'] = float(row.select_one(
                            '[data-stat=blk_per_g]').text.strip())

                    if row.select_one('[data-stat=tov_per_g]').text.strip() == "":
                        d['TOV_Per_Game'] = float(0)
                    else:
                        d['TOV_Per_Game'] = float(row.select_one(
                            '[data-stat=tov_per_g]').text.strip())

                    if row.select_one('[data-stat=pf_per_g]').text.strip() == "":
                        d['Fouls_Per_Game'] = float(0)
                    else:
                        d['Fouls_Per_Game'] = float(row.select_one(
                            '[data-stat=pf_per_g]').text.strip())

                    if row.select_one('[data-stat=pts_per_g]').text.strip() == "":
                        d['Points_Per_Game'] = float(0)
                    else:
                        d['Points_Per_Game'] = float(row.select_one(
                            '[data-stat=pts_per_g]').text.strip())

                    data.append(d)

            start_year += 1
            sleep(3)

        with open(f'{file_start}-{end_year}_per_game_{fileNameEnd}.json', 'w') as f:
            json.dump(data, f)
        return

    if reg_play == "Both":
        cntr = 0
        nameEnd = 'regular_season'
        while cntr < 2:
            actual_scrape(start_year, end_year, page_list[cntr], nameEnd)
            # since the second list will always be a list with playoffs, we can do this
            nameEnd = 'playoffs'
            cntr += 1
    elif reg_play == "Regular Season":
        actual_scrape(start_year, end_year, page_list, 'regular_season')
    elif reg_play == "Playoffs":
        actual_scrape(start_year, end_year, page_list, 'playoffs')
    return


def advanced_scrape(reg_play, start_year, end_year):
    tp = "adv"
    page_list = list_creator(reg_play, start_year, end_year, tp)

    def actual_scrape(start_year, end_year, page_list, fileNameEnd):
        data = []
        file_start = start_year  # did this for the file name
        for page in page_list:
            r = requests.get(page)
            soup = BeautifulSoup(r.content, 'html.parser')
            rows = soup.select('tbody tr')

            for row in rows:
                d = dict()
                # The initial scraping threw back some errors due to the initial structure of the HTML
                if row.select_one('[data-stat=g]').text.strip() != 'G':
                    d['Year'] = start_year
                    d['Name'] = row.select_one(
                        '[data-stat=player]').text.strip()
                    d['Position'] = row.select_one(
                        '[data-stat=pos]').text.strip()
                    d['Age'] = row.select_one('[data-stat=age]').text.strip()
                    d['Team'] = row.select_one(
                        '[data-stat=team_id]').text.strip()
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

                    if row.select_one('[data-stat=orb_pct]').text.strip() == "":
                        d['ORB_Percentage'] = float(0)
                    else:
                        d['ORB_Percentage'] = float(row.select_one(
                            '[data-stat=orb_pct]').text.strip())

                    if row.select_one('[data-stat=drb_pct]').text.strip() == "":
                        d['DRB_Percentage'] = float(0)
                    else:
                        d['DRB_Percentage'] = float(row.select_one(
                            '[data-stat=drb_pct]').text.strip())

                    if row.select_one('[data-stat=trb_pct]').text.strip() == "":
                        d['TRB_Percentage'] = float(0)
                    else:
                        d['TRB_Percentage'] = float(row.select_one(
                            '[data-stat=trb_pct]').text.strip())

                    if row.select_one('[data-stat=ast_pct]').text.strip() == "":
                        d['AST_Percentage'] = float(0)
                    else:
                        d['AST_Percentage'] = float(row.select_one(
                            '[data-stat=ast_pct]').text.strip())

                    if row.select_one('[data-stat=stl_pct]').text.strip() == "":
                        d['STL_Percentage'] = float(0)
                    else:
                        d['STL_Percentage'] = float(row.select_one(
                            '[data-stat=stl_pct]').text.strip())

                    if row.select_one('[data-stat=blk_pct]').text.strip() == "":
                        d['BLK_Percentage'] = float(0)
                    else:
                        d['BLK_Percentage'] = float(row.select_one(
                            '[data-stat=blk_pct]').text.strip())

                    if row.select_one('[data-stat=tov_pct]').text.strip() == "":
                        d['TOV_Percentage'] = float(0)
                    else:
                        d['TOV_Percentage'] = float(row.select_one(
                            '[data-stat=tov_pct]').text.strip())

                    if row.select_one('[data-stat=usg_pct]').text.strip() == "":
                        d['USG_Percentage'] = float(0)
                    else:
                        d['USG_Percentage'] = float(row.select_one(
                            '[data-stat=usg_pct]').text.strip())

                    d['OWS'] = float(row.select_one(
                        '[data-stat=ows]').text.strip())
                    d['DWS'] = float(row.select_one(
                        '[data-stat=dws]').text.strip())
                    d['WS'] = float(row.select_one(
                        '[data-stat=ws]').text.strip())
                    d['OBPM'] = float(row.select_one(
                        '[data-stat=obpm]').text.strip())
                    d['DBPM'] = float(row.select_one(
                        '[data-stat=dbpm]').text.strip())
                    d['BPM'] = float(row.select_one(
                        '[data-stat=bpm]').text.strip())
                    d['VORP'] = float(row.select_one(
                        '[data-stat=vorp]').text.strip())

                    data.append(d)

            start_year += 1
            sleep(3)

        with open(f'{file_start}-{end_year}_advanced_stats_{fileNameEnd}.json', 'w') as f:
            json.dump(data, f)
        return

    if reg_play == "Both":
        cntr = 0
        nameEnd = 'regular_season'
        while cntr < 2:
            actual_scrape(start_year, end_year, page_list[cntr], nameEnd)
            # since the second list will always be a list with playoffs, we can do this
            nameEnd = 'playoffs'
            cntr += 1
    elif reg_play == "Regular Season":
        actual_scrape(start_year, end_year, page_list, 'regular_season')
    elif reg_play == "Playoffs":
        actual_scrape(start_year, end_year, page_list, 'playoffs')
    return


def per_36_scrape(reg_play, start_year, end_year):
    tp = "per36"
    page_list = list_creator(reg_play, start_year, end_year, tp)

    def actual_scrape(start_year, end_year, page_list, fileNameEnd):
        data = []
        file_start = start_year  # did this for the file name
        for page in page_list:
            r = requests.get(page)
            soup = BeautifulSoup(r.content, 'html.parser')
            rows = soup.select('tbody tr')

            for row in rows:
                d = dict()

                if row.select_one('[data-stat=g]').text.strip() != 'G':
                    d['Year'] = start_year
                    d['Name'] = row.select_one(
                        '[data-stat=player]').text.strip()
                    d['Position'] = row.select_one(
                        '[data-stat=pos]').text.strip()
                    d['Team'] = row.select_one(
                        '[data-stat=team_id]').text.strip()
                    d['Age'] = row.select_one('[data-stat=age]').text.strip()
                    d['Games_Played'] = float(
                        row.select_one('[data-stat=g]').text.strip())
                    d['Games_Started'] = float(
                        row.select_one('[data-stat=gs]').text.strip())
                    d['Minutes_Played'] = float(
                        row.select_one('[data-stat=mp]').text.strip())

                    if row.select_one('[data-stat=fg_per_mp]').text.strip() == "":
                        d['FGM_Per_36'] = float(0)
                    else:
                        d['FGM_Per_36'] = float(row.select_one(
                            '[data-stat=fg_per_mp]').text.strip())

                    if row.select_one('[data-stat=fga_per_mp]').text.strip() == "":
                        d['FGA_Per_36'] = float(0)
                    else:
                        d['FGA_Per_36'] = float(row.select_one(
                            '[data-stat=fga_per_mp]').text.strip())

                    if row.select_one('[data-stat=fg_pct]').text.strip() == "":
                        d['FG_PCT'] = float(0)
                    else:
                        d['FG_PCT'] = float(row.select_one(
                            '[data-stat=fg_pct]').text.strip())

                    if row.select_one('[data-stat=fg3_per_mp]').text.strip() == "":
                        d['3PM_Per_36'] = float(0)
                    else:
                        d['3PM_Per_36'] = float(row.select_one(
                            '[data-stat=fg3_per_mp]').text.strip())

                    if row.select_one('[data-stat=fg3a_per_mp]').text.strip() == "":
                        d['3PA_Per_36'] = float(0)
                    else:
                        d['3PA_Per_36'] = float(row.select_one(
                            '[data-stat=fg3a_per_mp]').text.strip())

                    if row.select_one('[data-stat=fg3_pct]').text.strip() == "":
                        d['3P_PCT'] = float(0)
                    else:
                        d['3P_PCT'] = float(row.select_one(
                            '[data-stat=fg3_pct]').text.strip())

                    if row.select_one('[data-stat=fg2_per_mp]').text.strip() == "":
                        d['2PM_Per_36'] = float(0)
                    else:
                        d['2PM_Per_36'] = float(row.select_one(
                            '[data-stat=fg2_per_mp]').text.strip())

                    if row.select_one('[data-stat=fg2a_per_mp]').text.strip() == "":
                        d['2PA_Per_36'] = float(0)
                    else:
                        d['2PA_Per_36'] = float(row.select_one(
                            '[data-stat=fg2a_per_mp]').text.strip())

                    if row.select_one('[data-stat=fg2_pct]').text.strip() == "":
                        d['2P_PCT'] = float(0)
                    else:
                        d['2P_PCT'] = float(row.select_one(
                            '[data-stat=fg2_pct]').text.strip())

                    if row.select_one('[data-stat=ft_per_mp]').text.strip() == "":
                        d['FTM_Per_36'] = float(0)
                    else:
                        d['FTM_Per_36'] = float(row.select_one(
                            '[data-stat=ft_per_mp]').text.strip())

                    if row.select_one('[data-stat=fta_per_mp]').text.strip() == "":
                        d['FTA_Per_36'] = float(0)
                    else:
                        d['FTA_Per_36'] = float(row.select_one(
                            '[data-stat=fta_per_mp]').text.strip())

                    if row.select_one('[data-stat=ft_pct]').text.strip() == "":
                        d['FT_PCT'] = float(0)
                    else:
                        d['FT_PCT'] = float(row.select_one(
                            '[data-stat=ft_pct]').text.strip())

                    if row.select_one('[data-stat=drb_per_mp]').text.strip() == "":
                        d['DRB_Per_36'] = float(0)
                    else:
                        d['DRB_Per_36'] = float(row.select_one(
                            '[data-stat=drb_per_mp]').text.strip())

                    if row.select_one('[data-stat=orb_per_mp]').text.strip() == "":
                        d['ORB_Per_36'] = float(0)
                    else:
                        d['ORB_Per_36'] = float(row.select_one(
                            '[data-stat=orb_per_mp]').text.strip())

                    if row.select_one('[data-stat=trb_per_mp]').text.strip() == "":
                        d['TRB_Per_36'] = float(0)
                    else:
                        d['TRB_Per_36'] = float(row.select_one(
                            '[data-stat=trb_per_mp]').text.strip())

                    if row.select_one('[data-stat=ast_per_mp]').text.strip() == "":
                        d['AST_Per_36'] = float(0)
                    else:
                        d['AST_Per_36'] = float(row.select_one(
                            '[data-stat=ast_per_mp]').text.strip())

                    if row.select_one('[data-stat=stl_per_mp]').text.strip() == "":
                        d['STL_Per_36'] = float(0)
                    else:
                        d['STL_Per_36'] = float(row.select_one(
                            '[data-stat=stl_per_mp]').text.strip())

                    if row.select_one('[data-stat=blk_per_mp]').text.strip() == "":
                        d['BLK_Per_36'] = float(0)
                    else:
                        d['BLK_Per_36'] = float(row.select_one(
                            '[data-stat=blk_per_mp]').text.strip())

                    if row.select_one('[data-stat=tov_per_mp]').text.strip() == "":
                        d['TOV_Per_36'] = float(0)
                    else:
                        d['TOV_Per_36'] = float(row.select_one(
                            '[data-stat=tov_per_mp]').text.strip())

                    if row.select_one('[data-stat=pf_per_mp]').text.strip() == "":
                        d['Fouls_Per_36'] = float(0)
                    else:
                        d['Fouls_Per_36'] = float(row.select_one(
                            '[data-stat=pf_per_mp]').text.strip())

                    if row.select_one('[data-stat=pts_per_mp]').text.strip() == "":
                        d['Points_Per_36'] = float(0)
                    else:
                        d['Points_Per_36'] = float(row.select_one(
                            '[data-stat=pts_per_mp]').text.strip())

                    data.append(d)

            start_year += 1
            sleep(3)

        with open(f'{file_start}-{end_year}_per_36_{fileNameEnd}.json', 'w') as f:
            json.dump(data, f)
        return

    if reg_play == "Both":
        cntr = 0
        nameEnd = 'regular_season'
        while cntr < 2:
            actual_scrape(start_year, end_year, page_list[cntr], nameEnd)
            # since the second list will always be a list with playoffs, we can do this
            nameEnd = 'playoffs'
            cntr += 1
    elif reg_play == "Regular Season":
        actual_scrape(start_year, end_year, page_list, 'regular_season')
    elif reg_play == "Playoffs":
        actual_scrape(start_year, end_year, page_list, 'playoffs')

    return


def per_100_scrape(reg_play, start_year, end_year):
    tp = "per100"
    page_list = list_creator(reg_play, start_year, end_year, tp)

    def actual_scrape(start_year, end_year, page_list, fileNameEnd):
        data = []
        file_start = start_year  # did this for the file name
        for page in page_list:
            r = requests.get(page)
            soup = BeautifulSoup(r.content, 'html.parser')
            rows = soup.select('tbody tr')

            for row in rows:
                d = dict()

                if row.select_one('[data-stat=g]').text.strip() != 'G':
                    d['Year'] = start_year
                    d['Name'] = row.select_one(
                        '[data-stat=player]').text.strip()
                    d['Position'] = row.select_one(
                        '[data-stat=pos]').text.strip()
                    d['Age'] = row.select_one('[data-stat=age]').text.strip()
                    d['Team'] = row.select_one(
                        '[data-stat=team_id]').text.strip()
                    d['Games_Played'] = float(
                        row.select_one('[data-stat=g]').text.strip())
                    d['Games_Started'] = float(
                        row.select_one('[data-stat=gs]').text.strip())
                    d['Minutes_Played'] = float(
                        row.select_one('[data-stat=mp]').text.strip())

                    if row.select_one('[data-stat=fg_per_poss]').text.strip() == "":
                        d['FGM_Per_100_Posessions'] = float(0)
                    else:
                        d['FGM_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=fg_per_poss]').text.strip())

                    if row.select_one('[data-stat=fga_per_poss]').text.strip() == "":
                        d['FGA_Per_100_Posessions'] = float(0)
                    else:
                        d['FGA_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=fga_per_poss]').text.strip())

                    if row.select_one('[data-stat=fg_pct]').text.strip() == "":
                        d['FG_PCT'] = float(0)
                    else:
                        d['FG_PCT'] = float(row.select_one(
                            '[data-stat=fg_pct]').text.strip())

                    if row.select_one('[data-stat=fg3_per_poss]').text.strip() == "":
                        d['3PM_Per_100_Posessions'] = float(0)
                    else:
                        d['3PM_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=fg3_per_poss]').text.strip())

                    if row.select_one('[data-stat=fg3a_per_poss]').text.strip() == "":
                        d['3PA_Per_100_Posessions'] = float(0)
                    else:
                        d['3PA_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=fg3a_per_poss]').text.strip())

                    if row.select_one('[data-stat=fg3_pct]').text.strip() == "":
                        d['3P_PCT'] = float(0)
                    else:
                        d['3P_PCT'] = float(row.select_one(
                            '[data-stat=fg3_pct]').text.strip())

                    if row.select_one('[data-stat=fg2_per_poss]').text.strip() == "":
                        d['2PM_Per_100_Posessions'] = float(0)
                    else:
                        d['2PM_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=fg2_per_poss]').text.strip())

                    if row.select_one('[data-stat=fg2a_per_poss]').text.strip() == "":
                        d['2PA_Per_100_Posessions'] = float(0)
                    else:
                        d['2PA_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=fg2a_per_poss]').text.strip())

                    if row.select_one('[data-stat=fg2_pct]').text.strip() == "":
                        d['2P_PCT'] = float(0)
                    else:
                        d['2P_PCT'] = float(row.select_one(
                            '[data-stat=fg2_pct]').text.strip())

                    if row.select_one('[data-stat=ft_per_poss]').text.strip() == "":
                        d['FTM_Per_100_Posessions'] = float(0)
                    else:
                        d['FTM_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=ft_per_poss]').text.strip())

                    if row.select_one('[data-stat=fta_per_poss]').text.strip() == "":
                        d['FTA_Per_100_Posessions'] = float(0)
                    else:
                        d['FTA_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=fta_per_poss]').text.strip())

                    if row.select_one('[data-stat=ft_pct]').text.strip() == "":
                        d['FT_PCT'] = float(0)
                    else:
                        d['FT_PCT'] = float(row.select_one(
                            '[data-stat=ft_pct]').text.strip())

                    if row.select_one('[data-stat=drb_per_poss]').text.strip() == "":
                        d['DRB_Per_100_Posessions'] = float(0)
                    else:
                        d['DRB_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=drb_per_poss]').text.strip())

                    if row.select_one('[data-stat=orb_per_poss]').text.strip() == "":
                        d['ORB_Per_100_Posessions'] = float(0)
                    else:
                        d['ORB_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=orb_per_poss]').text.strip())

                    if row.select_one('[data-stat=trb_per_poss]').text.strip() == "":
                        d['TRB_Per_100_Posessions'] = float(0)
                    else:
                        d['TRB_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=trb_per_poss]').text.strip())

                    if row.select_one('[data-stat=ast_per_poss]').text.strip() == "":
                        d['AST_Per_100_Posessions'] = float(0)
                    else:
                        d['AST_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=ast_per_poss]').text.strip())

                    if row.select_one('[data-stat=stl_per_poss]').text.strip() == "":
                        d['STL_Per_100_Posessions'] = float(0)
                    else:
                        d['STL_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=stl_per_poss]').text.strip())

                    if row.select_one('[data-stat=blk_per_poss]').text.strip() == "":
                        d['BLK_Per_100_Posessions'] = float(0)
                    else:
                        d['BLK_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=blk_per_poss]').text.strip())

                    if row.select_one('[data-stat=tov_per_poss]').text.strip() == "":
                        d['TOV_Per_100_Posessions'] = float(0)
                    else:
                        d['TOV_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=tov_per_poss]').text.strip())

                    if row.select_one('[data-stat=pf_per_poss]').text.strip() == "":
                        d['Fouls_Per_100_Posessions'] = float(0)
                    else:
                        d['Fouls_Per_100_Posessions'] = float(row.select_one(
                            '[data-stat=pf_per_poss]').text.strip())

                    if row.select_one('[data-stat=pts_per_poss]').text.strip() == "":
                        d['Points_Per_100_Posessions'] = float(0)
                    else:
                        d['Points_Per_100_Posessions'] = float(row.select_one(
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

            start_year += 1
            sleep(3)

        with open(f'{file_start}-{end_year}_per_100_possessions_{fileNameEnd}.json', 'w') as f:
            json.dump(data, f)
        return

    if reg_play == "Both":
        cntr = 0
        nameEnd = 'regular_season'
        while cntr < 2:
            actual_scrape(start_year, end_year, page_list[cntr], nameEnd)
            # since the second list will always be a list with playoffs, we can do this
            nameEnd = 'playoffs'
            cntr += 1
    elif reg_play == "Regular Season":
        actual_scrape(start_year, end_year, page_list, 'regular_season')
    elif reg_play == "Playoffs":
        actual_scrape(start_year, end_year, page_list, 'playoffs')
    return


def totals_scrape(reg_play, start_year, end_year):
    tp = "totals"
    page_list = list_creator(reg_play, start_year, end_year, tp)

    def actual_scrape(start_year, end_year, page_list, fileNameEnd):
        data = []
        file_start = start_year  # did this for the file name
        for page in page_list:
            r = requests.get(page)
            soup = BeautifulSoup(r.content, 'html.parser')
            rows = soup.select('tbody tr')

            for row in rows:
                d = dict()

                if row.select_one('[data-stat=g]').text.strip() != 'G':
                    d['Year'] = start_year
                    d['Name'] = row.select_one(
                        '[data-stat=player]').text.strip()
                    d['Position'] = row.select_one(
                        '[data-stat=pos]').text.strip()
                    d['Age'] = row.select_one('[data-stat=age]').text.strip()
                    d['Team'] = row.select_one(
                        '[data-stat=team_id]').text.strip()
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

            start_year += 1
            sleep(3)

        with open(f'{file_start}-{end_year}_totals_{fileNameEnd}.json', 'w') as f:
            json.dump(data, f)
        return

    if reg_play == "Both":
        cntr = 0
        nameEnd = 'regular_season'
        while cntr < 2:
            actual_scrape(start_year, end_year, page_list[cntr], nameEnd)
            # since the second list will always be a list with playoffs, we can do this
            nameEnd = 'playoffs'
            cntr += 1
    elif reg_play == "Regular Season":
        actual_scrape(start_year, end_year, page_list, 'regular_season')
    elif reg_play == "Playoffs":
        actual_scrape(start_year, end_year, page_list, 'playoffs')
    return


def list_creator(reg_play, user_start_year, user_end_year, type):
    if type == "adv":
        if reg_play == "Regular Season":
            advanced_pages = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_advanced.html'
                advanced_pages.append(total_input)
                counter += 1
            return advanced_pages
        elif reg_play == "Playoffs":
            advanced_pages_playoffs = []
            counter = user_start_year
            while counter <= user_end_year:
                play_off_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_advanced.html'
                advanced_pages_playoffs.append(play_off_pgs)
                counter += 1
            return advanced_pages_playoffs
        elif reg_play == "Both":
            advanced_pages = []
            advanced_pages_playoffs = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_advanced.html'
                advanced_pages.append(total_input)
                play_off_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_advanced.html'
                advanced_pages_playoffs.append(play_off_pgs)
                counter += 1
            return advanced_pages, advanced_pages_playoffs
    elif type == "per36":
        if reg_play == "Regular Season":
            per_36_pages = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_per_minute.html'
                per_36_pages.append(total_input)
                counter += 1
            return per_36_pages
        elif reg_play == "Playoffs":
            per_36_playoff = []
            counter = user_start_year
            while counter <= user_end_year:
                play_off_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_per_minute.html'
                per_36_playoff.append(play_off_pgs)
                counter += 1
            return per_36_playoff
        elif reg_play == "Both":
            per_36_pages = []
            per_36_playoff = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_per_minute.html'
                per_36_pages.append(total_input)
                play_off_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_per_minute.html'
                per_36_playoff.append(play_off_pgs)
                counter += 1
            return per_36_pages, per_36_playoff
    elif type == "per100":
        if reg_play == "Regular Season":
            per_100_poss = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_per_poss.html'
                per_100_poss.append(total_input)
                counter += 1
            return per_100_poss
        elif reg_play == "Playoffs":
            per_100_poss_playoff = []
            counter = user_start_year
            while counter <= user_end_year:
                play_off_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_per_poss.html'
                per_100_poss_playoff.append(play_off_pgs)
                counter += 1
            return per_100_poss_playoff
        elif reg_play == "Both":
            per_100_poss = []
            per_100_poss_playoff = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_per_poss.html'
                per_100_poss.append(total_input)
                play_off_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_per_poss.html'
                per_100_poss_playoff.append(play_off_pgs)
                counter += 1
            return per_100_poss, per_100_poss_playoff
    elif type == "totals":
        if reg_play == "Regular Season":
            totals_season = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_totals.html'
                totals_season.append(total_input)
                counter += 1
            return totals
        if reg_play == "Playoffs":
            totals_playoff = []
            counter = user_start_year
            while counter <= user_end_year:
                playoff_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_totals.html'
                totals_playoff.append(playoff_pgs)
                counter += 1
            return totals_playoff
        if reg_play == "Both":
            totals_season = []
            totals_playoff = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_totals.html'
                totals_season.append(total_input)
                playoff_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_totals.html'
                totals_playoff.append(playoff_pgs)
                counter += 1
            return totals, totals_playoff
    elif type == "perG":
        if reg_play == "Regular Season":
            per_game = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_per_game.html'
                per_game_poss.append(total_input)
                counter += 1
            return per_game
        elif reg_play == "Playoffs":
            per_game_playoff = []
            counter = user_start_year
            while counter <= user_end_year:
                play_off_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_per_game.html'
                per_game_playoff.append(play_off_pgs)
                counter += 1
            return per_game_playoff
        elif reg_play == "Both":
            per_game = []
            per_game_playoff = []
            counter = user_start_year
            while counter <= user_end_year:
                total_input = f'https://www.basketball-reference.com/leagues/NBA_{counter}_per_game.html'
                per_game.append(total_input)
                play_off_pgs = f'https://www.basketball-reference.com/playoffs/NBA_{counter}_per_game.html'
                per_game_playoff.append(play_off_pgs)
                counter += 1
            return per_game, per_game_playoff


def bbref_scrape():
    # This is to ask the nature of the data
    print("Please select if you'd like to have your data from the playoffs, regular season, or both:\n")
    rpb = choice.Menu(['Playoffs', 'Regular Season', 'Both']).ask()

    # This is to ask the specific data required
    print("Please select what data you'd like: \n")
    data = 'something else'  # just to start the loop
    wanted_data = []
    while data != 'No more':
        data = choice.Menu(['Totals', 'Advanced', 'Per 36',
                            'Per 100', 'Per Game', 'All', 'No more']).ask()
        if data != 'No more' and data != 'All' and data not in wanted_data:
            wanted_data.append(data)
        elif data != 'No more' and data != 'All' and data in wanted_data:
            print("Please try again. Do not select a source that you've already selected and please do not select 'All' if you've already selected a source. If you're done please select the 'No more' option.\n")
        elif data == 'All' and not wanted_data:
            wanted_data.append('Totals')
            wanted_data.append('Advanced')
            wanted_data.append('Per 36')
            wanted_data.append('Per 100')
            wanted_data.append('Per Game')
            data = 'No more'

    years = userYears()

    # This is to actually create whatever data that the user requested
    for wd in wanted_data:
        if wd == 'Advanced':
            advanced_scrape(rpb, years[0], years[1])
        elif wd == 'Totals':
            totals_scrape(rpb, years[0], years[1])
        elif wd == 'Per 36':
            per_36_scrape(rpb, years[0], years[1])
        elif wd == 'Per 100':
            per_100_scrape(rpb, years[0], years[1])
        elif wd == 'Per Game':
            per_game_scrape(rpb, years[0], years[1])

    return


bbref_scrape()
