#!/usr/bin/python


import argparse

from account import loadAccountsFromConfigJson
from config import loadConfigJson


def main():
	parser = argparse.ArgumentParser(description='Get a handle on your personal finances.')

	parser.add_argument(
		'config',
		nargs=1,
		help='A config file specifying your finances.')

	args = parser.parse_args()

	configJson = loadConfigJson(args.config[0])

	accounts = loadAccountsFromConfigJson(configJson)

	totalBalance = sum([account.getTotalBalance() for account in accounts])

	print("")
	print("Total Balance:")
	print(totalBalance)
	print("")


if __name__ == "__main__":
	main()
