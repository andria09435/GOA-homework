number = int(input("შეიტანეთ ნებისმიერი რიცხვი: "))

for i in range(0, number + 1):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
