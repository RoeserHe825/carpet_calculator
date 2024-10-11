# Henry Roeser
# 10/11/2024
# Carpet Calculator 

# Input


length = input("Enter the length of the room in feet: ")
width =  input("Enter the width of the room in feet: ")
carpet_price = input("Enter the price per square yard for the carpet between $2.00 and $4.50: ")

# Convert the user's input (length/width/carpet price) to NUMBERS so we can do some math later on in the script
length = float(length)
width = float(width)
carpet_price = float(carpet_price)

# Process

# Calculate the area (in square feet) of the room
area = length * width # Area in square feet

# Next, calculate the number of SQUARE YARDS of carpet we need to buy to cover the room
square_yards_of_carpet = area / 9


# Calculate subtotal (before any taxes are applied)
subtotal = square_yards_of_carpet * carpet_price

# Calculate the Michigan state sales tax
SALES_TAX_RATE = .06
order_sales_tax = subtotal * SALES_TAX_RATE

# Calculate the grand total on the order
grand_total = subtotal + order_sales_tax

# total = float(length * width)
# new_total = total * 2 
# total


# Output
print(f"You need {square_yards_of_carpet:.2f} square yards of carpet.")
print(f"The order subtotal is ${subtotal:.2f} ")
print(f"The state sales tax is ${order_sales_tax:.2f} ")
print(f"The grand total is ${grand_total:.2f} ")