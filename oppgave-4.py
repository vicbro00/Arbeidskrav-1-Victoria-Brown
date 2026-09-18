from pathlib import Path
import csv

# Oppgave 4.1 og oppgave 4.2
print(f"Current directory is: {Path.cwd()}")
data_directory = Path(".") / "supporthenvendelser.csv"
support_path = Path(".") / "supporthenvendelser.csv"
rapport_path = Path(".") / "support_rapport.txt"

print(f"Directory exists: {data_directory.exists()}")
print(support_path)
print(rapport_path)

valid = 0
category_count = {}
resolved_count = {}
unresolved_count = []
total = 0

# Checks if row is empty
with open("supporthenvendelser.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)
    next(data)
    for row_number, row in enumerate(data):
        # Starts the row from row 2
        row_number += 1
        if "" in row or len(row) != 4:
            print(f"Line {row_number} id: {row[0]} is missing a value")
            continue
        int_row = int(row[0])
        if int_row < 0:
            print(f"Line {row_number} id: {row[0]} is not a positive whole number")
            continue
        int_minutes = row[2]
        try:
            int_minutes = int(int_minutes)
        except ValueError:
            print(f"Line {row_number} id: {row[0]} does not include a number")
            continue
        # Checks if row has yes or no, if it does it adds 1 to all valid rows, and adds the total minutes
        if row[3] == "yes" or row[3] == "no":
            valid += 1
            if row[1] in category_count:
                category_count[row[1]] += 1
            else:
                category_count[row[1]] = 1
            total += int_minutes
            if row[3] in resolved_count:
                resolved_count[row[3]] += 1
            else:
                resolved_count[row[3]] = 1
            if row[3] == "no":
                unresolved_count.append(row)
        else:
            print(f"Line {row_number} id: {row[0]} is not 'yes' or 'no'")
        # Shows the entire row
        print(row)
        # Shows total minutes in minutes category
        print(f"Total minutes are: {total}")
        average = total / valid
        # Shows average minutes from valid rows
        print(f"Average minutes are: {average:.1f}")


    # Shows how many values are in each category
    for c, category in category_count.items():
        print(f"Category: {c}: {category}")
    # Shows how many valid rows there are
    print(f"Number of valid rows are: {valid}")

    # Shows how many resolved and unresolved issues there are
    for r, resolved in resolved_count.items():
        if r == "yes":
            print(f"Resolved issues are: {resolved}")
        else:
            print(f"Unresolved issues are: {resolved}")

    # Shows the category with the most issues
    highest_value = max(category_count, key=category_count.get)
    print(f"Category with the most issues is: {highest_value}")

    # Shows sorted unresolved issues
    sorted_unresolved_issues = sorted(unresolved_count, key=lambda row: row[2], reverse=True)
    print(sorted_unresolved_issues)

# Oppgave 4.3
# Generate a support-rapport.txt file
with open(rapport_path, "w", encoding="utf-8") as file:
    file.write("--- Minutes ---\n")
    file.write(f"Total minutes in issues: {total} minutes\n")
    file.write(f"Average minutes in issues: {average:.1f} minutes\n")
    file.write("\n")
    file.write("--- Categories ---\n")
    for c, category in category_count.items():
        file.write(f"Category: {c}: {category} values\n")
    file.write(f"Category with the most issues is: {highest_value}\n")
    file.write("\n")
    file.write("--- Validation ---\n")
    file.write(f"Number of valid rows are: {valid}\n")
    for r, resolved in resolved_count.items():
        if r == "yes":
            file.write(f"Resolved issues are: {resolved}\n")
        else:
            file.write(f"Unresolved issues are: {resolved}\n")
    file.write("\n")
    file.write("--- Sorted issues ---\n")
    for unresolved in sorted_unresolved_issues:
        file.write(f"{unresolved[0]}, {unresolved[1]}, {unresolved[2]}, {unresolved[3]}\n")

# Oppgave 4.4
def sum_resolved_minutes(requests: list[dict[str, str | int]]) -> int | None:
    try:
        total = 0
        for request in requests:
            if request["is_resolved"] == "yes":
                total += int(request["minutes"])
        return total
    except ValueError:
        print("Invalid")

print(sum_resolved_minutes([{"is_resolved": "yes", "minutes": 13}, {"is_resolved": "yes", "minutes": 15}, {"is_resolved": "yes", "minutes": 10}]))