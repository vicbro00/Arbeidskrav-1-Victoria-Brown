import datetime as dt
from datetime import datetime

# Ikke forventet en meny, bare funksjoner

def new_date(date):
    try:
        date = dt.datetime.strptime(date,
            "%d.%m.%Y")
        return date
    except ValueError:
        print("Invalid date format")
        return None

def end_date(start_time, minutes):
    print("In progress")

def remaining_days(date1, date2):
    if date2 > date1:
        remaining = date2 - date1
        return remaining.date
    else:
        remaining = date1 - date2
        return remaining.date

def chronological_list(list_of_dates):
    print("In progress")

def main():
    while True:
        first_date = new_date(input("What is the date? "))
        if first_date is not None:
            print(first_date)
            break
        else:
            pass
if __name__ == "__main__":
    main()
