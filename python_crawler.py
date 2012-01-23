import BeautifulSoup
import urllib2

links = []

def parse_links(url, depth, search):
	
	page = urllib2.urlopen(url)
	soup = BeautifulSoup.BeautifulSoup(page)
	
	if depth > 0:
		for i in range(len(soup('a'))):
			if soup('a')[i]['href'].startswith('http'):
				if search in soup('a')[i]['href']:
					links.append(soup('a')[i]['href'])
				parse_links(soup('a')[i]['href'], depth-1, search)					
	else:
		return	
	
url = 'http://news.ycombinator.com/'
depth = 2
search = 'ycombinator'

parse_links(url, depth, search)

for i in range(len(links)):
		print(links[i])
	
