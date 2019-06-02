# NBA Data Analyzation
A short project that examines player statistics collected from basketball reference.

I learned how to scrape data from this source, check it out [here.](https://github.com/LearnDataSci/article-resources/blob/master/Ultimate%20Guide%20to%20Web%20Scraping/Part%201%20-%20Requests%20and%20BeautifulSoup/notebook.ipynb)

## Data Scraping Script
There is a python script that scrapes data and takes in a user-inputted range, ranging from 1980-2019.
**Prior to 1980, stat-tracking was spotty and some statistics were completely ignored altogether.** For example, steals and blocks were not recorded until the 1973-74 NBA season.  

The script makes sure that the user doesn't enter an incorrect year, and compiles the data from basketballreference from any of the following pages:
- Advanced Stats
- Per-36 Minute Stats
- Per-100 Possession Stats
- Per-Game Stats
- Season Totals

### Other Libraries Used

The libraries that were used for the creation of the script include:

* json
* urllib3
* choice
* requests
* BeautifulSoup
* time

#### Notes about the Scraping Script
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

### Variable Notes
There are certain variables that are repeated throughout the script. Here are their descriptions:

- **reg_play** - This is the variable that tells the script whether or not the data its looking for is in the regular season or playoffs.

- **user_start_year/start_year** - This variable is what holds the user inputted start year. It's used to fill in the year field for each data entry, create a list of pages along with the end year, and to help create the file name. The name was shortened when called by the scraping functions in order to distinguish them.

- **user_end_year/end_year** - This variable is what holds the user inputted end year. It's used to help create a page list and to help create the file name. The name was shortened when called by the scraping functions in order to distinguish them.

- **type/tp** - This variable helps tell the page list creating function what type of page list to create and it's called by that function from the individual page scraping functions.
