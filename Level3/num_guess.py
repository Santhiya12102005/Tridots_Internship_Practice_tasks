num = 42

cnt=0
while True:
    numm = int(input("Enter a number:"))
    if num==numm:
        print(f"You Guessed!!\nAttempt:{cnt}")
        break
    elif numm<num:
        print("Your number is To Low...Try again")
    else:
        print("Your number is To High...Try again")
    cnt+=1