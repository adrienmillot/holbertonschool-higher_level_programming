#!/usr/bin/python3
"""
    script that takes in a letter and sends a POST request with parameter
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
        url = "http://0.0.0.0:5000/search_user"
        letter = "" if len(sys.argv) == 1 else sys.argv[1]
        values = {'q': letter}
        response = requests.post(url=url, data=values)
        if not is_valid_json(response):
            print("Not a valid JSON")
        else:
            content = response.json()
            if (len(content) == 0):
                print("No result")
            else:
                print("[{}] {}".format(content['id'], content['name']))
    except requests.exceptions.HTTPError as exception:
        print("Error code: {}".format(exception.response.status_code))
