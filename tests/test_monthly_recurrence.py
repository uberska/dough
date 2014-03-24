#!/usr/bin/python


import datetime
import unittest

from recurrence import *


class TestMonthlyRecurrence(unittest.TestCase):
	def setUp(self):
		startDate = datetime.date(2014, 3, 12)

		self.unboundedRecurrence = MonthlyRecurrence(10)
		# Full dates of recurrence should be
		# [
		#	... for infinity ...
		#	datetime.date(YEAR, 1, 10),
		#	datetime.date(YEAR, 2, 10),
		#	datetime.date(YEAR, 3, 10),
		#	datetime.date(YEAR, 4, 10),
		#	datetime.date(YEAR, 5, 10),
		#	datetime.date(YEAR, 6, 10),
		#	datetime.date(YEAR, 7, 10),
		#	datetime.date(YEAR, 8, 10),
		#	datetime.date(YEAR, 9, 10),
		#	datetime.date(YEAR, 10, 10),
		#	datetime.date(YEAR, 11, 10),
		#	datetime.date(YEAR, 12, 10),
		#	... for infinity ...
		# ]

		self.unboundedWithStartDateRecurrence = MonthlyRecurrence(15, startDate=startDate)
		# Full dates of recurrence should be
		# [
		#	datetime.date(2014, 3, 15),
		#	datetime.date(2014, 4, 15),
		#	datetime.date(2014, 5, 15),
		#	datetime.date(2014, 6, 15),
		#	... for infinity ...
		# ]

		self.unboundedWithNumOccurrencesRecurrence = MonthlyRecurrence(5, startDate=startDate, numOccurrences=2)
		# Full dates of recurrence should be
		# [
		#	datetime.date(2014, 4, 5),
		#	datetime.date(2014, 5, 5)
		# ]

		self.pinnedDayRecurrence = MonthlyRecurrence(31)
		# Full dates of recurrence should be
		# [
		#	... for infinity ...
		#	datetime.date(YEAR, 1, 31),
		#	datetime.date(YEAR, 2, 28), (leap year=29)
		#	datetime.date(YEAR, 3, 31),
		#	datetime.date(YEAR, 4, 30),
		#	datetime.date(YEAR, 5, 31),
		#	datetime.date(YEAR, 6, 30),
		#	datetime.date(YEAR, 7, 31),
		#	datetime.date(YEAR, 8, 31),
		#	datetime.date(YEAR, 9, 30),
		#	datetime.date(YEAR, 10, 31),
		#	datetime.date(YEAR, 11, 30),
		#	datetime.date(YEAR, 12, 31),
		#	... for infinity ...
		# ]

	def test_unbounded_recurrence(self):
		rangeStartDate = datetime.date(2014, 5, 11)
		rangeEndDate = datetime.date(2014, 9, 9)

		dates = self.unboundedRecurrence.getDatesInRange(rangeStartDate, rangeEndDate)

		self.assertEqual(dates, [
			datetime.date(2014, 6, 10),
			datetime.date(2014, 7, 10),
			datetime.date(2014, 8, 10)
		])

	def test_unbounded_with_start_date_recurrence(self):
		rangeStartDate = datetime.date(2012, 1, 1)
		rangeEndDate = datetime.date(2014, 4, 20)

		dates = self.unboundedWithStartDateRecurrence.getDatesInRange(rangeStartDate, rangeEndDate)

		self.assertEqual(dates, [
			datetime.date(2014, 3, 15),
			datetime.date(2014, 4, 15)
		])

	def test_unbounded_with_num_occurrences_recurrence(self):
		rangeStartDate = datetime.date(2000, 1, 1)
		rangeEndDate = datetime.date(2020, 1, 1)

		dates = self.unboundedWithNumOccurrencesRecurrence.getDatesInRange(rangeStartDate, rangeEndDate)

		self.assertEqual(dates, [
			datetime.date(2014, 4, 5),
			datetime.date(2014, 5, 5)
		])

	def test_pinned_day_recurrence(self):
		# This mapping is valid for 2014, which is not a leap year
		monthToNumDaysMapping = {
			1: 31,
			2: 28,
			3: 31,
			4: 30,
			5: 31,
			6: 30,
			7: 31,
			8: 31,
			9: 30,
			10: 31,
			11: 30,
			12: 31
		}

		for month in monthToNumDaysMapping:
			numDaysInMonth = monthToNumDaysMapping[month]

			rangeStartDate = datetime.date(2014, month, 1)
			rangeEndDate = datetime.date(2014, month, numDaysInMonth)

			dates = self.pinnedDayRecurrence.getDatesInRange(rangeStartDate, rangeEndDate)

			# Check that we have one date and it's the last day of the month
			self.assertEqual(dates, [datetime.date(2014, month, numDaysInMonth)])


if __name__ == '__main__':
	unittest.main()
