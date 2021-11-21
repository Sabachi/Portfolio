# Extract data to calculate sum
#In this assignment you will read the XML data from that URL using
#urllib and then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.


import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error


data = "http://py4e-data.dr-chuck.net/comments_1386938.xml"

#Returns a handle to read the data
uh = urllib.request.urlopen(data).read()

# ET object which has parsed XML data.
tree = ET.fromstring(uh)

# Use the method findall to gather all the çomment tags,which are children
# tags of comments.
First = tree.findall('comments/comment')
number = list()

for item in First:
    num = item.find('count').text
    #print('num', number)
    number.append(int(num))


print(sum(number))
