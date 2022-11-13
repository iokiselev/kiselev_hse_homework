import pytest

from rate import Rate


class TestRate:
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = '{"Valute":{"EUR":{"Value":60,"Previous":59}}}'

    def test_value(self, requests_mock):
        requests_mock.get(self.url, text=self.response)

        rate = Rate()

        assert rate.eur() == 60

    def test_diff(self, requests_mock):
        requests_mock.get(self.url, text=self.response)

        rate = Rate(diff=True)

        assert rate.eur() == 1

    def test_full(self, requests_mock):
        requests_mock.get(self.url, text=self.response)

        rate = Rate(format_='full')

        assert rate.eur() == {'Previous': 59, 'Value': 60}

    @pytest.mark.parametrize('response,expected', [('{"Valute":{"EUR":{"Value":60,"Previous":59}}}', 60)])
    def test_parametrize(self, requests_mock, response, expected):
        requests_mock.get(self.url, text=response)

        rate = Rate()

        assert rate.eur() == expected
