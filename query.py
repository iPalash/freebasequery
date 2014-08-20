import requests
import sys
from pprint import pprint
query=sys.argv[1]
flags='exact=true&lang=en&format=entity&stemmed=true'
apikey='AIzaSyCXlaquY_ssvP-n-Now1jcvbg_xKHR05V0'
r = requests.get('https://www.googleapis.com/freebase/v1/search?+'+flags+'&query='+query+'&key='+apikey)
data1=r.json()
# pprint(data1) #prints the json

for i in range(len(data1['result'])):
	try:
		print data1['result'][i]['name'],
		print data1['result'][i]['score']
	except:
		print "::Non-parsable characters::"
		pass