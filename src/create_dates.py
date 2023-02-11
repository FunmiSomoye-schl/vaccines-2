from read_dates import read_months, read_years

def dates():
    months = read_months()
    years = read_years()
    yr_months = []

    for year in years:
        if year == "2021":
            for month in months[4:]:
                new_date = month + "-" + year
                yr_months.append(new_date)
        else:
            for month in months:
                new_date = month + "-" + year
                yr_months.append(new_date)

    return yr_months

new_dates = dates()