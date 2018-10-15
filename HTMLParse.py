import re
import requests
from bs4 import BeautifulSoup
import lxml
import xlrd
from xlwt import Workbook


req=requests.get("https://bitmessage.org/wiki/")
if(req.status_code==200):
    soup=BeautifulSoup(req.content)
    soup.prettify()
    soup.find_all("a")
    for link in soup.find_all('a'):
        print(link,link.text)


'''    wb=Workbook()
    sheet1=wb.add_sheet('Raw Data')
    sheet1.write(link)
    wb.save('output.xls')
'''