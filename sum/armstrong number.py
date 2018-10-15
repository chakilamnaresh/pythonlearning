n=int(input("Enter the number here"))
new_n=n
sum=0
while(n!=0):
    r=n%10
    sum=sum+r*r*r
    n=n//10
if(sum==new_n):
    print("Armstrong number")
else:
    print("not an armstrong number")