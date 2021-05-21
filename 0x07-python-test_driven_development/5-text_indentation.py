#!/usr/bin/python3
""" text_indentation module """


def text_indentation(prmText):
    """ text_indentation function

    this function split a text by punctuation

    Attributes:
        prmText: text to split
    """
    if not isinstance(prmText, str):
        raise TypeError("text must be a string")

    prmText = prmText.replace(". ", ".\n")
    prmText = prmText.replace("? ", "?\n")
    prmText = prmText.replace(": ", ":\n")

    for key, line in enumerate(list(prmText.split("\n"))):
        print("{}".format(line))
        if key < len(list(prmText.split("\n"))) - 1:
            print()
