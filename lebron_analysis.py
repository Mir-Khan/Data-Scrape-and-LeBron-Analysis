import pandas as pd
import matplotlib.pyplot as plt

adv_reg = pd.read_json(
    r'C:\Users\Mir\Documents\GitHub\NBA__Project\2014-2019_json_files\2004-2019_advanced_stats_regular_season.json')

adv_play_off = pd.read_json(
    r'C:\Users\Mir\Documents\GitHub\NBA__Project\2014-2019_json_files\2004-2019_advanced_stats_playoffs.json')
# Just to observe all the columns we have
for col in adv_play_off.columns:
    print(col)

# A surface-level examination of the data, to make sure it was imported correctly
adv_play_off.head(10)

# We want to compare LeBron to all his contemporaries, so we took the total dataset and subsetted
adv_playoff_LBJ = pd.DataFrame(
    adv_play_off.loc[adv_play_off['Name'] == 'LeBron James'])
# Tells us we don't need 2004,05, or 2019 since LeBron didn't make playoffs these years
adv_playoff_LBJ['Year']

# Since LeBron has played every regular season he's been in, and we want to stay consistent, I took out the years he didn't make playoffs
adv_reg_LBJ = pd.DataFrame(
    adv_reg.loc[(adv_reg['Name'] == 'LeBron James') & (adv_reg['Year'] != 2004) & (adv_reg['Year'] != 2005) & (adv_reg['Year'] != 2019)])

# This is for everybody else essentially
adv_pf_notLBJ = pd.DataFrame(adv_play_off.loc[(adv_play_off['Name'] != 'LeBron James') &
                                              (adv_play_off['Year'] != 2004) & (adv_play_off['Year'] != 2005) & (adv_play_off['Year'] != 2019)])

adv_reg_notLBJ = pd.DataFrame(adv_reg.loc[(adv_reg['Name'] != 'LeBron James') &
                                          (adv_reg['Year'] != 2004) & (adv_reg['Year'] != 2005) & (adv_reg['Year'] != 2019)])

# Cleaning and adjusting the data for visualization

# I want to see year-by-year comparisons, so I grouped the data by year here
pf_notLBJ_year_obs = adv_pf_notLBJ.groupby('Year')
reg_notLBJ_year_obs = adv_reg_notLBJ.groupby('Year')
playoff_LBJ_year_obs = adv_playoff_LBJ.groupby('Year')
reg_LBJ_year_obs = adv_reg_LBJ.groupby('Year')

# Now I'm just looking at the basic form of the data, for LBJ it's as as simple as looking at the actual observations. For everyone else, you have

# max is 3.8 and 75% of the data is contained below 0.3/0.4 OWS for each year, everyone above this is an outlier
pf_notLBJ_year_obs['OWS'].describe()
# max is much higher (as there are more games in the regular season),never below 10 and 75% of the data never dips below 1.5
reg_notLBJ_year_obs['OWS'].describe()

# max is never lower than 1.3, and again 75% of the data is always around 0.3 or 0.2
pf_notLBJ_year_obs['DWS'].describe()
# Again much higher, no lower than 4.9 (the lockout season), and 75% is no lower than 1.3
reg_notLBJ_year_obs['DWS'].describe()

# max is never lower than 3.1, and 75% of the data is within 0.5 most of the time
pf_notLBJ_year_obs['WS'].describe()
# max is never lower than 12.7, and 75% of the data is within 2.9 or above
reg_notLBJ_year_obs['WS'].describe()

# We just have to adjust the data based on WS since its just OWS and DWS combined

adv_pf_notLBJ = adv_pf_notLBJ.loc[adv_pf_notLBJ['WS'] >= 1]
adv_reg_notLBJ = adv_reg_notLBJ.loc[adv_reg_notLBJ['WS'] >= 6]

# Grouping all the other players by year
adv_pf_notLBJ = adv_pf_notLBJ.groupby('Year')
adv_reg_notLBJ = adv_reg_notLBJ.groupby('Year')

# Plots

# LBJ WS vs Mean WS
axes = plt.gca()
adv_playoff_LBJ.plot(kind='line', x='Year', y='WS',
                     color='red', label='LeBron James', ax=axes)
adv_pf_notLBJ['WS'].mean().plot(kind='line', x='Year', y='WS',
                                color='blue', label='League Average WS', ax=axes)
plt.legend(loc='upper left')
plt.title('LeBron James Playoff WS vs Average WS of the League')
plt.ylabel('Playoff WS')
plt.annotate('2011-2012 Lockout Season', xy=(2012, 5.8), xytext=(2015.3, 5.7),
             ha='center', arrowprops=dict(arrowstyle='wedge', connectionstyle='arc3, rad=0'))
plt.savefig('WS_PF_LBJvsLeagueAVG.png', dpi=100)
plt.show()

# LBJ TS% Regular Season vs Playoffs with USG%

# Adjusting the TS% to make sure they're at the same scale as the USG%
adv_playoff_LBJ['TS_Percentage'] = adv_playoff_LBJ['TS_Percentage'] * 100
adv_reg_LBJ['TS_Percentage'] = adv_reg_LBJ['TS_Percentage'] * 100

# The actual plotting
axes = plt.gca()

adv_playoff_LBJ.plot(kind='line', x='Year', y='TS_Percentage',
                     color='red', label='Playoffs TS%', ax=axes)
adv_reg_LBJ.plot(kind='line', x='Year', y='TS_Percentage',
                 color='blue', label='Regular Season TS%', ax=axes)
adv_playoff_LBJ.plot(kind='line', x='Year', y='USG_Percentage',
                     color='red', label='Playoff USG%', ax=axes, linestyle='dashed')
