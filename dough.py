#!/usr/bin/python


import argparse
import datetime

from account import loadAccounts
from balance_modifier import loadBalanceModifiers
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

	parser.add_argument(
		'-d',
		'--days',
		nargs=1,
		type=int,
		default=[365],
		help='Number of days to calculate ahead of today.')

	args = parser.parse_args()

	configJson = loadConfigJson(args.config[0])

	accounts = loadAccounts(configJson)

	balanceModifiers = loadBalanceModifiers(configJson)

	engine = Engine(accounts, balanceModifiers)

	startDate = datetime.date.today()
	endDate = startDate + datetime.timedelta(days=args.days[0])

	data = engine.execute(startDate, endDate)

	outputData(data, args.output[0])


if __name__ == "__main__":
	main()
