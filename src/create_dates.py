from read_dates import read_years
import calendar
import datetime

today = datetime.date.today()
today_yr = today.year
today_mnth = today.month

def dates():
        years = read_years()
        weekday = 2 #Wednesday
        yr_mnths = []

        for year in years:
                result = [str(0) + str(month) + "-" 
                + str(max(week[weekday] for week in calendar.monthcalendar(year, month))) + "-" 
                + str(year) for month in range(1, 10)]

                result_2 = [str(month) + "-" 
                + str(max(week[weekday] for week in calendar.monthcalendar(year, month))) + "-" 
                + str(year) for month in range(10, 13)]

                results = result + result_2

                if year == 2021:
                        results = results[4:]
                        yr_mnths += results
                elif year == today_yr:
                        # results = results[:today_mnth]
                        results = results[:1] #January
                        yr_mnths += results
                else:
                        yr_mnths += results

        return yr_mnths


new_dates = dates()
print("Date start is: ", new_dates[0], "and date end is: ", new_dates[-1])


def comparison_dictkeys():
        months = ["Jan", "Feb", "Mar", "Apr", "May",
        "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

        my_dict = {}
        for date in new_dates:
                date_month = int(date[:2])
                date_yr = str(date[-2:])
                key = months[date_month-1]
                key = key + date_yr
                my_dict[key] = date
        return my_dict

comp_dict = comparison_dictkeys()