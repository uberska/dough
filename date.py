#!/usr/bin/python


import datetime


DATE_FORMAT = "%m/%d/%Y"


# http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(startDate, endDate):
	for numDaysDelta in range(int ((endDate - startDate).days)):
		yield startDate + datetime.timedelta(numDaysDelta)
