import math as m


def lineofflight(route):
	dlat = m.radians(route[2]-route[0])
	dlongt = m.radians(route[3]-route[1])
	
	a = ((m.sin(dlat/2))*(m.sin(dlat/2)))+(m.cos(m.radians(route[0])) * m.cos(m.radians(route[2])) * (m.sin(dlongt/2))*(m.sin(dlongt/2)) )
	c = 2 * m.atan2(m.sqrt(a), m.sqrt(1-a))
	d = 6378100 * c
	return d