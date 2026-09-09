from operator import itemgetter

# Pre-made sessions
allSessions = [
    {"topic": "Loops",
        "duration_minutes": 20,
        "status": "Completed"},
    {"topic": "Lists",
        "duration_minutes": 30,
        "status": "Completed"},
    {"topic": "Arrays",
        "duration_minutes": 50,
        "status": "Planned"},
    {"topic": "Tuples",
        "duration_minutes": 60,
        "status": "Planned"},
    {"topic": "Variables",
        "duration_minutes": 30,
        "status": "Completed"}
]

# Still need if else conditions if user has an invalid input etc
while True:
    # Menu
    print("1. Register a session")
    print("2. Show all study sessions")
    print("3. Only show completed study sessions")
    print("4. Search for a word in topic")
    print("5. Sort sessions by duration, longest first")
    print("6. Show total and average duration for completed sessions")
    print("7. Finish program")

    choice = input("What do you want to do? ")
    if (choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6"
    and choice != "7"):
        print("Invalid input")
        continue

    if choice == "1":
        print("Register a new session")
        newSession = {
            "topic": input("What is the session topic? ").capitalize(),
            "duration_minutes": int(input("How long is the session? ")),
            "status": input("Planned or completed? ").capitalize()
        }
        allSessions.append(newSession)
        print(newSession)

    elif choice == "2":
        for sessions in allSessions:
            print(sessions)

    elif choice == "3":
        for completed in [c for c in allSessions if c.get("status") == "Completed"]:
            print(completed)

    elif choice == "4":
        key = "topic"
        search = input("What topic do you want to look for? ").strip()
        matches = [session for session in allSessions if session[key] == search.lower()]
        if matches:
            print(f"Found {len(matches)} match(es): {matches}")
        else:
            print("No matching results.")

    elif choice == "5":
        print("Sorted by duration", sorted(allSessions, key=itemgetter("duration_minutes")))

    elif choice == "6":
        print("In progress")
        # Show first the total duration for completed sessions
        # Then show the average duration for completed sessions
    elif choice == "7":
        break