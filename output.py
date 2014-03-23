#!/usr/bin/python


import datetime

from date import DATE_FORMAT
from date import daterange


def outputData(data, outputPath):
	dates = list()
	balances = list()

	for currentDate in daterange(data.startDate, data.endDate + datetime.timedelta(1)):
		dates.append(currentDate.strftime(DATE_FORMAT))
		balances.append(str(data.balances[currentDate]))

	file = open(outputPath, "w")
	file.write(",".join(dates))
	file.write("\n")
	file.write(",".join(balances))
	file.write("\n")
	file.close()
