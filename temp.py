a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))

if(a>b and a>c):
    print("The greatest of 3 numbers is ",a)

else:
    if(b>a and b>c):
        print("The greatest of 3 numbers is ",c)

    else:
        if(c>a and c>b):
            print("The greatest of 3 numbers is ",c)
