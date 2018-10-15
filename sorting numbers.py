x=[5,8,1,12,4,1]
count=0
for i in range(0,len(x)):
    for j in range(i,len(x)):
        if(x[i]>x[j]):
            
            t=x[i]
            x[i]=x[j]
            x[j]=t
        if(x[i]==x[j]):
           count=count+i
            
print(x)
        
