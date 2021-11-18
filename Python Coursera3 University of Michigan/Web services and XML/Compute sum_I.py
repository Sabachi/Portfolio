# Extract data to calculate sum
#In this assignment you will read the XML data from that URL using
#urllib and then parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file.

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error


data = "http://py4e-data.dr-chuck.net/comments_1386938.xml"
uh = urllib.request.urlopen(data).read()
tree = ET.fromstring(uh)

First = tree.findall('comments/comment')
number = list()

for item in First:
    num = item.find('count').text
    #print('num', number)
    number.append(int(num))


print(sum(number))
