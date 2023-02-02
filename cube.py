n=int(input("enter number"))
list=[]
for i in range(n+1):
    list.append(i**3)
print(list)

print([i**3 for i in range(11)])