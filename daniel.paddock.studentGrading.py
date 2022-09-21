print("Welcome to GPA Calculator")
input("Student name")
input("Student SCID")
a = int(input("Enter your percentage on Assignments"))
b = int(input("Enter your percentage on Labs"))
c = int(input("Enter your percentage on Reading Exercises"))
d = int(input("Enter your percentage on quizzes"))
e = int(input("Enter your percentage on Midterm"))
f = int(input("Enter your percentage on Project"))
total = a+b+c+d+e+f
if total >= 94:
    print("letter grade: A")
    print("grade point: 4.00")
    print("excellent performance")
elif total >= 90:
    print("letter grade: A-")
    print("grade point: 4.67")
    print("excellent performance")
elif total >= 87:
    print("letter grade: B+")
    print("grade point: 3.33")
    print("good performance")
elif total >= 84:
    print("letter grade: B")
    print("grade point: 3.00")
    print("good performance")
elif total >= 80:
    print("letter grade: B-")
    print("grade point: 2.67")
    print("good performance")
elif total >= 77:
    print("letter grade: C+")
    print("grade point: 2.33")
    print("average performance")
elif total >= 74:
    print("letter grade: C")
    print("grade point: 2.00")
    print("average performance")
elif total >= 70:
    print("letter grade: C-")
    print("grade point: 1.67")
    print("average performance")
elif total >= 65:
    print("letter grade: D+")
    print("grade point: 1.33")
    print("unsatisfactory performance")
elif total >= 60:
    print("letter grade: D")
    print("grade point: 1.00")
    print("unsatisfactory performance")
elif total >= 55:
    print("letter grade: D-")
    print("grade point: 0.67")
    print("unsatisfactory performance")
elif total <= 54.99:
    print("letter grade: F")
    print("grade point: 0.00")
    print("failing performance")
