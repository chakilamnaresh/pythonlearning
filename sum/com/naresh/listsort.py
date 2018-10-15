x = [5, 5,1,1,1,12,4,1,5,5,16,88,4,4,8, 1, 12, 4, 1]

for i in range(0, len(x)):
    count = 0
    for j in range(0, len(x)):
        if (x[i]==x[j]):
            count = count + 1

print(x)