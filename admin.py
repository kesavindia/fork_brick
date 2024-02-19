import json
from tabulate import tabulate


class AdminModule:
    def __init__(self, filename="admin_data.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):

        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.distribution_percentages = data.get('distribution_percentages', {})
                self.transportation_rate_per_km = data.get('transportation_rate_per_km', 0)

            print("Welcome to admin page")
        except FileNotFoundError:
            print("File not found. Initializing with default values.")

    def save_data(self):
        data = {
            'distribution_percentages': self.distribution_percentages,

        }
        if hasattr(self, 'transportation_rate_per_km'):  # Check if the attribute is present
            data['transportation_rate_per_km'] = self.transportation_rate_per_km
        with open(self.filename, 'w') as file:
            json.dump(data, file)
        print("Data saved successfully!")

    def set_distribution_percentages(self, investor_percentage):
        total_percentage = investor_percentage
        if total_percentage >= 100:
            print("Error: Total percentage should equal to 100.")
            return

        self.distribution_percentages = {'investor': investor_percentage}
        self.save_data()

    def set_transportation_rate_per_km(self, rate_per_km):
        self.transportation_rate_per_km = rate_per_km
        self.save_data()

    def display_data(self):
        data = []
        for key, value in self.distribution_percentages.items():
            data.append([key, f"{value}%"])

        if hasattr(self, 'transportation_rate_per_km'):
            data.append(["Transportation Rate per Kilometer", self.transportation_rate_per_km])

        print(tabulate(data, headers=["Attribute", "Value"], tablefmt="grid"))
def display_menu():
    print("1. Set distribution percentages")
    print("2. Set customer transportation rate per kilometer")
    print("3. Display data")
    print("4. Exit")
    return input("Enter your choice: ")


# Example usage:
admin_module = AdminModule()
while True:
    choice = display_menu()
    if choice == '1':
        investor_percentage = float(input("Enter investor percentage: "))
        admin_module.set_distribution_percentages(investor_percentage)
    elif choice == '2':
        rate_per_km = float(input("Enter customer transportation rate per kilometer: "))
        admin_module.set_transportation_rate_per_km(rate_per_km)
    elif choice == '3':
        admin_module.display_data()
    elif choice == '4':
        print("Thank You...")
        admin_module.save_data()  # Save data before exiting
        break
    else:
        print("Invalid choice. Please enter a valid option.")
