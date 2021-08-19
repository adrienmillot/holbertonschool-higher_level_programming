#!/usr/bin/python3
"""
    script that list 10 last commit for a repository
"""


import requests
import sys


if __name__ == "__main__":
    try:
        url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2],
            sys.argv[1]
        )
        response = requests.get(url=url)
        content = response.json()
        if (len(content) == 0):
            print("No result")
        else:
            for infos in content[0:10]:
                print(
                    "{}: {}".format(
                        infos.get('sha'),
                        infos.get('commit').get('author').get('name')
                    )
                )
    except requests.exceptions.HTTPError as exception:
        print("Error code: {}".format(exception.response.status_code))
