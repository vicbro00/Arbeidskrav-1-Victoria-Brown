import datetime as dt
from datetime import datetime, timedelta

def new_date(date):
    try:
        date = dt.datetime.strptime(date,
            "%d.%m.%Y")
        return date
    except ValueError:
        print("Invalid date format. Please try again!")
        return None

def end_date(start_time, minutes):
    try:
        start_time = dt.datetime.strptime(start_time,
                                      "%H.%M")
        try:
            minutes = int(minutes)
            if minutes > 0 and minutes:
                minutes = timedelta(minutes=minutes)
            else:
                print("Not a positive minute number. Try again")
                return None
        except ValueError:
            print("Invalid input. Try again")
            return None

        end = start_time + minutes
        return end

    except ValueError:
        print("Invalid time format. Please try again!")
        return None

def remaining_days(date1, date2):
    try:
        date1 = dt.datetime.strptime(date1,
                                    "%d.%m.%Y")
        date2 = dt.datetime.strptime(date2,
                                    "%d.%m.%Y")
        if date2 > date1:
            remaining = date2 - date1
            return remaining
        else:
            remaining = date1 - date2
            return remaining
    except ValueError:
        print("Invalid input. Try again")

def chronological_list(list_of_dates):
    dates = []
    lists = list_of_dates.split(", ")

    for date in lists:
        try:
            list_date = dt.datetime.strptime(date,
                                        "%d.%m.%Y")
            dates.append(list_date)
        except ValueError:
            print("Invalid input. Try again")
            return None

    return sorted(dates)

def main():
    while True:
        first_date = new_date(input("What is the date? "))
        if first_date is not None:
            print(datetime.strftime(first_date, "%d.%m.%Y"))
            break
    while True:
        end_time = end_date(input("When did you start? "), input("How many minutes? "))
        if end_time is not None and end_time:
            print(datetime.strftime(end_time, "%H.%M"))
            break
    while True:
        remaining = remaining_days(input("What is the first date? "), input("What is the second date? "))
        if remaining is not None:
            print(f"{remaining.days} days between.")
            break
    while True:
        dates = chronological_list(input("Give a list of dates (separated by commas) "))
        if dates is not None:
            for date in dates:
                final_date = datetime.strftime(date, "%d.%m.%Y")
                print(final_date)
            break

if __name__ == "__main__":
    main()