adv_reg_LBJ.plot(kind='line', x='Year', y='USG_Percentage',
                 color='blue', label='Regular Season USG%', ax=axes, linestyle='dashed')


box = axes.get_position()
axes.set_position([box.x0, box.y0, box.width * 0.9, box.height])
plt.title("LeBron's TS% vs USG%")
plt.ylabel('Percentage')
plt.legend(bbox_to_anchor=(1.04, 1), loc='upper left')
plt.annotate('Irving and Love injured in the playoffs', xy=(2015, 37.6), xytext=(
    2014, 42), ha='center', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'))
plt.savefig('TSPct_LBJ.png', dpi=100, bbox_inches='tight')
plt.show()


# LBJ compared to the rest of the league's best WS
axes = plt.gca()

adv_pf_notLBJ['WS'].max().plot(kind='line', x='Year', y='WS',
                               color='red', label='Best of the Rest WS Playoffs', ax=axes, linestyle='dashed')
adv_reg_notLBJ['WS'].max().plot(kind='line', x='Year', y='WS',
                                color='blue', label='Best of the Rest WS Regular Season', ax=axes, linestyle='dashed')
adv_playoff_LBJ.plot(kind='line', x='Year', y='WS',
                     color='red', label='LBJ WS Playoffs', ax=axes)
adv_reg_LBJ.plot(kind='line', x='Year', y='WS', color='blue',
                 label='LBJ WS Regular Season', ax=axes,)

box = axes.get_position()
axes.set_position([box.x0, box.y0, box.width * 0.9, box.height])
plt.legend(bbox_to_anchor=(1.04, 1), loc='upper left')
plt.title('LeBron James WS v Best of the Rest')
plt.ylabel('Playoff WS')

# Annotations
# Injury
plt.annotate('LeBron suffers a back injury', xy=(2015, 10.3), xytext=(
    2015, 8), ha='center', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'), fontsize='small')

# Regular Season Player Names
plt.annotate('Dirk Nowitzki', xy=(2006, 17.7), xytext=(
    2007.3, 20.3), ha='center', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'), fontsize='small', fontweight='bold')
plt.annotate('Dirk Nowitzki', xy=(2007, 16.3), xytext=(
    2007.5, 12), ha='center', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'), fontsize='small', fontweight='bold')
plt.annotate('Chris Paul', xy=(2008, 17.8), xytext=(
    2007.5, 18.2), ha='center', fontsize='small', fontweight='bold')
plt.annotate('Kevin Durant', xy=(2014, 19.2), xytext=(
    2014.1, 20), ha='center', fontsize='small', fontweight='bold')
plt.annotate('James Harden', xy=(2015, 16.4), xytext=(
    2015.39, 15.7), ha='center', fontsize='small', fontweight='bold')
plt.annotate('Steph Curry', xy=(2016, 17.9), xytext=(
    2016, 18.1), ha='center', fontsize='small', fontweight='bold')
plt.annotate('James Harden', xy=(2017, 15), xytext=(
    2016.2, 14), ha='center', fontsize='small', fontweight='bold')
plt.annotate('James Harden', xy=(2018, 15.4), xytext=(
    2016.72, 11.2), ha='center', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'), fontsize='small', fontweight='bold')

# Playoff Player Names
plt.annotate('Dirk Nowitzki', xy=(2006, 5.4), xytext=(
    2007.4, 9), ha='center', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'), fontsize='small', fontweight='bold')
plt.annotate('Kevin Garnett', xy=(2008, 4.1), xytext=(
    2009, 1), ha='center', fontsize='small', fontweight='bold', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'))
plt.annotate('Pau Gasol', xy=(2010, 4.3), xytext=(
    2010, 6), ha='center', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'), fontsize='small', fontweight='bold')
plt.annotate('James Harden', xy=(2015, 3.9), xytext=(
    2015, 6), ha='center', fontsize='small', fontweight='bold', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'))

plt.savefig('LBJ WS Comparisons.png', dpi=100, bbox_inches='tight')
plt.show()

# These are for the annotations of the other player names, I wanted to show who exactly we're comparing to LeBron
adv_reg_notLBJ.apply(lambda x: x.loc[x['WS'].idxmax(), ['Name', 'WS']])

adv_pf_notLBJ.apply(lambda x: x.loc[x['WS'].idxmax(), ['Name', 'WS']])

# DWS Analysis
axes = plt.gca()

adv_playoff_LBJ.plot(kind='line', x='Year', y='DWS',
                     color='red', label='LBJ DWS Playoffs', ax=axes)
adv_pf_notLBJ['DWS'].max().plot(kind='line', x='Year', y='DWS',
                                color='blue', label='Best Leaguewide Playoff DWS')

plt.title("LeBron's Playoff DWS vs Leaguewide DWS")
plt.ylabel('Playoff DWS')
plt.legend(loc='upper right')

# annotations

plt.annotate('Kevin Garnett', xy=(2012, 1.6), xytext=(2012, 1.2), ha='center', fontsize='small',
             color='green', arrowprops=dict(arrowstyle='<|-', connectionstyle='arc3, rad=0'))
plt.annotate('Draymond Green', xy=(2016, 1.5), xytext=(2016, 1), ha='center', arrowprops=dict(
    arrowstyle='<|-', connectionstyle='arc3, rad=0'), fontsize='small', color='green')

plt.savefig('LBJ DWS Comparisons.png', dpi=100, bbox_inches='tight')
plt.show()


# Getting the names for the annotations again
adv_pf_notLBJ.apply(lambda x: x.loc[x['DWS'].idxmax(), ['Name', 'DWS']])
adv_playoff_LBJ[['Year', 'DWS']]
