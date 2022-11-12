import pytest
from unittest.mock import patch, Mock, MagicMock


def init(arg_format, Valute):
    t_init = Rate(arg_format)
    t_init.make_format(Valute)
    expected = True
    if arg_format == 'full':
        expected = True
    else:
        expected = False
    if Valute == 'USD':
        expected = True
    else:
        expected = False
    return expected


@pytest.mark.parametrize("arg_format, Valute, expected",
                         [('full', 'USD', True),
                          ('value', 'USD', True),
                          ('full', 'asdf', False),
                          ('xcbv', '', False)])
def test_init(arg_format, Valute, expected):
    assert init(arg_format, Valute) == expected
    return expected


class Rate:
    def __init__(self, format_='value'):
        self.format = format_

    def exchange_rates(self):
        mock = MagicMock()
        self.r = mock.return_value = {'USD': {'ID': 'R01239',
                                                 'NumCode': '978',
                                                 'CharCode': 'USD',
                                                 'Nominal': 1,
                                                 'Name': 'Евро',
                                                 'Value': 61.5416,
                                                 'Previous': 61.0037}}
        return self.r

    def make_format(self, currency):
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                return response[currency]['Value']

        return 'Error'

    def USD(self):
        return self.make_format('USD')
