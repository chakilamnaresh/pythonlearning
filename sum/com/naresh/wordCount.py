s1='''bitty bought a butter
    but butter is bitter
    so she bought a better butter
    to make bitter butter'''

words=s1.split()
print(words)

wc=[]

for i in words:
    wc[i]=s1.count(i)
print(wc)