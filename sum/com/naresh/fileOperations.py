import json

with open('E:\states.json') as f:
    data=json.load(f)

    for state in data['states']:
     del state['area_codes']
     print(state)

     with open('E:\states2.json','w') as f:
         json.dump(data,f)
         