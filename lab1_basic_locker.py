SECRET_PASSWORD = "12345"

user_input = input("Enter password: ")

if user_input == SECRET_PASSWORD:
    print("Access granted")
else:
    print("Wrong password")
