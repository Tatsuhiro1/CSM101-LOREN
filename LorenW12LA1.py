Loren_classrecord = {
    "Liza": {
        "StudID": "S001",
        "Grade": [90, 85, 86, 82, 83, 90, 92]
    },
    "Jeremy": {
        "StudID": "S002",
        "Grade": [72, 75, 69, 80, 84, 75, 85]
    }
}
print ("========STUDENT CHECKER========")
search_input = input("Enter student name to search: ")

Loren = search_input

found_student = None


for name in Loren_classrecord:
    if Loren.lower() == name.lower():
        found_student = name
        break

if found_student:
    student_data = Loren_classrecord[found_student]
    student_id = student_data["StudID"]
    grades = student_data["Grade"]

    total = 0
    count = 0
    highest = grades[0]
    lowest = grades[0]
    needs_intervention = False


    for grade in grades:
        total += grade
        count += 1

        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade
        if grade < 60:
            needs_intervention = True

    average = total / count

    print("\nStatus: Student Found!")
    print("Student ID:", student_id)
    print("Name:", found_student)
    print("Grades:", grades)
    print(f"Average Grade: {average:.2f}")
    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)

    if needs_intervention:
        print("Candidate for intervention")
else:
    print("\nStatus: Student '" + Loren + "' not found.")