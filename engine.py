#!/usr/bin/python


import datetime

from data import Data
from date import daterange


class Engine(object):
	def __init__(self, accounts, balanceModifiers, today=None):
		"""
		today should not be set outside of unit tests. It's needed since
		the Engine currently only supports calculating dates in the future.
		Until this is changed, the unit tests will run as if they are running
		from a fixed date in time.
		"""

		self.accounts = accounts

		self.balanceModifiers = balanceModifiers

		self.today = today

	def execute(self, startDate, endDate, today=None):
		data = Data()

		# Allow modifying today for unit tests to work consistently
		if self.today:
			today = self.today
		else:
			today = datetime.datetime.today().date()

		# Ensure we're looking into the future
		if startDate < today:
			raise RuntimeError("Engine only supports calculating future dates.")

		# Record the dates the data is for
		data.startDate = startDate
		data.endDate = endDate

		# Calculate our daily balance
		currentBalance = sum([account.getTotalBalance() for account in self.accounts])

		for currentDate in daterange(today, data.endDate + datetime.timedelta(1)):
			# Apply our balance modifiers
			for modifier in self.balanceModifiers:
				if modifier.recurrence.isOnDate(currentDate):
					currentBalance += modifier.amount

			# Save the new balance for the current date
			if (currentDate >= startDate):
				data.balances[currentDate] = currentBalance

		return data
