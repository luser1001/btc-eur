#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    pip install pycoingecko
    Powered by CoinGecko API
"""

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def main():
    print(cg.ping())
    print(cg.get_price(ids='bitcoin', vs_currencies='eur'))

if __name__ == "__main__":
    main()
