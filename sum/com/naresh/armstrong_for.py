for i in range(1,100):
    new_i=i
    sum=0
    while(i!=0):
        r=i%10
        sum=sum+r*r*r
        i=i//10
if(sum==new_i):
    print("Armstrong number",i)


