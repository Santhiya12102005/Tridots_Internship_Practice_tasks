# built in errors handling
num=int(input("Enter a number:"))
div=int(input("Enter a divisor:"))

try:
    res=num//div
except ZeroDivisionError:
    print(f"Error Occured: {num} cannot divided by {div}")
else:
    print(f"Result is {res}")
finally:
    print("Task Completed....")

# manual error handling
st="Hello"
if not type(st) is int:
    raise Exception("Only integers are allowed")