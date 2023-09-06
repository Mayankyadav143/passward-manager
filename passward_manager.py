import random
import string

# Dictionary to store passwords
passwords = {}

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = generate_password()
    
    passwords[website] = {'username': username, 'password': password}
    print(f"Password for {website} saved successfully!")

def retrieve_password():
    website = input("Enter website: ")
    
    if website in passwords:
        username = passwords[website]['username']
        password = passwords[website]['password']
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print(f"No password found for {website}.")

while True:
    print("Options:")
    print("1. Save Password")
    print("2. Retrieve Password")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        save_password()
    elif choice == '2':
        retrieve_password()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")