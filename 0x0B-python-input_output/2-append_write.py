#!/usr/bin/python3
""" append_write module """


def append_write(prmFileName="", prmText=""):
    """
        function that add specific text to a specific file

        Args:
            prmFileName: name of the file
            prmText: text to add
    """
    nbCharacter = 0
    with open(prmFileName, 'a', encoding="UTF-8") as file:
        nbCharacter = file.write(prmText)
    file.closed
    return nbCharacter
