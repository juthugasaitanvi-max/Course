# Pattern: A pattern is a systematic arrangement of characters like stars or numbers printed in a specific shape such as triangle or diamond.Outer loop controls the rows while the Inner loop controls the columns.end=" " is used for giving spaces between characters.

# row=int(input("Please enter how many rows you want "))
# for i in range(row):
#     for j in range(i):
#         print("$",end=" ")
#     print()

# floyd=int(input("Please enter how manyyy rowss u wanttttt!! "))
# n=1
# for i in range(1,floyd+1):
#     for j in range(1,i+1):
#         print(n,end=" ")
#         n+=1
#     print()

# floyd=int(input("Please enter how many rows u want! "))
# n=floyd
# for i in range(1,floyd+1):
#     for j in range(i):
#         print(n,end=" ")
#         n-=1
#     print()

diamond = int(input("Plz enter how many rows u want!!!!! "))
for i in range(1, diamond + 1):
    print(" " * (diamond - i) + "* " * i)

for i in range(diamond - 1, 0, -1):
    print(" " * (diamond - i) + "* " * i)