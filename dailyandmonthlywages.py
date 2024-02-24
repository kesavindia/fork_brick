import csv

def calculate_monthly_wage(daily_wage, working_days_per_month):
    return daily_wage * working_days_per_month

def set_wages(name, daily_wage, working_days_per_month):
    """
    Set daily and monthly wages for labor work.
    """
    monthly_wage = calculate_monthly_wage(daily_wage, working_days_per_month)
    with open('wages.csv', 'a', newline='') as file:  # Use 'a' mode to append to the existing file
        writer = csv.writer(file)
        writer.writerow(['Name', 'Daily Wage', 'Monthly Wage'])
        writer.writerow([name, daily_wage, monthly_wage])

def edit_wages(name, daily_wage, working_days_per_month):
    """
    Edit daily and monthly wages for a specific person.
    """
    rows = []
    with open('wages.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'] == name:
                row['Daily Wage'] = daily_wage
                row['Monthly Wage'] = calculate_monthly_wage(daily_wage, working_days_per_month)
            rows.append(row)

    with open('wages.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Daily Wage', 'Monthly Wage'])
        writer.writeheader()
        writer.writerows(rows)

def view_wages(name):
    """
    View daily and monthly wages set for a specific person.
    """
    with open('wages.csv', 'r') as file:
        reader = csv.DictReader(file)
        found = False
        for row in reader:
            if row['Name'] == name:
                found = True
                print("Wages:")
                print(f"Name: {row['Name']}")
                print(f"Daily Wage: {row['Daily Wage']}")
                print(f"Monthly Wage: {row['Monthly Wage']}")
                break
        if not found:
            print(f"No wages found for {name}.")

def main():
    while True:
        print("\nAdmin Module Menu:")
        print("1. Add Wages")
        print("2. Edit Wages")
        print("3. View Wages")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            daily_wage = float(input("Enter daily wage: "))
            working_days_per_month = int(input("Enter the number of working days in a month: "))
            set_wages(name, daily_wage, working_days_per_month)
            print("Wages added successfully.")

        elif choice == '2':
            name = input("Enter name to edit wages: ")
            daily_wage = float(input("Enter new daily wage: "))
            working_days_per_month = int(input("Enter the number of working days in a month: "))
            edit_wages(name, daily_wage, working_days_per_month)
            print("Wages edited successfully.")

        elif choice == '3':
            name = input("Enter name to view wages: ")
            view_wages(name)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
