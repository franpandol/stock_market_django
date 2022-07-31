import requests
from django.conf import settings


def request_data(symbol: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={settings.ALPHAVANTAGE_API_KEY}"
    result = requests.get(url)
    result_json = result.json()
    return result_json


def process_data(result_json: dict):
    # When the symbol is not found, the API returns 200 OK with an error message:
    if result_json.get("Error Message"):
        return {"error": result_json.get("Error Message")}

    # Example of successful result.json():
    # {
    # "Meta Data": {
    #     "1. Information": "Daily Prices (open, high, low, close) and Volumes",
    #     "2. Symbol": "IBM",
    #     "3. Last Refreshed": "2022-07-29",
    #     "4. Output Size": "Compact",
    #     "5. Time Zone": "US/Eastern"
    # },
    # "Time Series (Daily)": {
    #     "2022-07-29": {
    #         "1. open": "129.5200",
    #         "2. high": "131.0000",
    #         "3. low": "129.3100",
    #         "4. close": "130.7900",
    #         "5. volume": "5786815"
    #     },
    #     "2022-07-28": {
    #         "1. open": "128.7500",
    #         "2. high": "129.8100",
    #         "3. low": "128.6060",
    #         "4. close": "129.2200",
    #         "5. volume": "3913680"
    #     },...
    # }

    last_refreshed = result_json.get("Meta Data").get("3. Last Refreshed")
    time_series = result_json.get("Time Series (Daily)")
    last_value = time_series.get(last_refreshed)
    close_value = last_value.get("4. close")
    open_value = last_value.get("1. open")
    high_value = last_value.get("2. high")
    low_value = last_value.get("3. low")
    day_before_last = sorted(time_series.items())[-2][1]

    # Examples of the format of data.items():
    # >>> sorted(data.items())[-2]
    # ('2022-07-28', {'1. open': '128.7500', '2. high': '129.8100', '3. low': '128.6060', '4. close': '129.2200', '5. volume': '3913680'})

    # >>> sorted(data.items())[-2][1]
    # {'1. open': '128.7500', '2. high': '129.8100', '3. low': '128.6060', '4. close': '129.2200', '5. volume': '3913680'}
    day_before_last_close_value = day_before_last.get("4. close")
    variation_between_last_two_days = float(close_value) - float(
        day_before_last_close_value
    )

    return {
        "last_refreshed": last_refreshed,
        "close_value": close_value,
        "open_value": open_value,
        "high_value": high_value,
        "low_value": low_value,
        "variation_between_last_two_days": variation_between_last_two_days,
    }
