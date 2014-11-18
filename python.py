import json
import re
from pprint import pprint
import urllib2

API_KEY = 'Get your own'
offset = 0
newCollection = []

while offset <39000: #hardcoded whatevs
	url = 'https://www.kimonolabs.com/api/5ycszq5u?apikey=%s&kimoffset=%d' % (API_KEY, offset)
	response = urllib2.urlopen(url)
	data = json.load(response)
	
	for keyval in data["results"]["collection1"]:
		keyword = keyval["keyword"].encode("utf-8")
		if keyword:
			#grab the first word of the entry and set it as the keyword
			keyval["keyword"] = keyword.split(' ')[0]
			newEntryText = ' '.join(keyword.split(' ')[1:])
			#convert all entries to list
			
			# WHY?
			if len(keyval["entry"]):
				keyval["entry"].insert(0, newEntryText)
			else: 
				keyval["entry"] = [newEntryText]

		#remove page numbers from entries
		newEntryList = []	

		for entry in keyval["entry"]:
			entryJoin = ' '.join(entry.split(' ')[1:])
			newEntryList.append(entryJoin)
		keyval["entry"] = newEntryList

		newCollection.append(keyval)

		
	offset += 2500

pprint json.dumps(data, indent=4)
