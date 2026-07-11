# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

print(f"Welcome to the BMI Checker!")

height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kg:"))

BMI = weight / (height ** 2 )

if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}. You have a normal weight.")
else:
    print(f"Your BMI is {BMI}. You are overweight.")