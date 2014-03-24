#!/usr/bin/python


import datetime

from date import DATE_FORMAT
from date import getPinnedDayOfNextMonth
from date import pinDayToMonth


def loadRecurrenceFromJsonObj(jsonObj):
	if jsonObj["type"] == "daily":
		startDate = datetime.datetime.strptime(jsonObj["start"], DATE_FORMAT).date()
		dayStep = int(jsonObj["step"])
		return DailyRecurrence(startDate, dayStep)
	else:
		raise RuntimeError("Unknown recurrence type: %s" % jsonObj["type"])


class Recurrence(object):
	def __init__(self, name):
		self.name = name

	def getDatesInRange(self, rangeStartDate, rangeEndDate):
		raise RuntimeError("Not Yet Implemented")

	def isOnDate(self, date):
		return len(self.getDatesInRange(date, date)) == 1


class DailyRecurrence(Recurrence):
	def __init__(self, startDate, dayStep=1, numOccurrences=None):
		super(DailyRecurrence, self).__init__("daily")

		self.startDate = startDate

		self.dayStep = dayStep

		self.numOccurrences = numOccurrences

	def getDatesInRange(self, rangeStartDate, rangeEndDate):
		dates = list()

		occurrences = 1

		# Check if we don't start until after the range
		if self.startDate > rangeEndDate:
			return dates

		# Figure out our first date within the range
		currentDate = self.startDate

		while currentDate < rangeStartDate and \
			(not self.numOccurrences or occurrences <= self.numOccurrences):

			currentDate += datetime.timedelta(self.dayStep)
			occurrences += 1

		# Add dates from now until the end of the date range
		while currentDate <= rangeEndDate and \
			(not self.numOccurrences or occurrences <= self.numOccurrences):

			dates.append(currentDate)
			currentDate += datetime.timedelta(self.dayStep)
			occurrences += 1

		return dates


class MonthlyRecurrence(Recurrence):
	def __init__(self, dayOfMonth, startDate=None, numOccurrences=None):
		super(MonthlyRecurrence, self).__init__("monthly")

		if numOccurrences and not startDate:
			raise RuntimeError("You can not specify a number of ocurrences without a start date.")

		self.dayOfMonth = dayOfMonth

		self.startDate = startDate

		self.numOccurrences = numOccurrences

	def getDatesInRange(self, rangeStartDate, rangeEndDate):
		dates = list()

		occurrences = 1

		# Figure out which month to start in
		if self.startDate:
			# If we have a start date, start in the same month as the start date
			srcDate = self.startDate
		else:
			# If there's no start date, then our recurrence has infinite timing. Start in
			# the same month as our range
			srcDate = rangeStartDate

		year = srcDate.year
		month = srcDate.month
		day = pinDayToMonth(year, month, self.dayOfMonth)

		currentDate = datetime.date(year, month, day)

		# Either case above can end up with a currentDate with days before srcDate's
		# days. In that case, we need to go one more month ahead to start.
		if currentDate < srcDate:
			currentDate = getPinnedDayOfNextMonth(currentDate.year, currentDate.month, self.dayOfMonth)

		# Add dates from now until the end of the date range if we haven't
		# reached our max number of occurrences and the date is after the start
		# of the range.
		while currentDate <= rangeEndDate and \
			(not self.numOccurrences or occurrences <= self.numOccurrences):

			# Check if we've reach the start of our range
			if currentDate >= rangeStartDate:
				dates.append(currentDate)

			currentDate = getPinnedDayOfNextMonth(currentDate.year, currentDate.month, self.dayOfMonth)

			occurrences += 1

		return dates
