from operator import itemgetter

# Pre-made sessions
all_sessions = [
    {"topic": "Loops",
        "duration_minutes": 20,
        "status": "Completed"},
    {"topic": "Lists",
        "duration_minutes": 30,
        "status": "Completed"},
    {"topic": "Arrays",
        "duration_minutes": 50,
        "status": "Completed"},
    {"topic": "Tuples",
        "duration_minutes": 60,
        "status": "Planned"},
    {"topic": "Variables",
        "duration_minutes": 30,
        "status": "Planned"}
]

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
        new_session = {}
        while True:
            topic = input("What is the topic? ").capitalize()
            if topic and topic.strip() and topic is not None:
                new_session["topic"] = topic
            else:
                print("Try again")
                continue
            break
        while True:
            try:
                duration = int(input("How long was the session in minutes? "))
                if duration <= 0:
                    print("Give a positive number and try again")
                    continue
            except ValueError:
                print("Not a valid number. Try again")
                continue
            new_session["duration_minutes"] = duration
            break
        while True:
            status = input("Planned or Completed? ").capitalize()
            if status != "Planned" and status != "Completed":
                print("Try again")
                continue
            else:
                new_session["status"] = status
            break
        all_sessions.append(new_session)
        print(all_sessions)

    elif choice == "2":
        for sessions in all_sessions:
            print(sessions)

    elif choice == "3":
        for completed in [session for session in all_sessions if session.get("status") == "Completed"]:
            print(completed)

    elif choice == "4":
        while True:
            key = "topic"
            search = input("What topic do you want to look for? ").strip()
            matches = [session for session in all_sessions if session[key] == search.capitalize()]
            if matches:
                print(f"Found {len(matches)} match(es): {matches}")
                break
            else:
                print("No matching results.")
            continue

    elif choice == "5":
        print("Sorted by duration", sorted(all_sessions, key=itemgetter("duration_minutes"), reverse=True))

    elif choice == "6":
        completed_sessions = [session for session in all_sessions if session["status"] == "Completed"]
        total = sum(session.get("duration_minutes", 0) for session in completed_sessions)
        if len(completed_sessions) <= 0:
            print("Cannot divide by 0")
        else:
            print(f"The total duration for all sessions is: {total}")
            average = sum(session.get("duration_minutes", 0) for session in completed_sessions) / len(completed_sessions)
            print(f"The average duration for all sessions is: {average:.2f}")
    elif choice == "7":
        break