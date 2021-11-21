# Extracting data from JSON
# In this assignment you will provide a prompt for a URL,
# read the JSON data from that URL using urllib and then parse and extract
#the comment counts from the JSON data and compute the sum of the numbers in
#the file.

import urllib.request, urllib.parse, urllib.error
import json

url_raw = input('Enter - ')

# Gives a handle into which the document has been read
data = urllib.request.urlopen(url_raw).read()
number = list()

# Parse the JSON and store it as dictionary
info = json.loads(data)

# Dumps the data in json format, to receive readable data
print(json.dumps(info, indent = 4))
print('User count:', len(info))
items = info["comments"] # extract value for the key comments

for item in items:
    num = item["count"] # extract value for the key count
    print(num)
    number.append(num)


print(sum(number))
