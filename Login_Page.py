import re

current_user = None

def register():
    username = input("Enter username (should start with a capital letter): ")
    password = input("Enter password (at least 8 characters including alphabets and numbers): ")
    user_type = input("Enter user type (Administrator/Investor): ")

    if not (username.istitle() and re.match("^(?=.*[a-zA-Z])(?=.*[0-9]).{8,}$", password)):
        print("Invalid username or password. Please try again.")
        return

    if user_type not in ["Administrator", "Investor"]:
        print("Invalid user type. Please enter either Administrator or Investor.")
        return

    with open('registered_users.txt', 'a') as file:
        file.write(f"{username},{password},{user_type}\n")
    print("Registration successful!")


def login():
    global current_user
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open('registered_users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password, user_type = line.strip().split(',')
            if username == stored_username and password == stored_password:
                current_user = username
                print(f"Login successful! Welcome {username} ({user_type})")
                return
            print("Invalid username or password. Please try again.")


def logout():
    global current_user
    if current_user:
        print(f"Logout successful. Goodbye, {current_user}!")
        current_user = None
    else:
        print("No user is currently logged in.")


def main():
    while True:
        choice = input("Press 1 to register, 2 to login, 3 to logout, or 4 to exit : ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            logout()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


