import unittest


import requests


def get_weather(city):
    url = f'http://api.weather.com/current?city={city}'
    response = requests.get(url)
    data = response.json()
    temperature = data['temperature']
    return temperature


# mocking test
from unittest.mock import patch         # patch replace function requests.get(url)


def test_get_weather():
    mock_response = {
        'temperature': 25.0
    }

    with patch('requests.get') as mock_get:                     # patch replace function requests.get(url)
        mock_get.return_value.json.return_value = mock_response

        temperature = get_weather('mock_city')

        assert_temperature = 25.0


if __name__ == '__main__':
    unittest.main()
