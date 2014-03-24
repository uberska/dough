#!/usr/bin/python


import calendar
import datetime


DATE_FORMAT = "%m/%d/%Y"


# http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(startDate, endDate):
	for numDaysDelta in range(int ((endDate - startDate).days)):
		yield startDate + datetime.timedelta(numDaysDelta)


# http://stackoverflow.com/questions/4130922/how-to-increment-datetime-month-in-python
def addMonthToDate(date, months=1):
	month = date.month - 1 + months
	year = date.year + (month / 12) # purposeful integer division
	month = (month % 12) + 1
	day = pinDayToMonth(year, month, date.day)
	return datetime.date(year, month, day)


def pinDayToMonth(year, month, day):
	return min(day, calendar.monthrange(year, month)[1])


def getPinnedDayOfNextMonth(year, month, day):
	"""
	Ignore the day in date and use the day passed in instead. This is useful if
	you're doing math on the date, and the date's day may have already been pinned.
	"""
	year = year + (month / 12) # purposeful integer division
	month = (month % 12) + 1
	day = pinDayToMonth(year, month, day)
	return datetime.date(year, month, day)
