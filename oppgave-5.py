import datetime as dt

# Class of activities
class Activity:
    def __init__(self, title, category, date, estimated_minutes, status):
        self.title = title
        self.category = category
        self.date = date
        self.estimated_minutes = estimated_minutes
        self.status = status

    # Marks activity as completed
    def completed(self):
        self.status = "Completed"

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
    estimated_minutes = int(input("Duration of activity: "))
    status = input("Activity planned or completed? ").capitalize()

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
        print(f"Duration: {activity.estimated_minutes}")
        print(f"Status: {activity.status}\n")

def search_title_or_category():
    print("In progress")

def filter_by_status():
    print("In progress")

def sort_date_duration():
    print("In progress")

def mark_completed():
    print("In progress")

def show_total_activities():
    print("In progress")

def save_activities():
    print("In progress")

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
        show_total_activities()

    elif choice == "7":
        save_activities()

    elif choice == "8":
        break