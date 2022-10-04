from datetime import timedelta
from datetime import datetime


def date_range(start_date, end_date):
    # empty list for task
    list_of_dates = []
    # set our dates in datetime format
    try:
        # start date in datetime format
        start = datetime.strptime(start_date, "%Y-%m-%d")
        # end date in datetime format
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except:
        # pass if format is unreadable
        print(list_of_dates)
    else:
        # do if start date is earlier than end date
        while start <= end:
            # add to empty list the dates between two our input dates
            list_of_dates.append(datetime.strftime(start, "%Y-%m-%d"))
            # increment our date for 1 day
            start += timedelta(days=1)
        print(list_of_dates)


# call the function
date_range('2022-01-01', '2022-01-03')
