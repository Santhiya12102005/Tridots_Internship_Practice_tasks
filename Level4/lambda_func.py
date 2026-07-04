# lambda function to finding square of a number
x=lambda n:n**2
n = int(input("Enter number to find it's square:"))
print(x(n)) #anonyms function call lambda function

multi=lambda a,b:a*b
a=10
b=20
print(f"multiple of {a} and {b} is",multi(a,b))

# Built-in functions( map() )
num=[1,2,3,4,5]
double=list(map(lambda x:x**2,num))
print(double)

# Filter()
odd=list(filter(lambda x:x%2!=0,num))
print(odd)

# Sorted()
stud=[("Arivu",29),("Balaji",4),("Kavi",10)]
sort_stud=sorted(stud,key=lambda x:x[1])
print(sort_stud)