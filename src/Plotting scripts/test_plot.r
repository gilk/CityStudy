dat<-read.table(file="../../data/London_points_1_result_.txt",header=TRUE)
attach(dat)
#plot(mode ~ travel_time, type='l')
#names(dat)
#summary(dat)
#attributes(dat)
#dat$mode
#plot(subset(dat,mode=='transit',select=c(departure_time,travel_time)),col='red')
#min(departure_time)
#max(departure_time)
x<-seq(min(departure_time),max(departure_time),by=3600)
#y<-mean(subset(dat,dat$departure_time==x)$travel_time)

y<-sapply(x,function(x) mean(subset(dat,dat$departure_time==x)$travel_time))





plot(x,y,type='l',ylim=c(1000,10000),xlab='Departure Time (UNIX time)', ylab='Average journey time (Seconds)')

#mean(subset(dat,mode=='bicycling',select=c(travel_time)))


abline(h=mean(subset(dat,mode=='bicycling',select=c(travel_time))),col='green')
abline(h=mean(subset(dat,mode=='walking',select=c(travel_time))),col='blue')
abline(h=mean(subset(dat,mode=='driving',select=c(travel_time))),col='yellow')
