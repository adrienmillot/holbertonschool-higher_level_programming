#!/usr/bin/python3
""" script that count request by web request status """


import sys


if __name__ == "__main__":
    file_size = [0]
    status_count = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    def increment(prmString):
        """ increment request number """
        try:
            data = prmString.split()
            errorCode = int(data[-2])
            file_size[0] += int(data[-1])
            if check(errorCode) is True:
                status_count[errorCode] += 1

        except:
            pass

    def check(prmErrorCode):
        """ check error code validity """
        if prmErrorCode in status_count:
            return True
        return False

    def print_stats():
        """ print statistics """
        print("File size: {:d}".format(file_size[0]))
        for errorCode, count in sorted(status_count.items()):
            if status_count[errorCode]:
                print("{:d}: {:d}".format(errorCode, count))

    try:
        for index, line in enumerate(sys.stdin):
            increment(line)
            if index % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
