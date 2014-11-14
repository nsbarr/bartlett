import json
import re
import string
from pprint import pprint
import urllib2

response=open('new.json')
data = json.load(response)

#sourceText = "To start over in the carved moment is to take cover"
#sourceText = "if I make you happy you are not longer doubtful"
sourceText = "Today was a very hard day because everyone got fired"
sourceText = re.split('\s+', sourceText)
pprint(sourceText)



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