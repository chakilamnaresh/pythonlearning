s='''Amitab is one of the finest actors
Amitab is very tall
Amitab was once in love with rekha'''

lines=s.split('\n')
print(lines)

for i in lines:
    if(i.startswith('Amitab')):
        print(i)

print(s.count("Amitab"))