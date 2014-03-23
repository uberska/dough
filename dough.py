#!/usr/bin/python


import argparse


def main():
	parser = argparse.ArgumentParser(description='Get a handle on your personal finances.')

	parser.add_argument(
		'config',
		nargs=1,
		help='A config file specifying your finances.')

	args = parser.parse_args()

	print(args)


if __name__ == "__main__":
	main()
