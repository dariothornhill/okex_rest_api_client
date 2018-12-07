#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `okex_rest_api_client` package."""

import unittest
from okex_rest_api_client import Okex_rest_v3

class ClientTests(unittest.TestCase):
    def test_sign(self):
        client = Okex_rest_v3(access_key='1', api_secret='aQ==', passphrase='a')
        credential = client._credential(method='get',timestamp='2018-12-07T03:54:40Z', path='/api', message="{'a': 'b'}")
        self.assertEqual(credential, "2018-12-07T03:54:40ZGET/api{'a': 'b'}")

if __name__ == "__main__":
    h = ClientTests()