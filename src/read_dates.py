import pandas as pd

def read_months():
    dates = pd.read_csv("new_dates.csv")
    dates = dates.date.to_list()
    return dates

def read_years():
    years = pd.read_csv("years.csv")
    years = years.year.to_list()
    years = [format(x,'d') for x in years] #convert entries to strings
    return years





