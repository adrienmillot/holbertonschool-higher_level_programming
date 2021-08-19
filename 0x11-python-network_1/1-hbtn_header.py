#!/usr/bin/python3
"""
    displays the value of the X-Request-Id variable found
    in the header of the response.
"""


from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
