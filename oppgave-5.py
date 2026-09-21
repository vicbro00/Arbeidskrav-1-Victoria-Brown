import datetime as dt
from operator import attrgetter

from pathlib import Path
from time import strptime

print(f"Current directory is: {Path.cwd()}")
activities_path = Path(".") / "activities.txt"

# Class of activities
class Activity:
    def __init__(self, title, category, date, estimated_minutes, status):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    # Prints the correct output, instead of something unreadable
    def __repr__(self):
        return f"Activity: {self.title!r}, {self.category}, {self.date}, {self.estimated_minutes}, {self.status}"

    # Marks activity as completed
    def completed(self):
        self.status = "completed"

def register_and_show_activity():
    title = input("Title of activity: ").capitalize()
    category = input("Category of activity: ").capitalize()
    while True:
        date = input("Date of activity (dd.mm.year): ")
        try:
            date = dt.datetime.strptime(date, "%d.%m.%Y")
            break
        except ValueError:
            print("Invalid date format. Please try again!")
    while True:
        try:
            estimated_minutes = int(input("Duration of activity: "))

            if estimated_minutes <= 0:
                print("Minutes is not a positive number")
                continue
            break
        except ValueError:
            print("Minutes is not a number")
    status = input("Activity planned or completed? ").lower()

    activity = Activity(
        title,
        category,
        date,
        estimated_minutes,
        status
    )

    activities.append(activity)
    for activity in activities:
        print(f"\nTitle: {activity.title}")
        print(f"Category: {activity.category}")
        print(f"Date: {activity.date.strftime('%d.%m.%Y')}")
        print(f"Duration: {activity.estimated_minutes} minutes")
        print(f"Status: {activity.status}\n")

def search_title_or_category():
    print("Choose 1 to search for title: ")
    print("Choose 2 to search for category: ")

    # Lets the user search by title or category
    while True:
        search_choice = input("What do you want to do? ")
        if search_choice == "1":
            try:
                title_search = input("Search for a title: ").capitalize()
                for activity in activities:
                    if title_search == activity.title:
                        print(activity)
                break
            except TypeError:
                print("Invalid input")
        elif search_choice == "2":
            try:
                category_search = input("Search for a category: ").capitalize()
                for activity in activities:
                    if category_search == activity.category:
                        print(activity)
                break
            except TypeError:
                print("Invalid input")

def filter_by_status():
    # Lets the user filter all activities based on planned or completed
    while True:
        filter_choice = input("Filter by planned or completed? ").capitalize()
        if filter_choice == "Planned":
            try:
                for activity in activities:
                    if activity.status == "planned":
                        print(activity)
            except TypeError:
                print("Invalid input")
        elif filter_choice == "Completed":
            try:
                for activity in activities:
                    if activity.status == "Completed":
                        print(activity)
            except TypeError:
                print("Invalid input")

def sort_date_duration():
    # If user chooses 1 here: sort by date
    # If user chooses 2 here: sort by duration
    print("Choose 1 to sort by date")
    print("Choose 2 to sort by duration")

    while True:
        sort_choice = input("What do you want to do? ")
        if sort_choice == "1":
            print("Sorted by date", sorted(activities, key=attrgetter("date")))
            break
        elif sort_choice == "2":
            print("Sorted by duration", sorted(activities, key=attrgetter("estimated_minutes")))
            break

def mark_completed():
    print("Choose activity to mark as completed")
    for idx, x in enumerate(activities, start=1):
        print(idx, x)

    while True:
        activity_choice = int(input("Type activity number to complete: "))
        selected_activity = activities[activity_choice - 1]
        if selected_activity.status == "completed":
            print("Activity already completed")
            continue
        else:
            Activity.completed(selected_activity)
        break

def show_number_activities():
    # Shows total number of activities
    total = 0
    for x in enumerate(activities, start=1):
        total += 1
    print(f"Total activities: {total}")

    # Shows total estimated minutes of all activities
    total_minutes = 0
    for activity in activities:
        total_minutes += activity.estimated_minutes
    print(f"Total minutes: {total_minutes}")

    # Shows total number of completed activities
    total_completed = 0
    for activity in activities:
         if activity.status == "completed":
             total_completed += 1
    print(f"Total completed activities: {total_completed}")

def save_activities():
    with open(activities_path, "w", encoding="utf-8") as file:
        for activity in activities:
            file.write(f"Title: {activity.title}\n")
            file.write(f"Category: {activity.category}\n")
            file.write(f"Date: {activity.date}\n")
            file.write(f"Duration: {activity.estimated_minutes}\n")
            file.write(f"Status: {activity.status}\n")
    print("Activities saved")

    with open(activities_path, "r", encoding="utf-8") as file:
        for line in file:
            activity = line.strip("\n").split(": ")
            if line.startswith("Title"):
                title = activity[1]
            elif line.startswith("Category"):
                category = activity[1]
            elif line.startswith("Date"):
                date = strptime(activity[1])
            elif line.startswith("Duration"):
                duration = int(activity[1])
            elif line.startswith("Status"):
                status = activity[1]
                new_activity = Activity(title, category, date, duration, status)
                activities.append(new_activity)
    print("Activities reread")

# Empty activity list
activities = []

# Menu
while True:
    print("1. Register and show activities")
    print("2. Search for title or category")
    print("3. Filter by status")
    print("4. Sort by date or duration")
    print("5. Mark activity as completed")
    print("6. Show number of activities, total estimated time and number of completed activities")
    print("7. Save activities to file and read them again")
    print("8. Quit program")

    choice = input("What do you want to do? ")
    if (choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6"
    and choice != "7"):
        print("Invalid input")
        continue

    if choice == "1":
        register_and_show_activity()

    elif choice == "2":
        search_title_or_category()

    elif choice == "3":
        filter_by_status()

    elif choice == "4":
        sort_date_duration()

    elif choice == "5":
        mark_completed()

    elif choice == "6":
        show_number_activities()

    elif choice == "7":
        save_activities()

    elif choice == "8":
        break