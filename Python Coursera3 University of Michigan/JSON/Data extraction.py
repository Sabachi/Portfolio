# Extracting data from JSON
# In this assignment you will provide a prompt for a URL,
# read the JSON data from that URL using urllib and then parse and extract
#the comment counts from the JSON data and compute the sum of the numbers in
#the file.

import urllib.request, urllib.parse, urllib.error
import json

url_raw = input('Enter - ')
data = urllib.request.urlopen(url_raw).read()
number = list()

info = json.loads(data)
print(json.dumps(info, indent = 4))
print('User count:', len(info))
items = info["comments"]

for item in items:
    num = item["count"]
    print(num)
    number.append(num)


print(sum(number))
