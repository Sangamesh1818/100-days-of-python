print(f"Welcome to pizza deliveries!")
size = input(f"What size pizza do you want? S, M, or L (s,m, or l): ")
bill = 0

if (size == "S" or size == "s"):
    bill = 15
    print(f"You have selected a small pizza. Your bill is ${bill}.")
elif (size == "M" or size == "m"):
    bill = 20
    print(f"You have selected a medium pizza. Your bill is ${bill}.")
elif (size == "L" or size == "l"):
    bill = 25
    print(f"You have selected a large pizza. Your bill is ${bill}.")
else:
    print(f"You have selected an invalid size. Please select S, M, or L (s, m, or l).")

if (size in ["S", "s", "M", "m", "L", "l"]):
    pepperoni = input(f"Do you want pepperoni? Y or N (y or n): ")
    if (pepperoni == "Y" or pepperoni == "y"):
        if (size == "S" or size == "s"):
            bill += 2
        else:
            bill += 3
        print(f"You have selected pepperoni. Your bill is ${bill}.")

    extra_cheese = input(f"Do you want extra cheese? Y or N (y or n): ")
    if (extra_cheese == "Y" or extra_cheese == "y"):
        bill += 1
        print(f"You have selected extra cheese. Your bill is ${bill}.")

    print(f"\nYour final bill is ${bill}.")