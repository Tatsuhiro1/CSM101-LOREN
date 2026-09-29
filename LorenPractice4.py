#Practice 4
number = int(input("Enter a number of students: "))
students = {}

for i in range(number):
    print("\nStudent", i + 1)

    name = input("Enter Student name: ")

    g1 = float(input("Enter Grade 1: "))
    g2 = float(input("Enter Grade 2: "))
    g3 = float(input("Enter Grade 3: "))

    students[name] = [g1, g2, g3]
print("\nStudent Records:")

highest = 0
namehighest = ""

lowest = 100
namelowest = ""

tally = 0

for name, grade in students.items():
    average = sum(grade) / len(grade)

    print(name, grade, "Average:", round(average, 2))

    if average > highest:
        highest = average
        namehighest = name

    if average < lowest:
        lowest = average
        namelowest = name

    if average > 75:
        tally += 1


print(f"\nStudent {namehighest} is highest grade: {highest:.2f}")
print(f"Student {namelowest} is lowest grade: {lowest:.2f}")
print(f"There are {tally} students with an average above 75.")