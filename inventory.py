import csv,json

class Brick:
    def __init__(self, type, dimensions, weight, color, strength_rating, quantity, cost_per_unit):
        self.type = type
        self.dimensions = dimensions
        self.weight = weight
        self.color = color
        self.strength_rating = strength_rating
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def calculate_total_weight(self):
        if self.quantity == 0:
            raise ValueError("Cannot calculate total weight with zero quantity.")
        return self.weight * self.quantity

    def calculate_total_cost(self):
        return self.cost_per_unit * self.quantity

class RawMaterial:
    def __init__(self, type, supplier, unit, quantity, cost_per_unit):
        self.type = type
        self.supplier = supplier
        self.unit = unit
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def calculate_total_cost(self):
        return self.cost_per_unit * self.quantity

class InventoryLocation:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity
        self.current_stock = []

    def add_stock(self, brick, quantity):
        if self.capacity - sum(b.quantity for b in self.current_stock) >= quantity:
            self.current_stock.append(brick)
            brick.quantity += quantity
        else:
            raise ValueError(f"Insufficient capacity at {self.location}")

    def remove_stock(self, brick, quantity):
        try:
            if quantity <= brick.quantity:
                brick.quantity -= quantity
                if brick.quantity == 0:
                    self.current_stock.remove(brick)
            else:
                raise ValueError(f"Insufficient stock of {brick.type} at {self.location}")
        except ValueError as e:
            print(f"Error removing stock: {e}")

def load_inventory(filename):
    """
    Loads inventory data from a JSON file.
    """
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            inventory_locations = {}
            for location_data in data["locations"]:
                location = InventoryLocation(location_data["location"], location_data["capacity"])
                for item_data in location_data["items"]:
                    if item_data["type"] == "brick":
                        brick = Brick(*item_data["details"])
                        location.add_stock(brick, item_data["quantity"])
                    else:
                        material = RawMaterial(*item_data["details"])
                        location.current_stock.append(material)
                inventory_locations[location.location] = location
            return inventory_locations
    except FileNotFoundError:
        print(f"Inventory file '{filename}' not found. Creating a new one.")
        return {}

def save_inventory(inventory, filename):
    """
    Saves inventory data to a JSON file.
    """
    data = {
        "locations": [
            {
                "location": location.location,
                "capacity": location.capacity,
                "items": [
                    {
                        "type": "brick" if isinstance(item, Brick) else "raw_material",
                        "details": item.__dict__,
                        "quantity": item.quantity,
                    }
                    for item in location.current_stock
                ],
            }
            for location in inventory.values()
        ]
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def main():
    filename = "inventory.json"
    inventory = load_inventory(filename)

    while True:
        print("\nInventory Management:")
        print("1. Add new brick")
        print("2. Add new raw material")
        print("3. View inventory by location")
        print("4. Check quantity of specific item")
        print("5. Add stock to location")
        print("6. Remove stock from location")
        print("7. Save inventory to file")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add new brick details and update inventory
            type = input("Enter brick type: ")
            dimensions = eval(input("Enter dimensions (as a tuple): "))
            weight = float(input("Enter weight: "))
            color = input("Enter color: ")
            strength_rating = int(input("Enter strength rating: "))
            quantity = int(input("Enter quantity: "))
            cost_per_unit = float(input("Enter cost per unit: "))
            
            brick = Brick(type, dimensions, weight, color, strength_rating, quantity, cost_per_unit)
            # You need to add the brick to the appropriate location in inventory
            # e.g., inventory["Warehouse"].add_stock(brick, quantity)
            print("Brick added successfully!")

        elif choice == "2":
            # Add new raw material details and update inventory
            type = input("Enter raw material type: ")
            supplier = input("Enter supplier: ")
            unit = input("Enter unit: ")
            quantity = int(input("Enter quantity: "))
            cost_per_unit = float(input("Enter cost per unit: "))
            
            material = RawMaterial(type, supplier, unit, quantity, cost_per_unit)
            # You need to add the material to the appropriate location in inventory
            # e.g., inventory["Warehouse"].current_stock.append(material)
            print("Raw material added successfully!")

        elif choice == "3":
            # Display inventory details for each location
            for location, inv_loc in inventory.items():
                print(f"\nLocation: {location}")
                for item in inv_loc.current_stock:
                    if isinstance(item, Brick):
                        print(f"Brick Type: {item.type}, Quantity: {item.quantity}")
                    else:
                        print(f"Raw Material Type: {item.type}, Quantity: {item.quantity}")

        elif choice == "4":
            # Ask user for item type and location
            item_type = input("Enter item type (brick/raw material): ")
            location = input("Enter location: ")
            # Check quantity and display
            # e.g., print(inventory[location].get_quantity(item_type))

        elif choice == "5":
            # Ask user for item type, location, and quantity
            item_type = input("Enter item type (brick/raw material): ")
            location = input("Enter location: ")
            quantity = int(input("Enter quantity to add: "))
            # Update inventory and save
            # e.g., inventory[location].add_stock(item, quantity)
            # save_inventory(inventory, filename)
            print("Stock added successfully!")

        elif choice == "6":
            # Ask user for item type, location, and quantity
            item_type = input("Enter item type (brick/raw material): ")
            location = input("Enter location: ")
            quantity = int(input("Enter quantity to remove: "))
            # Update inventory and save
            # e.g., inventory[location].remove_stock(item, quantity)
            # save_inventory(inventory, filename)
            print("Stock removed successfully!")


        elif choice == "7":
            save_inventory(inventory, filename)
            print("Inventory saved successfully!")

        elif choice == "8":
            save_inventory(inventory, filename)
            print("Exiting...")

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()