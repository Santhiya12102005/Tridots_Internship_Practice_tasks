stud={
    'Name':'Santhiya',
    'Age':20,
    'Grade':'B',
    'Subject':'Maths'
}
print("Student dictionary:")
for k,v in stud.items():
    print(f"{k} is {v}")

print("After updation:")
stud.update({"Passed":"True"})
for k,v in stud.items():
    print(f"{k} is {v}")