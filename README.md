# NBA Data Analyzation
A short project that examines player statistics collected from basketball reference.

I learned how to scrape data from this source, check it out [here.](https://github.com/LearnDataSci/article-resources/blob/master/Ultimate%20Guide%20to%20Web%20Scraping/Part%201%20-%20Requests%20and%20BeautifulSoup/notebook.ipynb)

## Data Scraping Script
There is a python script that scrapes data and takes in a user-inputted range, ranging from 1980-2019.
**Prior to 1980, stat-tracking was spotty and some statistics were completely ignored altogether.** For example, steals and blocks were not recorded until the 1973-74 NBA season.  

The script makes sure that the user doesn't enter an incorrect year, and compiles the data from basketballreference from the following pages:
- Advanced Stats
- Per-36 Minute Stats
- Per-100 Possession Stats
- Season Totals

#### Notes about the Script
Files will be outputted in JSON format, with the naming schema STARTyear-ENDyear_stat.JSON.

Due to the nature of the actual source of the data, I encountered the problem of some of the fields in the HTML table (namely fields that involved ratios) outputting empty strings because of an empty field in the HTML itself.

In order to combat this, and to make sure that the entirety of a row was taken if it contained data, code in the scripts actually scraping the data looked like the following:
```python
if row.select_one('[data-stat=fg3_pct]').text.strip() == "":
          d['3P_PCT'] = float(0)
      else:
          d['3P_PCT'] = float(row.select_one(
              '[data-stat=fg3_pct]').text.strip())
```

This isn't necessarily the most efficient way to get around the problem but it was the simplest one I could think of at the time. For this reason, data collection may be more resource intensive than I initially desired.

This may or may not be optimized in the future, but as of writing this I opted to leave this alone as the script works fine. 
