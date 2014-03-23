#!/usr/bin/python


import datetime

from data import Data
from date import daterange


class Engine(object):
	def __init__(self, accounts):
		self.accounts = accounts

	def execute(self, startDate, endDate):
		data = Data()

		data.startDate = startDate
		data.endDate = endDate

		for currentDate in daterange(data.startDate, data.endDate + datetime.timedelta(1)):
			data.balances[currentDate] = 0.0

		return data
