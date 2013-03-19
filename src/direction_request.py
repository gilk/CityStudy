import time
import urllib
import json
def directions_request(route,mode,t=int(time.time())):
	status = True
	while status:
		url='http://maps.googleapis.com/maps/api/directions/json?'+'origin='+str(route[0])+','+str(route[1])+'&'+'destination='+str(route[2])+','+str(route[3])+'&'+'sensor=false'+'&departure_time='+str(t)+'&mode='+mode
		res = json.load(urllib.urlopen(url))
		if res['status'] == 'OK' : status = False
		if res['status'] == 'OVER_QUERY_LIMIT' : time.sleep(1)
	return res