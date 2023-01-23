students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Paul": 99,
    "Ama": 74,
    "Bob": 61
}

student_grades = {}

for key in students_scores:
    score = students_scores[key]
    if score > 90:
        student_grades[key] = "outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds expectation"
    elif score > 70:
        student_grades[key] = "acceptable"
    else:
        student_grades[key] = "failed"

print(student_grades)
