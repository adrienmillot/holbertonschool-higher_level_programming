#!/usr/bin/python3
"""
    displays the value of the X-Request-Id variable found
    in the header of the response.
"""


import requests
import sys


if __name__ == "__main__":
    response = requests.get(url=sys.argv[1])
    print(response.headers.get("X-Request-Id"))
