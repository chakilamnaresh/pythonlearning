import requests
import json

params=("lat":40.71,"lon":-74)
req=requests.get("http://api.open-notify.org/iss-pass.json", params)
print(req.status_code)
print(req.content)






