"""
Day 2 - Tip Calculator

Calculates the per-person cost of a restaurant bill after applying
a user-selected tip percentage.

"""

#collect user inputs and convert them to numeric values 
bill_text = input("How much was your bill?\n")
bill = float(bill_text)

tip = input("Would you like to tip 10, 12, or 15%?\n")
tip_num = float(tip)

partysize = input("How many people dined with you?\n")
party_num = int(partysize)


#calculate the per person bill
bill_per = (bill * (1+ (tip_num / 100))) / party_num
rounded_bill = round(bill_per,2)

#output result
print(f"Each person should pay ${rounded_bill}")
