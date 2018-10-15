from bs4 import BeautifulSoup

with open("https://www.google.com") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")
