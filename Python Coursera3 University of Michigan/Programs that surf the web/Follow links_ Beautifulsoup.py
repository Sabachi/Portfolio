#Following links
# In this assignment you will write a program to follow links.
#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers
#in the file.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_raw = input('Enter - ')
html = urllib.request.urlopen(url_raw, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')



for i in range(7):
    z = 0
    if i != 0:
        html = urllib.request.urlopen(answer_1,context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
    for tag in tags:
        tag_link = tag.get('href',None)
        z = z+1
        if z==18:
            answer_1 = tag_link
            break

answer_2 = str(answer_1)
answer_3 = answer_2.split("_")
ans = answer_3[2].split(".")
print("answer", ans[0])
