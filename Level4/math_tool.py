def area_circle(r):
    return 3.14*r*r

def area_rect(w,h):
    return w*h

def is_even(num):
    if num%2==0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

def factorial(n):
    val=1
    for i in range(1,n+1):
        val*=i
    return val

r=int(input("Enter radius:"))
print("Areaof the circle:",area_circle(r))
w=int(input("Enter length:"))
h=int(input("Enter length:"))
print("Area of the rectangle:",area_rect(w,h))
num=int(input("Enter a number:"))
is_even(num)
n=int(input("Enter a number:"))
print(f"Factorial of {n} is ",factorial(n))