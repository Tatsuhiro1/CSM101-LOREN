#Practice3
students = { "Ana": (90, 89, 94), "Ben": (98, 95, 97), "Carlo": (78, 82, 85), "Diana": (95, 91, 93) }
highest = 0
newhighest = ""
tally = 0
lowest = 100
namelowest = ""

for name, grade  in students.items():
    average =sum(grade)/len(grade)
    print(f"{name}, {grade}, Average:, {average:.2f}")
    if average > highest:
        highest = average
        namehighest = name
    if average < lowest:
        lowest = average
        namelowest = name
    for g in grade:
        if g < 75:
            tally += 1
print(f"Student {namehighest} is highest grade: {highest:.2f}")
print(f"Student {namelowest} is lowest grade: {lowest:.2f}")
print(f"There are {tally} students which are in total.")