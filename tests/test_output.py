#!/usr/bin/python


import datetime
import unittest

from data import Data
from output import outputData


class TestOutput(unittest.TestCase):
	OUTPUT_PATH = "/tmp/dough_test_output.csv"

	def setUp(self):
		self.data = Data()

		self.data.startDate = datetime.date(2014, 3, 23)
		self.data.endDate = datetime.date(2014, 3, 25)

		self.data.balances = {
			datetime.date(2014, 3, 23): 100.0,
			datetime.date(2014, 3, 24): 230.0,
			datetime.date(2014, 3, 25): 60.0
		}

	def test_output_csv(self):
		outputData(self.data, self.OUTPUT_PATH)

		file = open(self.OUTPUT_PATH, "r")
		lines = file.readlines()
		file.close()

		goalLines = [
			"03/23/2014,03/24/2014,03/25/2014\n",
			"100.0,230.0,60.0\n"
		]

		self.assertEqual(lines, goalLines)


if __name__ == '__main__':
	unittest.main()
