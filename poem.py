import json
import re
import string
from pprint import pprint
import urllib2

response=open('new.json')
data = json.load(response)

#Change the source text to change the poem."
sourceText = "The palm tree exposes a large number of loose, carved spines out of pleasure Boredom"
sourceText = re.split('\s+', sourceText)



#This poem generator takes each word from your Source Text and looks it up in the Concordance Index
#of Bartlett's Quotations. If it's there, the generator gives you the Nth quotation snippet for that
#word, where N is the position of the word in the source text (5th word gets 5th quote, etc.)
#If there aren't enough quotations, the generator just returns the first one.

for word in sourceText:
	punctuatedWord = word+','
	for keyval in data["results"]:
		keyword = keyval["keyword"].encode("utf-8")
		if keyword.lower() == word or keyword.lower() == punctuatedWord:
			try: 
				pprint(keyval["entry"][sourceText.index(word)].encode("utf-8"))
			except IndexError:
				pprint(keyval["entry"][0].encode("utf-8"))