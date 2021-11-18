#Scraping numbers
# In this assignment you will scrape numbers using Beautifulsoup.
# Use urlib to read the HTML from the data files below, and parse the data,
#extracting numbers and compute the sum of the numbers in the file.


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

results = list()

# Retrieve all of the anchor tags
tags = soup('span')
#print("tags",tags)

for tag in tags:
    print("new line", tag)
    tag_1 = str(tag)
    result = tag_1.split()
    result_1 = result[1].split('>')
    result_2 = result_1[1].split('<')
    result_3 = int(result_2[0])
    results.append(result_3)


print(sum(results))
