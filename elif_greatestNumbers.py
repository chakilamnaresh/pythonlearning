a=10
b=8
c=22

if(a>b and a>c):
    print("The greatest number is:", a)
elif(b>a and b>c):
    print("The greatest number is:", b)
elif(c>a and c>b):
    print("The greatest number is:", c)

else:
    print("No number is greatest among these three")
