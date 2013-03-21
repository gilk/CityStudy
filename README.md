Still working out the kinks but for now it works in three stages

run point_generator.py to generate a list of random points in a city

run transit_loop.py to run the points through google maps api directions

and then plotting\ scripts/test_plot.r will create a simple plot

------------------

Current problems

Without google maps for business;

	Can only make a limited number of requests per day to generate the data sample
	
	Cannot use departure_time as a request parameter for driving directions so can only show how public transport journey times vary vs. time
