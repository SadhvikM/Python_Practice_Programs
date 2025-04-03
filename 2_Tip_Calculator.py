print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("How much percentage tip would you like to give? 10, 12 or 15? "))
tip_amount = tip_percentage / 100 * total_bill
number_of_people = int(input("How many people to split the bill? "))
each_person_bill_amount = round((total_bill + tip_amount) / number_of_people, 2)
print(f"Each person should pay: ${each_person_bill_amount}")