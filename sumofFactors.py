sum=0
i=1
n=int(input("Enter n: "))
while(i<=n):
    if(n%i==0):
         print("The number is:",i)
         sum = sum + i
    i=i+1
    print(sum)
