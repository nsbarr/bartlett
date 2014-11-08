#&kimoffset=2500
import urllib2
import json
import re
from pprint import pprint

url = 'https://www.kimonolabs.com/api/5ycszq5u?apikey=ljg3wCjOnciTusPUO6b7KWNsBtShygVN'
paginatorKey = "&kimoffset="
initialOffset = 0

while initialOffset <39000:
	response = urllib2.urlopen(url+paginatorKey+str(initialOffset))
	data = json.load(response)   
	print data
	initialOffset +=2500


#maxOffset = 38000



