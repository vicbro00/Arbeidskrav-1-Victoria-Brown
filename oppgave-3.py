import datetime as dt
from datetime import datetime, timedelta

# Ikke forventet en meny, bare funksjoner

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
            if minutes > 0 and minutes:
                minutes = timedelta(minutes=minutes)
            else:
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
    print("In progress")

def main():
    while True:
        first_date = new_date(input("What is the date? "))
        end_time = end_date(input("When did you start? "), int(input("How many minutes? ")))
        remaining = remaining_days(input("What is the first date? "), input("What is the second date? "))
        if first_date is not None and end_time is not None and remaining is not None:
            print(datetime.strftime(first_date, "%d.%m.%Y"))
            print(datetime.strftime(end_time, "%H.%M"))
            print(f"{remaining.days} days between.")
            break
        else:
            pass
if __name__ == "__main__":
    main()
