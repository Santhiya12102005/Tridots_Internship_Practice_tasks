num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
m = input("Enter anyone from(+,-,*,/,//,%,**):")
match m:
    case '+':
        print(num1+num2)
    case '-':
        print(num1-num2)
    case '*':
        print(num1*num2)
    case '/':
        print(num1/num2)
    case '//':
        print(num1//num2)
    case '%':
        print(num1%num2)
    case '**':
        print(num1**num2)
    case _:
        print("Enter valid character")

