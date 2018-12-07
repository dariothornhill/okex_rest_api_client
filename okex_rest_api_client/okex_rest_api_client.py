# -*- coding: utf-8 -*-
import requests
import codecs
import hmac


class Okex_rest_v3():
    def __init__(self, **kwargs):
        try:
            self._OKEX_ACCESS_KEY = kwargs.api_key
            self._OKEX_SECRET = codecs.decode(kwargs.access_secret, "base64")
            self._OKEX_PASSPHRASE = kwargs.passphrase
        except Exception as identifier:
            print(identifier)

    def _headers(self, timestamp, signature):
        return {
            'OK-ACCESS-KEY': self._OKEX_ACCESS_KEY,
            'OK-ACCESS-SIGN': signature,
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-PASSPHRASE': self._OKEX_PASSPHRASE}

    def _credential(self, method, timestamp, path, message):
        # FIXME: Signature is bugged

        credential = timestamp + method.upper() + path + message
        return credential

    def _sign_request(self, credential):
        # FIXME: Signature is bugged

        sha = hmac.new("sha256", self._OKEX_SECRET)
        signature = sha.update(credential).hexdigest()
        return codecs.encode(signature, "base64")

    def get_spot_instruments(self):

        # TODO: Add error handling
        return requests.get(
            'http://www.okex.com/api/spot/v3/instruments').json()

    def get_spot_ticker(self):

        # TODO: Add error handling
        return requests.get(
            'https://www.okex.com/api/spot/v3/instruments/ticker').json()

    def get_spot_orders(self, pair):

        # TODO: Add error handling
        return requests.get(
            "https://www.okex.com/api/spot/v3/instruments/" +
            pair +
            "/books?size=200").json()

    def get_spot_trades(self, pair):

        # TODO: Add error handling
        return requests.get(
            "https://www.okex.com/api/spot/v3/instruments/" +
            pair +
            "/trades").json()


# TODO: create real tests and remove code below
"""
okex = Okex_rest_v3()

print("{}".format(okex.get_spot_instruments()))
print("{}".format(okex.get_spot_ticker()))
print("{}".format(okex.get_spot_orders("BTC-USD")))
print("{}".format(okex.get_spot_trades("BTC-USD")))
"""
