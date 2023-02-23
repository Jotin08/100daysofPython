print("Welcome to the Tip Calculator!")
bill = input("What is the total bill?\n$")
tip = input("What percentage of tip would you like to pay?\n")
split = input("How many people will split the bill?\n")

# conver out inputs into floats and int so we can do some math
total_bill = float(bill)

tip_percentage = int(tip) / 100
tip_amount = tip_percentage * total_bill

split_bill = int(split)

final_amount = "{:.2f}".format((total_bill + tip_amount) / split_bill)

message = (f"Each person should pay: ${final_amount}")
print(message)
