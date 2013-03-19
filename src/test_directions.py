import urllib
import json
from r_point_thrower import throwpoint

#url='http://maps.googleapis.com/maps/api/distancematrix/json?origins=Bobcaygeon+ON|41.43206,-81.38992&destinations=Darling+Harbour+NSW+Australia|24+Sussex+Drive+Ottawa+ON|Capitola+CA&mode=tranist&sensor=false&departure_time=1363280400000'
#url='http://maps.googleapis.com/maps/api/distancematrix/json?origins='
baseurl='http://maps.googleapis.com/maps/api/directions/json?'
origin=throwpoint()
destination=throwpoint()
#for x in range(0,2):
#	origins.append(throwpoint())
#	destinations.append(throwpoint())

print 'Origin = ', origin
print 'Destination = ', destination

print '  '
print '  '
print '  '

sensorstat='sensor=false'
mode='mode=transit'

url=baseurl+'origin='+str(origin[0])+','+str(origin[1])+'&'+'destination='+str(destination[0])+','+str(destination[1])+'&'+sensorstat+'&arrival_time='+str(1363748140)+'&'+mode
#print url
result=json.load(urllib.urlopen(url))

print 'this many',result['routes'][0]['legs'][0]['duration']['value']

#print len(result["rows"])
#print result

#print '  '
#print ' noon '
#print '  '
#print result

#for x in result['rows']:
#	print x['elements']


print '  '
print '  '
print '  '

url=baseurl+'origin='+str(origin[0])+','+str(origin[1])+'&'+'destination='+str(destination[0])+','+str(destination[1])+'&'+sensorstat+'&arrival_time='+str(1363456800)+'&'+mode
#print url
result=json.load(urllib.urlopen(url))



#print len(result["rows"])
#print result

#print '  '
#print ' 6pm '
#print '  '

#print result
#for x in result['rows']:
#	print x['elements']
#for x in result['routes'][0]['legs'][0]['duration']:
#	
#	print '  '
#	print '  '
#	print x
print 'this many',result['routes'][0]['legs'][0]['duration']['value']