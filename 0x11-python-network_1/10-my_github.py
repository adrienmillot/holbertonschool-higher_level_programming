#!/usr/bin/python3
"""
    script that get information about user from github api
"""


import requests
import sys


def is_valid_json(data) -> bool:
    """
        check if a data is a json
    """
    try:
        data.json()
        return True
    except Exception:
        return False


if __name__ == "__main__":
    try:
        url = "https://api.github.com/user"
        response = requests.get(url=url, auth=(sys.argv[1], sys.argv[2]))
        if not is_valid_json(response):
            print("Not a valid JSON")
        else:
            content = response.json()
            if (len(content) == 0):
                print("No result")
            else:
                print("{}".format(content.get("id")))
    except requests.exceptions.HTTPError as exception:
        print("Error code: {}".format(exception.response.status_code))
