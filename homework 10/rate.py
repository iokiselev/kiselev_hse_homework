import requests

class Rate:
	def __init__(self, diff=False, format_='value'):
		self.format = format_
		self.diff = diff

	def exchange_rates(self):
		self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
		return self.r.json()['Valute']

	def make_format(self, currency):
		response = self.exchange_rates()

		if currency in response:
			if self.format == 'full':
				return response[currency]

		if self.format == 'value':
			if self.diff:
				return response[currency]['Value'] - response[currency]['Previous']
			else:
				return response[currency]['Value']

	def eur(self):
		return self.make_format('EUR')

	def usd(self):
		return self.make_format('USD')

	def brl(self):
		return self.make_format('BRL')