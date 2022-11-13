import pytest
from rate import Rate


class TestRate:
    url = 'https://www.cbr-xml-daily.ru/daily_json.js';
    response = '{"Valute":{"EUR":{"Value":60,"Previous":59}}}';

    @pytest.mark.parametrize('diff,format,expected', [
        (False, 'value', 60),
        (False, 'full', {'Previous': 59, 'Value': 60}),
        (True, 'value', 1),
        (True, 'full', {'Previous': 59, 'Value': 60})])
    def test_rate(self, requests_mock, diff, format, expected):
        requests_mock.get(self.url, text=self.response)

        rate = Rate(diff=diff, format_=format)

        assert rate.eur() == expected

