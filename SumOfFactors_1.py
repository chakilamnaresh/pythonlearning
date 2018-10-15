count=0
i=1
n=int(input("enter n: "))
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
print(count)