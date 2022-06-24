import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

link = 'http://py4e-data.dr-chuck.net/comments_1514535.xml'
html = urllib.request.urlopen(link).read().decode()

sum = 0
data = ET.fromstring(html)
tags = data.findall('comments/comment')

for tag in tags:
    sum += int(tag.find('count').text)

print('Sum:', sum)