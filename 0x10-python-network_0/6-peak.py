#!/usr/bin/python3
""" script to find a peak """


def find_peak(list_of_integers):
    """
        function that find the first peak
    """
    if None is list_of_integers or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    for i in range(len(list_of_integers)):
        if (
            i < len(list_of_integers) - 1
            and list_of_integers[i] > list_of_integers[i + 1]
            and (
                list_of_integers[i - 1] is None
                or list_of_integers[i - 1] < list_of_integers[i]
            )
        ):
            return list_of_integers[i]

    return list_of_integers[i]
