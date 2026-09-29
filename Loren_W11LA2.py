print("=== PIZZA ORDER ===")

loren_flavors = [
    (1, "Hawaiian"),
    (2, "Cheese")
]

print("Flavor:")
for loren_flavor in loren_flavors:
    print(f"{loren_flavor[0]}. {loren_flavor[1]}")

loren_choice = int(input("Choose flavor (1 or 2): "))

match loren_choice:
    case 1:
        loren_flavor = loren_flavors[0][1]
    case 2:
        loren_flavor = loren_flavors[1][1]
    case _:
        print("Invalid flavor")
        exit()


loren_sizes = [
    (1, "Small", 200),
    (2, "Medium", 300),
    (3, "Large", 400)
]

print("\nSize:")
for loren_size in loren_sizes:
    print(f"{loren_size[0]}. {loren_size[1]} - ₱{loren_size[2]}")

loren_size_choice = int(input("Choose size (1-3): "))

match loren_size_choice:
    case 1:
        loren_size = loren_sizes[0][1]
        loren_price = loren_sizes[0][2]
    case 2:
        loren_size = loren_sizes[1][1]
        loren_price = loren_sizes[1][2]
    case 3:
        loren_size = loren_sizes[2][1]
        loren_price = loren_sizes[2][2]
    case _:
        print("Invalid size")
        exit()

loren_quantity = int(input("Enter quantity: "))

loren_total = loren_price * loren_quantity
loren_final_price = loren_total

print("\n=== RECEIPT ===")
print("Flavor:", loren_flavor)
print("Size:", loren_size)
print("Quantity:", loren_quantity)
print(f"Price: ₱{loren_price:,.2f}")
print(f"Total: ₱{loren_total:,.2f}")
print(f"Final Price: ₱{loren_final_price:,.2f}")