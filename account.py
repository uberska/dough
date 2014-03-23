#!/usr/bin/python


def loadAccountsFromConfigJson(configJson):
	return [Account(accountJson) for accountJson in configJson["accounts"]]


class Account(object):
	def __init__(self, accountJson):
		self.name = accountJson["name"]
		self.balances = accountJson["balances"]

	def getTotalBalance(self):
		return sum([balance for balance in self.balances.values()])
