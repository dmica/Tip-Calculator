#Welcome Message
print("Welcome to the tip calculator.")

#Get bill value
bill = float(input("What was the total bill? $"))

#Get tip value and convert to precentage
tip = int(input("What precentage tip would you like to give? 10, 12, or 15? "))

#Get number of people
num_people = int(input("How many people to split the bill? "))

#Total bill with tip
bill_with_tip = tip / 100 * bill + bill

#Total bill per person
bill_per_person = bill_with_tip / num_people

#Round to 2 decimal places
final_bill = "{:.2f}".format(bill_per_person)

# Output
print(f"Each person should pay {final_bill}")
