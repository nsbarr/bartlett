import json
import re
import string
from pprint import pprint
import urllib2

response=open('new.json')
data = json.load(response)

sourceText = "To start over in the carved moment is to take cover"
sourceText = re.split('\s+', sourceText)
pprint(sourceText)


for word in sourceText:
	punctuatedWord = word+','
	for keyval in data["results"]:
		keyword = keyval["keyword"].encode("utf-8")
		if keyword.lower() == word or keyword.lower() == punctuatedWord:
			try: 
				pprint(keyval["entry"][sourceText.index(word)].encode("utf-8"))
			except IndexError:
				pprint(keyval["entry"][0].encode("utf-8"))