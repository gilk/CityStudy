#Generate the all the gps points for each city's data set

from r_point_thrower import throwpoint
import os

city='London'
country='UK'
centre=[51.507222,-0.1275]
area=1570

routes=100
fout_name_base, fout_name = city+'_points',city+'_points.txt'
ver = 1
while os.path.exists('../data/'+fout_name):
	fout_name = fout_name_base +'_'+ str(ver)+'.txt'
	ver += 1
outf = file('../data/'+fout_name, "w")
print 'Writing output to ', outf.name

for n in range(0,routes):
	p1=throwpoint(city,country,centre,area)
	p2=throwpoint(city,country,centre,area)
	outf.write(str(p1[0])+' '+str(p1[1])+' '+str(p2[0])+' '+str(p1[1]))
	outf.write('\n')