import requests
import urllib
import re




#Getting the Main Page of Bit Message

hit=requests.get("https://bitmessage.org/")
status=hit.status_code
print(status)



#if(status==200):
 #   requests.get("hit/wiki/Special:Random")
  #  print(var)