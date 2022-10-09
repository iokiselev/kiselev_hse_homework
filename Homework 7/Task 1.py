import requests


class Rate:
    def __init__(self, format_='value'):
        self.format = format_

    def exchange_rates(self):
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']

    def make_format(self, currency):
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

        if self.format == 'value':
            return response[currency]['Value']

        return ['Error']

    def eur(self):
        return self.make_format('EUR')

    def usd(self):
        return self.make_format('USD')

    def brl(self):
        return self.make_format('BRL')


class CurrencyNames(Rate):
    def __init__(self):
        super().__init__(format_='full')

    def currency_id(self, currency):
        return self.make_format(currency)['Name']

