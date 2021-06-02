#!/usr/bin/python3
""" read_file module """


def read_file(prmFileName=""):
    """
        function that read specific file

        Args:
            prmFileName: name of the file
    """
    with open(prmFileName, encoding="UTF-8") as file:
        read_data = file.read()
        print(read_data, end="")
    file.closed
