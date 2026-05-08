print("Let's calculate the cost of a pizza!")


labour_cost = 0.75
rent_cost = 1.00

# 1. Get user input for pizza diameter
pizza_diameter = float(input("What is the diameter for your pizza? (in): "))

# 2. Calculate variable and total costs
materials_cost = 0.5 * pizza_diameter
subtotal = labour_cost + rent_cost + materials_cost

# 3. Apply taxes
hst = 0.13
tax = subtotal * hst
total = subtotal + tax

# 4. Display the final result rounded to two decimal places
print(f"The cost of your pizza is ${round(total, 2)}")
