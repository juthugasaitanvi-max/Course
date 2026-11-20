customers = [
    ["Ravi", [("Rice", 50), ("Milk", 30), ("Bread", 25)]],
    ["Priya", [("Sugar", 40), ("Oil", 120), ("Eggs", 60)]],
    ["Amit", [("Apple", 80), ("Bad Entry", -10), ("Juice", 45)]]
]

print("===== GROCERY BILLING REPORT =====")

for customer in customers:
    name = customer[0]
    items = customer[1]
    total = 0

    print("\nCustomer:", name)
    print("-------------------------")

    
    for item, price in item:

        if price <= 0:
            print(item, "- Rejected (Invalid price)")
            continue

        print(item, "-", price)
        total += price

    print("-------------------------")
    print("Total Bill: Rs.", total)

print("\n===== BILLING COMPLETED =====")
