#!/usr/bin/python


import json
import unittest

from account import *


class TestAccounts(unittest.TestCase):
	def setUp(self):
		configJson = """
		{
			"accounts": [
				{
					"name": "Account1",
					"balances": {
						"savings": 100.0,
						"checking": 253.0
					}
				},
				{
					"name": "Account2",
					"balances": {
						"savings": 3856.50,
						"checking": 2965.87
					}
				}
			]
		}
		"""
		self.accounts = loadAccounts(json.loads(configJson))

	def test_total_balance(self):
		self.assertEqual(self.accounts[0].getTotalBalance(), 353.0)
		self.assertEqual(self.accounts[1].getTotalBalance(), 6822.37)


if __name__ == '__main__':
	unittest.main()
