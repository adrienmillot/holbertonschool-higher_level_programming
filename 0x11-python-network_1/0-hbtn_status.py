#!/usr/bin/python3
"""
    script that fetches https://intranet.hbtn.io/status
"""


from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        charsetStatus = content.decode("utf-8")

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(charsetStatus))
