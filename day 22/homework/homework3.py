status = input("Are you a student? (yes/no): ")
age = int(input("Enter your age: "))

if status.lower() == "yes":
    if age < 18:
        print("You are a minor student")
    else:
        print("You are an adult student")
else:
    print("You are not a student")