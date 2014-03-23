# dough

## What Does It Do?

Get a handle on your personal finances.

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
		]
	}

## Running dough

Pass the path to the config file to dough as an argument:

./dough.py my-finances.json
