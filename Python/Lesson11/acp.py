for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

for i in range(1, 6):
    print(" " * (5-i) + "* " * i)

for i in range(4, 0, -1):
    print(" " * (5-i) + "* " * i)