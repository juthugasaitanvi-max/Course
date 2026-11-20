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
# for i in range(1,4):
#     for j in range(1,4):
#         if j==3:
#             continue
#         print("i=",i,"j=",j)

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

note100=0
note50=0
note20=0
note150=0
note200=0
note10=0

customers_served=0
total_dispensed=0

Serving=True
while Serving :
    name=input("Enter customer name ")
    withdrawal_amount=int(input("Enter the withdrawal amount "))
    if withdrawal_amount <=0:
        print("Invalid amount")
        continue
    x=1
    remaining=withdrawal_amount
    while x <=6:
        if x==1:value=10
        elif x==2:value=20
        elif x==3:value=50
        elif x==4:value=100
        elif x==5:value=150
        else:value=200
        count=remaining//value
        if count >0:
            remaining-=count*value
            if value==200:note200+=count
            elif value==150:note150+=count
            elif value==100:note100+=count
            elif value==50:note50+=count
            elif value==20:note20+=count
            else:note10+=count
        x+=1
    customers_served+=1
    total_dispensed+=withdrawal_amount
    print("Transaction complete")
    next_customer=input("Next customer (YES/NO) ").strip().lower()
    if next_customer!="yes":
        Serving=False
print("Customers served",customers_served)
print("Total dispensed",total_dispensed)

            