import re
import hashlib


#Heelo


class UserAuthentication:
    def __init__(self):
        self.users = {}
        self.roles = ['Administrator', 'Investor']
    def register_user(self, username, password, role):
        if username[0].isupper() and username.isalpha() and len(password) >= 8:
            if role in self.roles:
                if username not in self.users:
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    user_id = len(self.users) + 1
                    self.users[username] = {'id': user_id, 'role': role, 'password': hashed_password}
                    return f"User {username} registered successfully as a {role}."
                else:
                    return f"Username {username} is already taken. Please choose a different username."
            else:
                return "Invalid role. Choose from Administrator or Investor."
        else:
            return "Invalid username or password format."

    def validate_password(self, password, hashed_password):
        return hashed_password == hashlib.sha256(password.encode()).hexdigest()

    def login_user(self, username, password):
        if username in self.users:
            while not self.validate_password(password, self.users[username]['password']):
                password = input("Incorrect password. Please try again : ")
            return f"Welcome, {self.users[username]['role']} {username}!"
        else:
            return "User not found. Please register first."

# Example usage
auth = UserAuthentication()

while True:
    choice = input("Enter 'R' for registration or 'L' for login : ")
    if choice.lower() == 'r':
        username = input("Enter username for registration: ")
        password = input("Enter password for registration : ")
        role = input("Enter role (Administrator/Investor) : ")

        registration_result = auth.register_user(username, password, role)
        print(registration_result)
    elif choice.lower() == 'l':
        login_username = input("Enter username for login : ")
        login_password = input("Enter password for login : ")

        login_result = auth.login_user(login_username, login_password)
        print(login_result)
    else:
        print("Invalid choice. Please try again.")

