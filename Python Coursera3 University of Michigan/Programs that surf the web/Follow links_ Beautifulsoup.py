#Following links
# In this assignment you will write a program to follow links.
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
# These codes are used for http documents
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_raw = input('Enter - ')

# Returns a file handle with the html document
html = urllib.request.urlopen(url_raw, context=ctx).read()

# Parse the html document and return it into a beautiful soup object
soup = BeautifulSoup(html, 'html.parser')

# Extract all tags and store it in a list
tags = soup('a')


# Repeat the process 7 times
for i in range(7):
    z = 0
    if i != 0: # from the 2nd run, parse the html to extract tags
        html = urllib.request.urlopen(answer_1,context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
    for tag in tags:
        tag_link = tag.get('href',None) # Pull out the href with the get method
        z = z+1
        if z==18: # check if the link is in the 18th position
            answer_1 = tag_link
            break

# in the assignment answer_1:- http://py4e-data.dr-chuck.net/known_by_Merina.html
# Split to find the name
answer_2 = str(answer_1)
answer_3 = answer_2.split("_")
ans = answer_3[2].split(".")
print("answer", ans[0])
