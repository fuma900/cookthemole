from parse_url import recognizeTimings

def scrape(soup):
	a = soup.find_all('span', {"class":"plaincharacterwrap"})
	b = ""
	for i in range(len(a)):
		b=b+a[i].text.encode('ascii')+" "
	b = b.split(".")
	v = [{
			'index' 	: i,
			'sentence' 	: s.strip(),
			'time'		: recognizeTimings(s),
		} for i, s in enumerate(b) if len(s) > 1]

	return {	
			'length': len(v),
			'steps'	: v,
			}