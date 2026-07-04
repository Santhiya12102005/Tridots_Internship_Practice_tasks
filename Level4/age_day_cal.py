from datetime import datetime,date
birth = input("Enter your birth date(YYYY-MM-DD):")
b = datetime.strptime(birth,"%Y-%m-%d").date()
today=date.today()
age = today.year-b.year
if(b.month,b.day)<(today.month,today.day):
    age-=1
days=(today-b).days
day_born=b.strftime("%A")

print("Your birth date is",birth)
print("Age is:",age)
print("Days lived so far:",days)
print("Day of the week:",day_born)
