n=int(input("Enter number of elements"))
k=int(input("Enter the order of odd number"))
li=[]
print("Enter values")
for i in range(0,n):
  num=int(input())
  if num%2!=0:
    li.append(num)
print(li[k-1])
