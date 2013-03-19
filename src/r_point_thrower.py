from math import pi
import math as m
import random
import urllib
import json

def throwpoint(city='London',country='UK',centre=[51.507222,-0.1275],area=1570):
	centre=map(m.radians,centre)
	EarthRadius=6372.796924
	radius=m.sqrt(area/pi)/EarthRadius
	inCity=False
	while(not inCity):
		dist= radius*random.random()
		direction=2*pi*random.random()
		newp=[0,0]
		newp[1]+=m.atan2(m.sin(direction)*m.sin(dist)*m.cos(centre[0]),m.cos(dist)-m.sin(centre[0])*m.sin(centre[0]))
		newp[0]=m.asin(m.sin(centre[0])*m.cos(dist) + m.cos(centre[0])*m.sin(dist)*m.cos(direction))
		newp=map(m.degrees,newp)
		url='http://maps.googleapis.com/maps/api/geocode/json?latlng='+str(newp[0])+','+str(newp[1])+'&sensor=false'
#		print url
		query=json.load(urllib.urlopen(url))
		#print query
		if(query['status']=='OK'):
			for address in query['results']:
				if(address['formatted_address']==city+', '+country): inCity=True
		return newp
#city='Paris'
#centre=[51.507222,-0.1275]
#print centre
#area=1570
#print 'with arguments'
#throwpoint(city,centre,area)

#print 'without arguments'
#for x in range(1,10):
#	print x, throwpoint()