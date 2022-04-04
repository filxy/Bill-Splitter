# Taking input from user
SubTotal = float(input("Please Type in your subtotal:"))
# Input tip percentage
Tip = int(input("Please Type in your percentage tip:"))
# Input no. of people splittling bill
people = float(input("Please Type in the number of people bill is being split between:"))
# Tax rate assigned
Rate = 0.15
# Calculating tax
tax = SubTotal * Rate
# Calculating Tip Amount
TipAmount = SubTotal * Tip/100
# Calculating total
Total = round(SubTotal + tax + TipAmount,2)
# Caculating total per person
totalperperson = round(Total/people,2)
# Printing owed tax
print("Total Owed: $"+str(tax))
# printing total bill
print("Total per person: $"+str(totalperperson))
