#ცვლადში შეინახეთ თქვენი სახელი, შემდეგ კი მომხმარებელსაც შემოატანინეთ თავისი სახელი, თუ თქვენი სახელები დაემთხვევა გამოუტანეთ "Our names are similar !", სხვა შემთხვევაში - "We have different names". hint: დაგჭირდებათ პირობითი განცხადებები და სტრინგის მეთოდები. ეს შემოწმება უნდა იყოს case-insensitna
name = "andria"
user_name = input("Enter your name: ")
if name == user_name.lower():
    print("Our names are similar!")
else:
    print("None")  
