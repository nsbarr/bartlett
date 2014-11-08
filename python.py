import json
import re
from pprint import pprint
import urllib2

url = 'https://www.kimonolabs.com/api/5ycszq5u?apikey=ljg3wCjOnciTusPUO6b7KWNsBtShygVN' #don't steal my key bro
paginatorKey = "&kimoffset="
initialOffset = 0
newCollection = []

while initialOffset <39000: #hardcoded whatevs
	response = urllib2.urlopen(url+paginatorKey+str(initialOffset))
	data = json.load(response)   

	for keyval in data["results"]["collection1"]:

		keyword = keyval["keyword"].encode("utf-8")

		if keyword != "":

			#grab the first word of the entry and set it as the keyword
			split = re.split('\s+', keyword)
			lengthOfSplit = len(split)
			firstWord = split[0]
			keyval["keyword"] = firstWord

			#grab the rest of the entry and set it as the entry
			split.pop(0)
			newEntryText = ' '.join(split)

			pprint(type(keyval["entry"]))

			#convert all entries to lists
			if type(keyval["entry"]) == list:
				keyval["entry"].insert(0,newEntryText)
			else: 
				keyval["entry"] = [newEntryText]

		#remove page numbers from entries
		newEntryList = []	

		for entry in keyval["entry"]:
			entrySplit = re.split('\s+', entry)
			entrySplit.pop()
			entryJoin = ' '.join(entrySplit)
			newEntryList.append(entryJoin)
		keyval["entry"] = newEntryList

		newCollection.append(keyval)

		
	initialOffset +=2500

data["results"] = newCollection

with open('new.json', 'w') as json_data:
	json.dump(data, json_data, indent=4)

