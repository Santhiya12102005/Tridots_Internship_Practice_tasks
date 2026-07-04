def safe_divider():
    try:
        num1=int(input("Enter num1:"))
        num2=int(input("Enter num2:"))
        res=num1/num2
    except ZeroDivisionError:
        print(f"Error: {num1} Cannot Divided by {num2}")
    except ValueError:
        print("Error: Integer only accepted")
    else:
        print(f"Result is {res}")

safe_divider()
    