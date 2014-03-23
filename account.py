#!/usr/bin/python


def loadAccounts(configJson):
	return [loadAccountFromJsonObj(accountJson) for accountJson in configJson["accounts"]]


def loadAccountFromJsonObj(jsonObj):
	return Account(jsonObj["name"], jsonObj["balances"])


class Account(object):
	def __init__(self, name, balances):
		self.name = name
		self.balances = balances

	def getTotalBalance(self):
		return sum([balance for balance in self.balances.values()])
