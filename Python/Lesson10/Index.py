# Nested loop:A loop inside anither loop
# Nested while loop is a while loop inside a while loop.
# Example:
# i=1
# while i <=3:
#     j=1
#     while j <=2:
#         print("i=",i,"j=",j)
#         j+=1
#     i+=1


# Nested for loop is a for loop inside a for loop.
# Example:
# for i in range(1,6):
#     for j in range(i):
#         print("?",end =" ")
#     print()

#Continue:Skips the remaining code in the current loop and jumps straight back to the condition 

#Example:
for i in range(1,4):
    for j in range(1,4):
        if j==3:
            continue
        print("i=",i,"j=",j)

# Uses of nested loop:Whenever we need to work with things that have 2 or more levels        
# for example:tables,patterns,matrices.

#CLASSROOM ACTIVITY

#ATM Cash Dispenser
#Outline:
#This one activity keeps you working with both nested loop types end to end - a daily ATM session that serves several customers, then a denomination report printed once the day is done.

# Step 1: Set up six counter variables (one per note value) plus counters for customers served and total dispensed, all starting at 0.

# Step 2: Start an outer while loop that keeps serving customers until the flag variable serving becomes False.

# Step 3: Ask for the customer's name and withdrawal amount; if the amount is invalid, print a message and continue back to the top of the loop.

# Step 4: Inside that same repeat, run an inner while loop that checks each of the six note values one at a time and works out how many of each note to dispense.

# Step 5: Update the matching counter variable for whichever note value was just dispensed, then ask if there is a next customer, setting serving to False if not.

# Step 6: Once the outer while loop ends, start an outer for loop stepping through each of the six note values to print the daily denomination report.

# Step 7: Inside that same repeat, run an inner for loop that prints one symbol for every note of that value dispensed across the whole day.