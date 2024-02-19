import csv

def set_billing_criteria(raw_materials_cost, labor_cost, profit_share):
    """
    Set billing criteria for the purchase of raw materials.
    """
    with open('billing_criteria.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Raw Materials Cost', 'Labor Cost', 'Profit Share'])
        writer.writerow([raw_materials_cost, labor_cost, profit_share])

def view_billing_criteria():
    """
    View billing criteria set for the purchase of raw materials.
    """
    with open('billing_criteria.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Billing Criteria:")
            print(f"Raw Materials Cost: {row['Raw Materials Cost']}")
            print(f"Labor Cost: {row['Labor Cost']}")
            print(f"Profit Share: {row['Profit Share']}")

def main():
    while True:
        print("\nAdmin Module Menu:")
        print("1. Set Billing Criteria")
        print("2. View Billing Criteria")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            raw_materials_cost = float(input("Enter raw materials cost: "))
            labor_cost = float(input("Enter labor cost: "))
            profit_share = float(input("Enter profit share: "))
            set_billing_criteria(raw_materials_cost, labor_cost, profit_share)
            print("Billing criteria set successfully.")

        elif choice == '2':
            view_billing_criteria()

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
