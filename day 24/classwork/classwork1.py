password = "12345"

while True:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Correct password")
        break
    else:
        print("Incorrect password")