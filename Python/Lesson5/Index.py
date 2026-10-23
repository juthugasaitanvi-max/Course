# Indentation:Adding blank space at the start of a line of code.It tells python which lines belong together.
# Conditional Statement:Is a descision making statement ,it checks whether something is true or false then runs the code according to the answer.
# "if" statement:The "if" statement runs the code only when the condition is true,if the condition is false it does nothing.
# "If-else" statement:This statement gives the program or code 2 paths ,One when the condition is true and another when the condition is false.
# EXAMPLE:

# age=10
# if age >=18:
#     print("u can vote")
# else:
#     print("u r too young to vote")
# Step 1: Ask for today's temperature and use if-else to decide between a jacket and a t-shirt.

# Step 2: Ask whether it is raining, and use an if statement to print an umbrella reminder.

# Step 3: Ask for the wind speed and use if-else to decide if a windbreaker is needed.

# Step 4: Ask whether there are puddles and use if-else to decide between boots and sneakers.

# Step 5: Print a message that sits outside every if and else block.

# Step 6: Print the final outfit summary with every decision made.    

temperature=int(input("enter today's temperature: "))
if temperature >=20:
    print("You should wear a t-shirt")
else:
    print("You should wear a jacket")    

is_raining=input("Is it raining today?(Yes/No): ")
if is_raining =="Yes!":
    print("Bring an umbrella")

wind_speed=int(input("enter today's wind speed: "))  
if wind_speed >=40:
    print("You need a windbreaker")
else:
    print("You don't need a windbreaker")

puddles=input("Are there puddles?(Yes/No): ")
if puddles =="Yes!":
    print("You should wear boots")
else:
    print("You should wear sneakers")
print("Weather Check completed")

