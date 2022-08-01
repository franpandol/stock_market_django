from unittest import TestCase

from api.services import request_data, process_data


class ServicesTestCase(TestCase):
    def setUp(self):
        self.response = {
            "Meta Data": {
                "1. Information": "Daily Prices (open, high, low, close) and Volumes",
                "2. Symbol": "IBM",
                "3. Last Refreshed": "2022-07-29",
                "4. Output Size": "Compact",
                "5. Time Zone": "US/Eastern",
            },
            "Time Series (Daily)": {
                "2022-07-29": {
                    "1. open": "129.5200",
                    "2. high": "131.0000",
                    "3. low": "129.3100",
                    "4. close": "130.7900",
                    "5. volume": "5786815",
                },
                "2022-07-28": {
                    "1. open": "128.7500",
                    "2. high": "129.8100",
                    "3. low": "128.6060",
                    "4. close": "129.2200",
                    "5. volume": "3913680",
                },
                "2022-07-27": {
                    "1. open": "127.9700",
                    "2. high": "129.4300",
                    "3. low": "127.5800",
                    "4. close": "129.1200",
                    "5. volume": "4175625",
                },
                "2022-07-26": {
                    "1. open": "128.2600",
                    "2. high": "129.3000",
                    "3. low": "127.6300",
                    "4. close": "128.0800",
                    "5. volume": "3645313",
                },
            },
        }

    def test_request_and_process_data(self):
        result = process_data(self.response)
        self.assertEqual(result.get("last_refreshed"), "2022-07-29")
        self.assertEqual(result.get("close_value"), "130.7900")
        self.assertEqual(result.get("open_value"), "129.5200")
        self.assertEqual(result.get("high_value"), "131.0000")
        self.assertEqual(result.get("low_value"), "129.3100")
        self.assertEqual(
            result.get("variation_between_last_two_days"), "1.5700"
        )
