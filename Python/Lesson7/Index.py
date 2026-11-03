# Nested conditional statements:-
# Nesting:Placing 1 thing inside another thing , the inner statement will only run if the outer one is true.
# Nested 'if' statement:1 if statement inside another if statement 
# Ex:
Age=19
Has_license=False
# if Age>=18:
#     print("U are an adult")
#     if Has_license:
#         print("You can drive!!")
# else :
#     print("U are a child !")
#     print("You cant drive!!!!")
# if Age>=18:
#     if Has_license:
#         print("U can drive")
#     else :
#         print("You are old enough but u need a license")
# else :
#     print("U are a child!!")    



# Custom Ride Builder
# Outline:
# # A Python program that prints a welcome banner. It asks you to pick a vehicle — Bike or Car. It uses a nested if-else inside each branch to ask for a specific model. It prints the name, top speed or seats, and best use case for the chosen model. It handles invalid input with an else at the outer level. It closes with a goodbye message.

# Step 1: Print the welcome banner: " === Welcome to Ride Builder! === ".

# Step 2: Print the Step 1 menu: "1 - Bike" and "2- Car". Take input and store in choice.

# Step 3: Write the outer if for choice == 1 (Bike branch).

# Step 4: Inside the Bike branch, print the Step 2 bike menu. Take input and store in bike_type.

# Step 5: Write a nested if-else for bike_type: Scooty details if 1, Mountain Bike details if else.

# Step 6: Write the outer elif for choice == 2 (Car branch).

# Step 7: Inside the Car branch, print the Step 2 car menu. Take input and store in car_type.

# Step 8: Write a nested if-else for car_type: Sedan details if 1, SUV details if else.

# Step 9: Write the outer else to print an invalid choice message.

# Step 10: Print the closing banner: " === Your custom ride is ready!"



print(" === Welcome to Ride Builder! === ")

print("1 - Bike and 2- Car")

Choice=int(input("Please select an option from above "))
if Choice==1:
    print("Do u want a scooty or mountain bike?")
    Bike_type=int(input("Please select 1 for scooty and 2 for mountain bike "))
    if Bike_type==1:
        print("You have selected scooty,Top speed - 80km/hr")
    else :
        print("You have selected mountain bike ,Top speed - 100km/hr")
elif Choice==2:
    print("Do u want a sedan or a SUV")
    Car_type=int(input("Please select 1 for sedan and 2 for SUV "))
    if Car_type==1:
        print("You have selected sedan ,Seats -5,speed -60km/hr ")
    else :
        print("You have selected SUV ,Seats -7,speed -100km/hr")
else :
    print("Invalid option")


print(" === Your custom ride is ready!===")












