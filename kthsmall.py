n=int(input("Enter number of values"))
k=int(input("Enter the order of smallest number"))
print("Enter the values")
li=[]
for i in range(0,n):
  li.append(int(input()))
li.sort()
print(li[k-1])
