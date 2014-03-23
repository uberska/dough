#!/usr/bin/python


import datetime


class Recurrence(object):
	def __init__(self, name):
		self.name = name

	def getDatesInRange(self, rangeStartDate, rangeEndDate):
		raise RuntimeError("Not Yet Implemented")


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
