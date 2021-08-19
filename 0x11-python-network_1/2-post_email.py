#!/usr/bin/python3
"""
    script that sends a POST request to the passed URL
    with the email as a parameter,
"""


from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    with request.urlopen(url, data) as response:
        content = response.read()
        print("{}".format(content.decode("utf-8")))
