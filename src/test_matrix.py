import urllib
import json
from r_point_thrower import throwpoint

#url='http://maps.googleapis.com/maps/api/distancematrix/json?origins=Bobcaygeon+ON|41.43206,-81.38992&destinations=Darling+Harbour+NSW+Australia|24+Sussex+Drive+Ottawa+ON|Capitola+CA&mode=tranist&sensor=false&departure_time=1363280400000'
#url='http://maps.googleapis.com/maps/api/distancematrix/json?origins='
baseurl='http://maps.googleapis.com/maps/api/distancematrix/json?'
origins=[]
destinations=[]
for x in range(0,2):
	origins.append(throwpoint())
	destinations.append(throwpoint())

print 'Origins = ', origins
print 'Destinations = ', destinations
urlorigins='origins='+str(origins[0][0])+','+str(origins[0][1])
for x in origins[1:]:
	urlorigins+='|'+str(x[0])+','+str(x[1])
print urlorigins

urldestinations='destinations='+str(destinations[0][0])+','+str(destinations[0][1])
for x in destinations[1:]:
	urldestinations+='|'+str(x[0])+','+str(x[1])
print urldestinations
print '  '
print '  '
print '  '
sensorstat='sensor=false'

mode='mode=transit'

url=baseurl+urlorigins+'&'+urldestinations+'&'+sensorstat+'&arrival_time='+str(1363748140)+'&'+mode
print url
result=json.load(urllib.urlopen(url))



#print len(result["rows"])
#print result

print '  '
print ' noon '
print '  '


for x in result['rows']:
	print x['elements']


url=baseurl+urlorigins+'&'+urldestinations+'&'+sensorstat+'&arrival_time='+str(1363456800)+'&'+mode
print url
result=json.load(urllib.urlopen(url))



#print len(result["rows"])
print result

print '  '
print ' 6pm '
print '  '


for x in result['rows']:
	print x['elements']
