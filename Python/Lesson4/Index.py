#Operator:An operator is a symbol in python that tells the computer to perform a specific task on 1 or more values.These symbols performs mathematical , logical , comparison and assignment operations on values known as operands.
# Operands are values or variables on which operators act 
# Types of operators:Arithmetic operators , Comparison operators , assignment operator and logical operators 
# Arithmetic operators: Perform standard mathematical calculations such as addition , subtraction , multiplication , division etc
# +:(addition)
# -:(substraction)
# *:(multiplication)  
# /:(division)
# **:(exponentiation)
# %:(modulus) : It gives us remainder.
# //:(floor division) : It gives us with quotient.

# Examples for floor division and modulus:

x=560
z=25
chocolates= x // z  # Each person recieves 22 chocolates.
leftover= x % z  # We are left with 10 chocolates.
print("distributed",chocolates)
print("remaining",leftover)

# Comparision operators: It compares 2 values or operands and return either true or false , they are decision makers of python . There are 6 comparison operators 
# ==: (equal to )
# (!=): (not equal to) 
# (>): (greater than) 
# (<): (smaller than) 
# (<=): (smaller than equal to) 
# (>=): (greater than equal to)

# Assignment Operator: They assign values to variables or update the current value of the variables with new values, often combining arithmetic or bitwise operators.
# = : (assignment)
# += : (add and assign)
# -= : (sub and assign)
# *= : (mulitply and assign)
# /= : (divide and assign)
# **= : (exponentiate and assign)
# //= : (floor divide and assign)
# %= : (modulus and assign)

# Logical Operators: They are used for logical operations such as and, or & not.


# Activity 1: A Python program that tracks a farmer's harvest across 5 fields. You will calculate the total and average yield, pack the harvest into 25 kg bags, find the leftover grain, compare this year's harvest with last year's, and update the total with a bonus crop and seed reserve.
# STEPS: 
# Step 1: Store the yield in kg for each of the 5 fields in separate variables using =.
# Step 2: Use + to add all 5 fields and store the result in total. Print total.
# Step 3: Calculate average using total / 5. Print average.
# Step 4: Set price_per_kg = 15 and caculate earnings = total * price_per_kg. Print earnings.
# Step 5: Use // to find how many full 25 kg bags can be packed. Store in bags. Print bags.
# Step 6: Use % to find the leftover grain after packing. Store in leftover. Print leftover.
# Step 7: Set last_year = 500. Use >, == , >= to compare total with last_year. Print each result.
# Step 8: Use += to add 30 kg bonus crop to total. Print the updated total.
# Step 9: Use -= to subtract 15 kg saved as seeds. Print the updated total.
# Step 10: Recalculate bags = total // 25 after all updates. Print the final bag count.