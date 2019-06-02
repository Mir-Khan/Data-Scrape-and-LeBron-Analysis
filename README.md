# NBA Data Analyzation
A short project that examines player statistics collected from basketball reference.

### Data Scraping Script
There is a python script that scrapes data and takes in a user-inputted range, ranging from 1980-2019.
**Prior to 1980, stat-tracking was spotty and some statistics were completely ignored altogether.** For example, steals and blocks were not recorded until the 1973-74 NBA season.  

The script makes sure that the user doesn't enter an incorrect year, and compiles the data from basketballreference from any of the following pages:
- Advanced Stats
- Per-36 Minute Stats
- Per-100 Possession Stats
- Per-Game Stats
- Season Totals

##### Notes about the Scraping Script
- Files will be outputted in JSON format, with the naming schema STARTyear-ENDyear_stat_playoff/regularSeason.JSON.

- Due to the nature of the actual source of the data, I encountered the problem of some of the fields in the HTML table (namely fields that involved ratios) outputting empty strings because of an empty field in the HTML itself.

  - In order to combat this, and to make sure that the entirety of a row was taken if it contained data, code in the scripts actually scraping the data looked like the following:
```python
if row.select_one('[data-stat=fg3_pct]').text.strip() == "":
          d['3P_PCT'] = float(0)
      else:
          d['3P_PCT'] = float(row.select_one(
              '[data-stat=fg3_pct]').text.strip())
```

  - This isn't necessarily the most efficient way to get around the problem but it was the simplest one I could think of at the time. For this reason, data collection may be more resource intensive than I initially desired.

  - This may or may not be optimized in the future, but as of writing this I opted to leave this alone as the script works fine.

- Increasing the range of the number of years you're scraping will significantly impact the amount of time you're waiting for the script to do its job.

- There are different functions for each type of page, but these can only be called by the main function, bbref_scrape. It's not suggested to actually use these functions individually. The intention was to just automate this for anyone who wants to get data easy.

- The actual script can just be called using the function bbref_scrape, and this can be called to follow a set of prompts that fill in important variables for the other functions.

#### Variable Notes
There are certain variables that are repeated throughout the script. Here are their descriptions:

- **reg_play** - This is the variable that tells the script whether or not the data its looking for is in the regular season or playoffs.

- **user_start_year/start_year** - This variable is what holds the user inputted start year. It's used to fill in the year field for each data entry, create a list of pages along with the end year, and to help create the file name. The name was shortened when called by the scraping functions in order to distinguish them.

- **user_end_year/end_year** - This variable is what holds the user inputted end year. It's used to help create a page list and to help create the file name. The name was shortened when called by the scraping functions in order to distinguish them.

- **type/tp** - This variable helps tell the page list creating function what type of page list to create and it's called by that function from the individual page scraping functions.

# LeBron Analysis
This analysis provides a general overview of some of LeBron's advanced statistics (mainly WS) compared to the rest of the league.

### Notes About the Data
There are some general notes about the data that should be mentioned.

- The observations only include the years that LeBron made the playoffs, which were 2006-2018. This is because of the fact that I wanted to be able to easily compare regular season stats and playoff stats better.

- The data containing the rest of the league was trimmed in order to be able to better observe the higher performers in the league. I did this through the **Win Share** metric. Why? This metric is probably the best one as it incorporates both defense and offense in its calculations.
  - Because of this the data was filtered out. This was done by only including the players that had more than 1 WS in the playoffs, as adding a win in the playoffs is something that a lot of teams would appreciate.
  - The regular season WS was filtered differently. The 2019 season saw the Sacramento Kings miss the playoffs in the Western Conference by 10 wins and the Hornets by 2 wins in the Eastern Conference. I opted to just use the average by these two and go for anyone who contributed by 6 or more wins in the regular season.

### Graphs and Takeaways
![WS Comparison of LeBron vs the mean of of the league in playoffs](https://github.com/Mir-Khan/NBA-Data-Analysis/blob/master/WS_PF_LBJvsLeagueAVG.png)

This graph shows us that compared to the rest of the league, LeBron is certainly above average in terms of WS. This doesn't tell us much besides LeBron James is a really good basketball player (duh). The one insightful thing we can see is 2012 is clearly an outlier, even by LeBron's standards. The two possible reasons for this:
- There was a lockout that caused the 2011-2012 season to be shortened to 62 games. The fewer games might mean more rest for LeBron and thus he can perform better come playoff time.
- LeBron had lost the 2011 finals in a disappointing fashion. He might've channeled this disappointment into one of his highest performing playoff performances in his career in regards to WS.

LeBron's True Shooting % compared to Usage Percentage:
![LeBron's TS% compared to USG% in both the regular season and playofss](https://github.com/Mir-Khan/NBA-Data-Analysis/blob/master/TSPct_LBJ.png)

This graph compares LeBron's 


WS Comparison to the best of the rest of the league:
![WS Comparison of LeBron vs the best of the rest of the league in both the regular season and playoffs](https://github.com/Mir-Khan/NBA-Data-Analysis/blob/master/LBJ%20WS%20Comparisons.png)

DWS Comparison to the best of the rest of the league:
![DWS Comparison of LeBron vs the best of the rest of the league](https://github.com/Mir-Khan/NBA-Data-Analysis/blob/master/LBJ%20DWS%20Comparisons.png)


## Other Libraries Used

The libraries that were used for the creation of the script include:

* [json](https://docs.python.org/3/library/json.html)
* [urllib3](https://pypi.org/project/urllib3/)
* [choice](https://pypi.org/project/choice/)
* [requests](https://pypi.org/project/requests/2.7.0/)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
* [time](https://docs.python.org/3/library/time.html)

The other libraries used for the analysis are as followed:
* [pandas](https://pandas.pydata.org/)
* [matplotlib](https://matplotlib.org/)

### Acknowledgements
I learned how to scrape data from LearnDataSci's tutorial here, check it out **[here.](https://github.com/LearnDataSci/article-resources/blob/master/Ultimate%20Guide%20to%20Web%20Scraping/Part%201%20-%20Requests%20and%20BeautifulSoup/notebook.ipynb)**
