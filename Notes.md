# Exploring COVID-19 Vaccine Effectiveness

## Major changes applied to the project
This analysis now aims to explore the relationship between Covid-19 vaccinations and deaths attributed to Covid-19 in the U.S. between 5/01/21 - 01/31/23. 

Adding data up to 2023 in the analysis will allow for observation of the trend up to this day when things are now cooled down.

Data in this repo was accessed on Wednesday, February 15 2023. 


## Data
Because of the wweekly updates, we focused on data for for the last wednesday of every month, because the database is updated every Thursday for data from the previous week's Wednesday up to the present week's Wednesday.


## Date Handling
Instead of manually typing the dates for the last wednesday of every month from May 2021 to January 2023 into the repo, a `years.csv` has been created that allows a user to easily add a new year for analysis to the data. 

The years are read in through `read_dates.py`, and the dates to be used are automatically created in `create_dates.py`. To capture additional months in the current year (if added to years), there will be a need to edit the `if statement` of the `dates` function in `create_dates.py`.


## Visualization
All dates were adjusted from May 2021 to January 2023 to reflect the new update frequency. As at Wednesday, February 15 2023, the CDC also visualizes the data in same manner adjusting to using the last Wednesdays from 2021.

All `.py` files were edited to reflect the new date changes, including the visualization files `scatters.py`, `animation.py` and `comparison.py`.

#
## REFERENCES
* https://ds5010.github.io/vaccines/
* https://github.com/ds5010/spring-2023/blob/main/vaccines-3-setup.md
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
* https://pypi.org/project/git-filter-repo/
* https://github.com/newren/git-filter-repo
https://docs.python.org/3/library/calendar.html
* https://github.com/ds5010/spring-2023/blob/main/04-Vaccines.md
