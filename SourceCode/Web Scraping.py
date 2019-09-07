import requests
from bs4 import BeautifulSoup
html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
b = BeautifulSoup(html.content, "html.parser")
title = b.title.string
print(b.title.string)
print(b.find_all('a'))

Links = []
for link in b.find_all('a'):
    Links.append(link.get('href'))

print("No of Links :" , len(Links))

"Writing output to a file"
with open('webscrape.txt','w') as f:
    f.write("Title: "+title+"\n")
    f.write("Links: "+"\n")
    for link in Links:
        f.write("Link"+str(link)+"\n")

