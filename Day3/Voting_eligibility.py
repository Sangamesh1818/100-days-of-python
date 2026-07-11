age = int(input("Enter your age: "))

print(f"Your age is {age}")

if(age>=18):
    print("You are an Adult & eligible to vote")
elif(age<18 and age>12):
    print(f"You are a Teenager & not eligible to vote")
else:
    print("You are a Child & not eligible to vote")

print("Thank you for using the Voting Eligibility Checker!")