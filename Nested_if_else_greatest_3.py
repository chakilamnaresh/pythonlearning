a=int(input("Enter the number for a:"))
b=int(input("Enter the number for b:"))
c=int(input("Enter the number for c:"))

if(a>b and a>c):
    print("The greatest of 3 numbers is ",a)

else:
    if(b>a and b>c):
        print("The greatest of 3 numbers is ",b)

    else:
        print("The greatest of 3 numbers is ",c)
