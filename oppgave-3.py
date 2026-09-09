import datetime as dt

# Ikke forventet en meny, bare funksjoner

def new_date(date):
    value = input("Date? ")

    dt.datetime.strptime(value,
                     "%d.%m.%Y")
    print(date)
    return date

def end_date(start_time, minutes):
    end = start_time - minutes
    return end

def remaining_days(date1, date2):
    remaining = date2 - date1
    return remaining

def chronological_list():
    print("In progress")
