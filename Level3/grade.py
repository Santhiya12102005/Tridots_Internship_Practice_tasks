mark = int(input("Enter your grade(0-100):"))
if mark>=90 and mark<=100:
    print("Grade:A\nResult: Pass")
elif mark>=80 and mark<90:
    print("Grade:B\nResult: Pass")
elif mark>=70 and mark<80:
    print("Grade:C\nResult: Pass")
elif mark>=60 and mark<70:
    print("Grade:D\nResult: Pass")
else:
    print("Grade:F\nResult:Fail")