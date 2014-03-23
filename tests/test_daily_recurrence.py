#!/usr/bin/python


import datetime
import unittest

from recurrence import *


class TestDailyRecurrence(unittest.TestCase):
	def setUp(self):
		startDate = datetime.date(2014, 3, 1)
		dayStep = 3
		numOccurrences = 4

		self.boundedRecurrence = DailyRecurrence(startDate, dayStep, numOccurrences)
		# Full dates of recurrence should be
		# [
		#	datetime.date(2014, 3, 1),
		#	datetime.date(2014, 3, 4),
		#	datetime.date(2014, 3, 7),
		#	datetime.date(2014, 3, 10)
		# ]

		self.unboundedRecurrence = DailyRecurrence(startDate, dayStep)
		# Full dates of recurrence should be
		# [
		#	datetime.date(2014, 3, 1),
		#	datetime.date(2014, 3, 4),
		#	datetime.date(2014, 3, 7),
		#	datetime.date(2014, 3, 10),
		#	datetime.date(2014, 3, 13),
		#	datetime.date(2014, 3, 16),
		#	datetime.date(2014, 3, 19),
		#	datetime.date(2014, 3, 22),
		#	datetime.date(2014, 3, 25),
		#	datetime.date(2014, 3, 28),
		#	datetime.date(2014, 3, 31),
		#	datetime.date(2014, 4, 3),
		#	... for infinity ...
		# ]

	def test_bounded_recurrence(self):
		rangeStartDate = datetime.date(2014, 3, 2)
		rangeEndDate = datetime.date(2015, 3, 2)

		dates = self.boundedRecurrence.getDatesInRange(rangeStartDate, rangeEndDate)

		self.assertEqual(dates, [
			datetime.date(2014, 3, 4),
			datetime.date(2014, 3, 7),
			datetime.date(2014, 3, 10)
		])

	def test_unbounded_recurrence(self):
		rangeStartDate = datetime.date(2014, 3, 16)
		rangeEndDate = datetime.date(2014, 3, 31)

		dates = self.unboundedRecurrence.getDatesInRange(rangeStartDate, rangeEndDate)

		self.assertEqual(dates, [
			datetime.date(2014, 3, 16),
			datetime.date(2014, 3, 19),
			datetime.date(2014, 3, 22),
			datetime.date(2014, 3, 25),
			datetime.date(2014, 3, 28),
			datetime.date(2014, 3, 31)
		])


if __name__ == '__main__':
	unittest.main()
