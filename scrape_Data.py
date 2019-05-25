from time import sleep
import requests
import urllib3
from bs4 import BeautifulSoup

# This is also me learning how to web-scrape properly
# Functions taken from https://github.com/LearnDataSci/article-resources/blob/master/Ultimate%20Guide%20to%20Web%20Scraping/Part%201%20-%20Requests%20and%20BeautifulSoup/notebook.ipynb

#############################Functions#########################################


def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


def open_html(path):
    with open(path, 'rb') as f:
        return f.read()


############################Initial Page Scrape#################################
url_advanced = r'https://www.basketball-reference.com/leagues/NBA_2010_advanced.html'
r = requests.get(url_advanced)
print(r.content[:100])  # this is to check if we actually have the url

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')

row = rows[0]
print(row)
name = row.select_one('tr > td').text.strip()
print(name)

team = row.select_one('[data-stat=team_id]').text.strip()
print(team)

gp = int(row.select_one('[data-stat=g]').text.strip())
print(f"Arron Afflalo played {gp} games during the 2009-10 NBA season")

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

for page in advanced_pages:
    r = requests.get(page)
    soup
