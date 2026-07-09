print("Welcome to a Tip Calculator!")
bill= float(input("What was the total_bill?: $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))
split = int(input("How many people to split the bill?: "))

Tip_as_percent = tip /100
total_tip_amount = bill * Tip_as_percent
Total_bill = bill + total_tip_amount
bill_per_person = Total_bill / split
final_amount = round(bill_per_person, 2)
print(f"your total bill is: ${final_amount}")