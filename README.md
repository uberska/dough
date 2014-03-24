# dough

## What Does It Do?

dough helps you get a handle on your personal finances.

## Config File

Create a json config file that represents your finances:

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
					"savings": 3856.50
				}
			}
		],
		"modifiers": [
			{
				"name": "Paycheck Every Two Weeks",
				"amount": 1000.0,
				"recurrence" : {
					"type": "daily",
					"start": "03/21/2014",
					"step": 14
				}
			},
			{
				"name": "Car Payment On The Tenth",
				"amount": -150.00,
				"recurrence" : {
					"type": "monthly",
					"day": 10
				}
			}
		]
	}

## Running dough

Pass the path to the config file to dough as an argument:

	./dough.py my-finances.json

dough uses argparse so run dough with -h to see a list of options that are configurable from the command line:

	./dough.py -h
