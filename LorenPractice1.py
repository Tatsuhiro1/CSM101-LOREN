#Practice 1
students = {
    "Ana": 85,
    "Ben": 98,
    "Carlo": 78,
    "Diana": 95
}
print("Students Grades")
print("-----------------")
print("Ana: ", students["Ana"])
print("Ben: ", students["Ben"])
#add a new student
students["Ella"] = 88
#updates a students grade
students["Carlo"] = 82
students["Diana"] = 91
name1 = input("Enter student name: ")
grade1 = input("Enter grade: ")
students[name1] = grade1

print(students)
print("\nUpdated Students Grades")
print("-----------------")

for name, grade in students.items():
    print(name.capitalize(), ":", grade)




#Search for a student
search_name = input("Enter student name to search: ")
while True:
    search_name = input("Enter student name to search: ")

    if search_name in students:
        print(search_name, ":", students[search_name])
    else:
        print("Student not found.")

    search_continue = input("Do you want to search another student? (yes/no): ")

    if search_continue.lower() != "yes":
        print("Exiting... Thank you for Using!")
        break