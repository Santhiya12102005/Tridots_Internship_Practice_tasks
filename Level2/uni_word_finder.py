s = "book teaches knowledge, book inspires everyone."
ls  =s.split()
print("Splitting the words:\n",ls)
s1=set(ls)
print("Uniques words:\n",s1)
print("No Of duplicates removed:",len(ls)-len(s1))