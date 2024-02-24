import re
import json
class UserOrder:
    def __init__(self):
        self.user_name = ""
        self.user_ph = ""
        self.user_address = ""
        self.remaining_amount = 0

    def validate_user_info(self):
        while True:
            self.user_name = input("Enter your name: ")
            self.user_ph = input("Enter your phone number: ")
            self.user_address = input("Enter your address: ")

            if all([self.user_name, self.user_ph, self.user_address]):
                if re.match(r'^[a-zA-Z]{3,12}$', self.user_name) and re.match(r'^\d{10}$', self.user_ph) and re.match(r'^[a-zA-Z]{3,30}$',self.user_address):
                    break
                else:
                    print("Invalid name or phone number or address format.")
            else:
                print("Please fill in all required fields.")
        print("Welcome to Brick manufacturing unit : ")

    def calculate_cost(self):
        n_bricks = int(input("Enter number of bricks you want: "))
        user_distance = float(input("Enter the distance to delivery location (in km): "))
        per_brick_price = 25
        per_km_cost = 25

        if user_distance <= 200:
            if n_bricks > 500:
                self.remaining_amount = (n_bricks * per_brick_price) + (per_km_cost * user_distance)
            else:
                print("Your lot n_bircks are less than 500 thats why we charge 15 extra per brick it is okk for you :yes or no")
                user_choice=input("Enter your choice : ").lower()
                if(user_choice=="yes"):
                    self.remaining_amount = ((n_bricks+15) * per_brick_price) + ((per_km_cost  * user_distance))
                else:
                    print("Thank you approching us ")
        else:
            print("Your location is too far for delivery.")
            user_choice = input("Do you accept  transportation charges you will take care? (yes/no): ").lower()
            if user_choice == "yes":
                self.remaining_amount = (n_bricks * per_brick_price)
            else:
                print("Thank you for considering us.")
                return

    def get_advance_payment(self):
        while True:
            advance_payment = float(input(f"Enter the advance payment (at least 20% of ${self.remaining_amount}): "))
            if advance_payment >= 0.2 * self.remaining_amount:
                if advance_payment > self.remaining_amount:
                    print(
                        "The advance payment is more than the total amount. Please pay up to 20% of the total amount or the total amount itself.")
                else:
                    break
            else:
                print("Advance payment should be at least 20% of the total amount.")

        remaining_amount = self.remaining_amount - advance_payment
        if remaining_amount < 0:
             print(f"Thank you for paying. Your change is ${-remaining_amount}.")
        else:
            print(f"Remaining amount to be paid: ${remaining_amount}")
            self.remaining_amount = remaining_amount
    def store_user_data(self):
        try:
            with open("userinformation.json", "a") as file:
                user_data = {
                    "name": self.user_name,
                    "phone_number": self.user_ph,
                    "address": self.user_address,
                    "remaining_amount": self.remaining_amount
                }
                json.dump(user_data, file)
                file.write(",\n")
                print("User data stored successfully.")
        except FileNotFoundError:
            print("Error occurred while storing user data.")

def main():
    user_order = UserOrder()
    user_order.validate_user_info()
    user_order.calculate_cost()
    if user_order.remaining_amount > 0:
         user_order.get_advance_payment()
         user_order.store_user_data()

if __name__ == "__main__":
    main()