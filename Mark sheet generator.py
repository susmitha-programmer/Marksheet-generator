def calculate grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B+"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
name = input("Enter student name: ")
roll = input("Enter roll number: ")
print("\nEnter marks out of 100")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
total = m1 + m2 + m3
average = total / 3
grade = calculate_grade(average)
print("\n--- Student Report ---")
print(f"Name         : {name}")
print(f"Roll Number  : {roll}")
print(f"Total Marks  : {total}/300")
print(f"Average Marks: {average:.2f}")
print(f"Grade        : {grade}")