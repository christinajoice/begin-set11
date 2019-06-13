n,k=map(int,input().split())
lis=list(map(int,input().split()))
li=[]
for i in lis:
    if i%2!=0:
        li.append(i)
print(li[k-1])
