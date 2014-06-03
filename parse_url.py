import sys, re

sys.path.insert(0, 'lib')

import urllib2
import importlib, logging
from bs4 import BeautifulSoup
import appengine_config

# Same as parse() except it split in a list of steps.
def parseCollection(message):
	url = message.sentence
	provider = recognizeProvider(url)
	logging.info('provider.' + provider + '.scrape')
	try:
		provider = importlib.import_module('provider.' + provider)
	except:
		logging.warning("Provider doesnt exist")
		raise 404

	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)
	return provider.scrape(soup)

# Strip domain from url and return string like:
# http://www.google.co.uk -> google_co_uk
def recognizeProvider(url):
	urlsplit = url.split('/')
	if (urlsplit[0] == 'http:' or 'https:'):
		v = urlsplit[2].split('www.')
	else:
		v = urlsplit[0].split('www.')
	v = v[len(v)-1].split('.')
	v = "_".join(v)
	return v

def recognizeTimings(sentence):
	minutes = 	[	'm',
					'min',
					'minute',
					'minutes',]
	hours = 	[	'h',
					'hrs',
					'hour',
					'hours',]
	numbers = 	{
					'an' 		: 1,
					'a' 		: 1,
					'two' 		: 2,
					'couple'	: 2,
					'three'		: 3,
					'four'		: 4,
					'dozen'		: 12,}
	t = 0;
	words = re.split(" |,|;|:", sentence);
	for i, word in enumerate(words):
		if i is not 0:
			if word in minutes:
				try: 
					t += int(words[i-1])
				except:
					pass
			if word in hours:
				try: 
					t += 60*int(words[i-1])
				except:
					pass
	return t