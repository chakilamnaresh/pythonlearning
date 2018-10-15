nan = '''bitty bought a 10/- butter.
        but butter is bitter
        so she bought a better butter &
        to make bitter butter better'''

print(nan.isspace())
print(nan.islower())
print(nan.isalpha())
print(nan.isalnum())
print(nan.isdigit())


max(nan)
min(nan)

s=0 #sentences
sp=0 #space
w=0  #words
l=0  #new line
a=0 #alpha
d=0 #digit
i=0
while(i<len(nan)):
    if(nan[i].isalpha()):
        s=s+1
    i=i+1







