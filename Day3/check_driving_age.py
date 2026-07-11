print(f"Welcome to the Driving Age Checker!")
age = int(input("Enter your age: "))

if (age >= 18):
    if (age >=80):
        print (f"You are not eligible to drive due to age restrictions.")
    else:
        print(f"You are eligible to drive!")
else:
    print(f"Sorry, you need to be at least 18 years old to drive.")