#!/usr/bin/python


from recurrence import loadRecurrenceFromJsonObj


def loadBalanceModifiers(configJson):
	return [loadBalanceModifierFromJsonObj(incomeJson) for incomeJson in configJson["modifiers"]]


def loadBalanceModifierFromJsonObj(jsonObj):
	return BalanceModifier(
		jsonObj["name"],
		jsonObj["amount"],
		loadRecurrenceFromJsonObj(jsonObj["recurrence"]))


class BalanceModifier(object):
	def __init__(self, name, amount, recurrence):
		self.name = name

		self.amount = amount

		self.recurrence = recurrence
