import json
import re
print("minimum_load_fee = 500")  # Rs
print("minimum_brick_price = 25")

minimum_brick_fee = 25  # Rs
minimum_load_fee = 500
def calculate_brick_cost(distance, num_bricks):
    if(num_bricks>=minimum_load_fee):
        per_km_distance=15
        total_cost=distance*per_km_distance+num_bricks*25
        return total_cost
    else:
        return "Please enter the minimum load"

def main():
    print("Welcome to the Brick Delivery System!")

    while True:
        user_name = input("Enter your name : ")
        if user_name.lower() == 'q':
            break

        phone_number = input("Enter your phone number: ")
        user_address = input("Enter your address: ")


        if any(field == "" for field in [user_name, phone_number, user_address]):
            print("Please fill in all required fields.")
            continue

        distance = float(input("Enter the distance for brick delivery (in km): "))


        while True:
            try:
                num_bricks = float(input("Enter the number of bricks you want (minimum 500): "))
                if num_bricks <minimum_load_fee:
                    print(f"Please enter at least {minimum_load_fee} bricks.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number of bricks.")


        total_cost = calculate_brick_cost(distance, num_bricks)

        print("Your total brick order amount is:", total_cost, "Rs.")

        try:
            with open("brick_orders.json", "w") as file:
                order_data = {
                    "name": user_name,
                    "address": user_address,
                    "phone_number": phone_number,
                    "distance": distance,
                    "num_bricks": num_bricks,
                    "total_cost": total_cost
                }
                json.dump(order_data, file)
                print("Order placed Successfully.")
        except FileNotFoundError:
            print("Error: Could not save order data to file.")
    else:
        print("Quilt")

if __name__ == "__main__":
    main()