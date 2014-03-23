#!/usr/bin/python


import argparse
import datetime

from account import loadAccountsFromConfigJson
from config import loadConfigJson
from data import Data
from engine import Engine
from output import outputData


def main():
	parser = argparse.ArgumentParser(description='Get a handle on your personal finances.')

	parser.add_argument(
		'config',
		nargs=1,
		help='A config file specifying your finances.')

	parser.add_argument(
		'-o',
		'--output',
		nargs=1,
		default=["finances.csv"],
		help='Output file to write to.')

	args = parser.parse_args()

	configJson = loadConfigJson(args.config[0])

	accounts = loadAccountsFromConfigJson(configJson)

	engine = Engine(accounts)

	startDate = datetime.date.today()
	endDate = startDate + datetime.timedelta(days=100)

	data = engine.execute(startDate, endDate)

	outputData(data, args.output[0])


if __name__ == "__main__":
	main()
