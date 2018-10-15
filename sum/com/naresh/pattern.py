n=int(input("enter n"))
for i in range (1,n):
    for s in range (n-1,i,-1):
        print(" ", end=" ")
        for j in range (1,i+1):
            print("*")
    print()
