
def sample(name,*details,**marks):
    print("Username is:",name)
    print("details:")
    for i in details:
        print(" ",i)
    for k,v in marks.items():
        print(f"{k} is {v}.")


sample("Santhiya",20,"CSE",CGPA=8.4,Core=80)


# unpacking *args and **kwargs
def unpack(a,b,c):
    return a+b+c



def unpack_kw(fname,lname):
    print(f"Hi {fname} {lname}!, we welcome you")

d={
    "fname":"Santhiya",
    "lname":"B"
}
ls=[1,2,3]
sum=unpack(*ls)
print(sum)
unpack_kw(**d)