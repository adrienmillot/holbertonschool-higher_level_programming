#!/usr/bin/python3
for c in reversed(range(ord('a'), ord('z') + 1)):
    if c % 2 != 0:
        print("{:c}".format(c - 32), end='')
    else:
        print("{:c}".format(c), end='')
