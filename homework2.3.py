students = {
    "Ana": [89, 66, 12, 75, 11],
    "Giorgi": [67, 72, 90, 91, 55],
    "Levant": [49, 36, 88, 98, 34],
    "Veronika": [99, 88, 32, 65, 99],
    "Nika": [77, 81, 41, 73, 99]
}


for name, grades in students.items():
    average = sum(grades) / len(grades)

    if average >= 90:
        final_grade = "A"
    elif average >= 80:
        final_grade = "B"
    elif average >= 70:
        final_grade = "C"
    elif average >= 60:
        final_grade = "D"
    else:
        final_grade = "F"
    print(f"{name}-ს საშუალო ქულაა: {average:.2f}  ნიშანი: {final_grade}")
