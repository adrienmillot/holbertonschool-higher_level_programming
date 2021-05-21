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

    prmText = prmText.strip()
    prmText = prmText.replace(".", ".\n")
    prmText = prmText.replace("?", "?\n")
    prmText = prmText.replace(":", ":\n")
    prmText = prmText.rstrip()

    if len(prmText) == 0:
        return

    for key, line in enumerate(list(prmText.split("\n"))):
        line = line.strip()
        print("{}".format(line))
        if key < len(list(prmText.split("\n"))) - 1:
            print()
