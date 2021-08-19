#!/usr/bin/python3
"""
    script that sends a POST request to the passed URL
    with the email as a parameter,
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    response = requests.post(url=sys.argv[1], data=values)
    content = response.content
    print("{}".format(content.decode("utf-8")))
