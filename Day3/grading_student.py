marks = int(input("Enter your marks: "))

if marks >= 90:
    print(f"You have scored an A grade!")
elif marks >= 80 and marks < 90:
    print(f"You have scored a B grade!")
elif marks >= 70 and marks < 80:
    print(f"You have scored a C grade!")
else:
    print(f"You have scored a D grade!")