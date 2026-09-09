# Menu
print("1. Evaluate time spent studying")
print("2. Analyze text")
print("3. Analyze number intervals")
print("4. Close program")

while True:
    choice = input("What do you want to do? ")
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Invalid input")
        continue
    if choice == "1":
        # Oppgave 1.1
        user_input = False

        while not user_input:
            try:
                study_sessions = int(input("How many sessions did you have? "))
                minutes_per_session = int(input("How many minutes per session? "))

                if not study_sessions or not minutes_per_session:
                    print("Please give a positive whole number and try again!")
                    continue
                elif study_sessions < 0 or minutes_per_session < 0:
                    print("Please give a positive whole number and try again!")
                    continue
                else:
                    hours = study_sessions * minutes_per_session
                    hours_remaining = hours // 60
                    minutes_remaining = (hours / 60) % 1
                    total_minutes = minutes_remaining * 60
                    print(f"Total time spent is: {hours_remaining} hours and {total_minutes:.0f} minutes")
                user_input = True
                continue

            except ValueError:
                number = 0
                print("Invalid input! Try again!")

    elif choice == "2":
        # Oppgave 1.2
        text = input("What is on your mind? ")

        if text == " ":
            print("Give a valid text and try again!")
        elif text == "":
            print("Give a valid text and try again!")
        else:
            count = []
            word_count = 0
            for char in text:
                count.append(char)
                word_count += 1

            print(f"Number of values: {word_count}")
            print(text.lower())
            print(text[::-1].capitalize())

            if "python".lower() in text.lower():
                print(text.title())
    elif choice == "3":
        # Oppgave 1.3

        start = int(input("Give a starting value: "))
        end = int(input("Give an end value: "))
        total = 0

        if start > end:
            print("Start value is greater than end value. Try again!")
        else:
            for n in range(start, end + 1):
                if n % 2 == 0:
                    print(f"{n} is even")
                elif n % 3 == 0:
                    print(f"{n} is divisible by 3")
                total = n + n
            print(f"Sum of all numbers: {total}")
    elif choice == "4":
        break