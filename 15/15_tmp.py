from datetime import date
import datetime
import calendar

#january 26-day find year
for x in range(1006,1996,10):
	#print my_date.weekday()
	if (calendar.weekday(x,1,26)==0 and calendar.isleap(x)):
		print "find : "+str(x)
	pass