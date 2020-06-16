friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}


]
print(friends[1]["name"])


# another example

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")


# using in keyword with dictionary:

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class.")



# using .values() to get values

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))