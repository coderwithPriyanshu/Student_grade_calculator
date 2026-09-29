
print("================================")
print("     STUDENT GRADE CALCULATOR")
print("================================")

# Student ka naam
name = input("Enter student name: ")

# Subjects ke marks lena
english = int(input("Enter English marks: "))
hindi = int(input("Enter Hindi marks: "))
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
computer = int(input("Enter Computer marks: "))

# Total marks calculate karna
total = english + hindi + maths + science + computer

# Percentage calculate karna
percentage = (total / 500) * 100

# Result check karna
if (english < 33 or hindi < 33 or maths < 33
        or science < 33 or computer < 33):
    result = "Fail"
    grade = "F"
elif percentage >= 90:
    reult = "Pass"
    grade = "C"
elif percentage >= 40:
    result = "Pass"
    grade = "D"
else:
    result = "Fail"
    grade = "F"

# Final report card
print("\n================================")
print("          REPORT CARD")
print("================================")

print("Student Name:", name)
print("English:", english)
print("Hindi:", hindi)
print("Maths:", maths)
print("Science:", science)
print("Computer:", computer)

print("--------------------------------")
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)
print("================================")
print("       Thank You!")