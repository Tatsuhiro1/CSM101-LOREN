while True:

    name = input("Enter your name: ")
    loren_nohour = float(input("Enter hours: "))
    print("1] Janitor")
    print("2] Clerk")
    print("3] Cashier")
    print("4] Manager")
    choice = int(input("Enter position: "))
    again = 0
    position = ""
    loren_salary = 0
    match choice:
        case 1:
            loren_position = "Janitor"
            loren_salary = 18000
        case 2:
            loren_position = "Clerk"
            loren_salary = 22000
        case 3:
            loren_position = "Cashier"
            loren_salary = 24000
        case 4:
            loren_position = "Manager"
            loren_salary = 40000
        case _:
            print("Invalid choice")
            exit()
    halfmonth = loren_salary / 2
    loren_rateperhour = halfmonth / 88
    loren_absenceded = 0
    overtimepay = 0
    if loren_nohour >= 88:
        loren_extra = loren_nohour - 88
        loren_ot = loren_rateperhour * 1.25
        overtimepay = loren_ot * loren_extra
        loren_salary = halfmonth + overtimepay
    else:
        loren_salary = loren_nohour * loren_rateperhour
    #loren_salary = halfmonth - loren_absenceded
    print("_____________________PALDO PAY ROLL_____________________")
    print(f"Position: {loren_position}")
    print(f"Basic salary: {halfmonth:,.2f}")
    print(f"Absence deduction: {loren_absenceded:,.2f}")
    print(f"Overtime pay: {overtimepay:,.2f}")
    print(f"Net salary: {loren_salary:,.2f}")

    again = input("\nDo you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        print("Program ended.")
        break