print(f"Welcome to the Rollercoaster Eligibility Checker!")
bill = 0

height = int(input("Enter your height in cm: "))
if height >= 120:
    print(f"You are eligible to ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if (age <= 12):
        bill = 5
        print(f"You need to pay $5.")
    elif (age >=12 and age <= 18):
        bill = 7
        print(f"You need to pay $7.")
    else:
        bill = 12
        print(f"You need to pay $12.")
    
    want_photo = input("Do you want a photo taken? Y or N: ")
    if want_photo == "Y" or want_photo == "y":
        bill += 3
    
    print(f"Your final bill is ${bill}.")
else:
    print(f"Sorry, you need to be at least 120 cm tall for eligibility.")