shop = [("Pen",15),("Pencil",10),("Eraser",15),("Note",25)]
maxx=0
minn=100
print("Shopping cart products:")
for i,j in shop:
    print(f"{i} is {j}")

for i in shop:
    maxx=max(maxx,i[1])
    minn=min(minn,i[1])

for i,j in shop:
    if maxx==j:
        print("Expensive item:",i)

for i,j in shop:
    if minn==j:
        print("Cheapest item:",i)