sum=0
n=int(input("enter the number here"))
i=1
while(i<n):
    if(n%i==0):
        sum=sum+i
    i=+1
if(sum==n):
    print(n,"perfect number")
else:
    print(n,"not a perfect number")