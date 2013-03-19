from direction_request import directions_request
from distance_calculator import lineofflight
import os

filename='../data/London_points_4'
extension='.txt'

lines= open(filename+extension).read().splitlines()
data=[]
for line in lines:
	data.append(map(float,line.split(' ')))

fout_name_base, fout_name = filename+'_result_',filename+'_result_'+extension
ver = 1
while os.path.exists(fout_name):
	fout_name = fout_name_base + str(ver)+'.txt'
	ver += 1
outf = file(fout_name, "w")
print 'Writing output to ', outf.name

times=[1363737600] #midnight tuesday 19th march 2013
for x in range(0,24):
	times.append(times[-1]+3600)

outf.write('start_lat start_longt end_lat end_longt departure_time mode distance travel_distance travel_time\n')

for route in data:
	for dep_time in times:
		res= directions_request(route,'transit',dep_time)
		outf.write(str(route[0])+' '+str(route[1])+' '+str(route[2])+' '+str(route[3])+' '+str(dep_time)+' '+'transit'+' '+str(lineofflight(route)/1000)+' '+str(float(res['routes'][0]['legs'][0]['distance']['value'])/1000)+' '+str(res['routes'][0]['legs'][0]['duration']['value'])+'\n')
#		print res['status']
#		print float(res['routes'][0]['legs'][0]['duration']['value'])/60
#		print float(res['routes'][0]['legs'][0]['distance']['value'])/1000
#		print lineofflight(route)/1000
	
	res= directions_request(route,'bicycling',times[0])
	outf.write(str(route[0])+' '+str(route[1])+' '+str(route[2])+' '+str(route[3])+' '+str(times[0])+' '+'bicycling'+' '+str(lineofflight(route)/1000)+' '+str(float(res['routes'][0]['legs'][0]['distance']['value'])/1000)+' '+str(res['routes'][0]['legs'][0]['duration']['value'])+'\n')
	
	res= directions_request(route,'walking')
	outf.write(str(route[0])+' '+str(route[1])+' '+str(route[2])+' '+str(route[3])+' '+str(times[0])+' '+'walking'+' '+str(lineofflight(route)/1000)+' '+str(float(res['routes'][0]['legs'][0]['distance']['value'])/1000)+' '+str(res['routes'][0]['legs'][0]['duration']['value'])+'\n')
	
	res= directions_request(route,'driving',times[0])
	outf.write(str(route[0])+' '+str(route[1])+' '+str(route[2])+' '+str(route[3])+' '+str(times[0])+' '+'driving'+' '+str(lineofflight(route)/1000)+' '+str(float(res['routes'][0]['legs'][0]['distance']['value'])/1000)+' '+str(res['routes'][0]['legs'][0]['duration']['value'])+'\n')