#!/usr/bin/python


import json


def loadConfigJson(jsonPath):
	jsonFile = open(jsonPath, "r")
	jsonConfig = json.load(jsonFile)
	jsonFile.close()
	return jsonConfig
