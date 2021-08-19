#!/usr/bin/python3
"""
    script that takes in a URL, sends a request to the URL handling error
"""


import requests
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        response = requests.get(url=sys.argv[1])
        response.raise_for_status()
        content = response.content
        print("{}".format(content.decode("utf-8")))
    except requests.exceptions.HTTPError as exception:
        print("Error code: {}".format(exception.response.status_code))
