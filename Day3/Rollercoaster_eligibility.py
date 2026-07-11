print(f"Welcome to the Rollercoaster Eligibility Checker!")

height = int(input("Enter your height in cm: "))
if height >= 120:
    print(f"You are eligible to ride the rollercoaster!")
else:
    print(f"Sorry, you need to be at least 120 cm tall for eligibility.")