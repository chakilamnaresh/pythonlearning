import re
regex=r"x[a-e]y"
matches=re.findall(regex,"x[a-e]y,xay,xby,xcy,xdy,xey,xhy")
print(matches)


import re
regex=(Java|pythhon|hadoop)
matches=re.findall(regex,"java,python,hadoop,salesforce")
print(matches)
