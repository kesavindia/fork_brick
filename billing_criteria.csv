import csv

def calculate_monthly_wage(daily_wage, working_days_per_month):
    return daily_wage * working_days_per_month

def set_wages(daily_wage, working_days_per_month):
    """
    Set daily and monthly wages for labor work.
    """
    monthly_wage = calculate_monthly_wage(daily_wage, working_days_per_month)
    with open('wages.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Daily Wage', 'Monthly Wage'])
        writer.writerow([daily_wage, monthly_wage])

def view_wages():
    """
    View daily and monthly wages set for labor work.
    """
    with open('wages.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Wages:")
            print(f"Daily Wage: {row['Daily Wage']}")
            print(f"Monthly Wage: {row['Monthly Wage']}")

def main():
    while True:
        print("\nAdmin Module Menu:")
        print("1. Set Wages")
        print("2. View Wages")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            daily_wage = float(input("Enter daily wage: "))
            working_days_per_month = int(input("Enter the number of working days in a month: "))
            set_wages(daily_wage, working_days_per_month)
            print("Wages set successfully.")

        elif choice == '2':
            view_wages()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
