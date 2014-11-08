import json
import re
from pprint import pprint
import urllib2


#paginator: &kimoffset=2500

#json_data=open('better.json')

#with open('better.json', 'r') as json_data:
#	data = json.load(json_data)

url = 'https://www.kimonolabs.com/api/5ycszq5u?apikey=ljg3wCjOnciTusPUO6b7KWNsBtShygVN'
paginatorKey = "&kimoffset="
initialOffset = 0
newCollection = []

while initialOffset <39000:
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
			split.pop(0)
			newEntryText = ' '.join(split)

			pprint(type(keyval["entry"]))

			if type(keyval["entry"]) == list:
				keyval["entry"].insert(0,newEntryText)
			else: 
				keyval["entry"] = [newEntryText]

			#newCollection.append(keyval)

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

