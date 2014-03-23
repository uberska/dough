#!/usr/bin/python


import datetime
import unittest

from balance_modifier import BalanceModifier
from engine import Engine
from recurrence import DailyRecurrence


class TestEngine(unittest.TestCase):
	def setUp(self):
		accounts = list()

		today = datetime.date(2014, 3, 1)

		allowanceStartDate = datetime.date(2014, 3, 1)

		everyOtherDayRecurrence = DailyRecurrence(allowanceStartDate, 2, 5)

		balanceModifiers = [BalanceModifier("100 Dollar Allowance", 100.0, everyOtherDayRecurrence)]

		self.engine = Engine(accounts, balanceModifiers, today)

	def test_engine(self):
		startDate = datetime.date(2014, 3, 3)
		endDate = datetime.date(2014, 3, 13)

		data = self.engine.execute(startDate, endDate)

		self.assertEqual(data.startDate, startDate)
		self.assertEqual(data.endDate, endDate)

		self.assertEqual(data.balances[datetime.date(2014, 3, 3)], 200.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 4)], 200.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 5)], 300.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 6)], 300.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 7)], 400.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 8)], 400.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 9)], 500.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 10)], 500.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 11)], 500.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 12)], 500.0)
		self.assertEqual(data.balances[datetime.date(2014, 3, 13)], 500.0)


if __name__ == '__main__':
	unittest.main()
