import pytest
from ..src.main_0 import get_weather


def test_get_weather(mocker):
    # Mock requests.get
    mock_get = mocker.patch("mocks.src.main_0.requests.get")

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "contiditon": "Sunny"}

    # Call function
    result = get_weather("Dubai")

    # Assertion
    assert result == {"temperature": 25, "contiditon": "Sunny"}
    mock_get.assert_called_once_with("http://api.weather.com/v1/Dubai")
