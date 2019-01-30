import os
import json
import datetime
from shutil import copyfile

MAIN_DIR = os.path.expanduser("~/.new_file_manager/")
HEADER_DIR = MAIN_DIR + "headers/"
TEMPLATE_DIR = MAIN_DIR + "templates/"


def get_comment_char(filetype):
    """
    Returns a tuple containing (comment_header, comment_char, comment_footer)
    comment header and footer are for languages like C where multi line comments are different
    :param filetype: The extension of the file to get the comment char for
    :return: a tuple containing (comment_header, comment_char, comment_footer)
    """

    if filetype == ".c" or filetype == ".cpp" or filetype == ".h":
        return "/*\n", "*", "*/\n"

    elif filetype == ".py":
        return "\"\"\"\n", "", "\"\"\"\n"

    elif filetype == ".rs":
        return "", "//", ""

    elif filetype == ".tex" or filetype == ".cls":
        return "", "%", ""

    elif filetype == ".sh" or filetype == ".bash":
        return "#!/bin/bash", "#", ""

    else:
        return "", "", ""


def get_header_string(header, comment_char):
    """
    Parses a header and creates a string representation of it
    :param header: A dictionary representing the header to write
    :param comment_char: A tuple containing (comment_header, comment_char, comment_footer)
    :return: A string representation of the header
    """
    out_string = comment_char[0]
    description = ""
    date = ""

    for key, value in header.items():

        if key == "description":
            out_string += comment_char[1] + " description: " + input("Enter a description for the file: \n") + "\n"

        elif key == "date":
            out_string += comment_char[1] + " date: " + datetime.datetime.today().strftime('%Y-%m-%d') + "\n"

        else:
            out_string += comment_char[1] + " " + key + ": " + value + "\n"

    out_string += comment_char[2] + "\n"


    return out_string


def load_header(header_name):
    """
    Load the header from the header dir named header_name.json
    :param header_name: The nane of the header to load
    :return: A dictionary representing the header
    """

    with open(os.path.join(HEADER_DIR, header_name + ".json"), 'r') as fp:
        header = json.load(fp)

    return header


def list_headers():
    """
    List all headers in the header dir
    :return: None
    """

    for file in os.listdir(HEADER_DIR):
        print(os.path.splitext(file)[0])


def set_up():
    """
    Creates the required directories and files
    :return: None
    """
    if not os.path.exists(MAIN_DIR):
        os.mkdir(MAIN_DIR)
        os.mkdir(HEADER_DIR)
        os.mkdir(TEMPLATE_DIR)

        default_header = {"author" : "Name",
                          "date" : "Date",
                          "description" : "Description"}

        with open(HEADER_DIR + "default.json", 'w') as fp:
            json.dump(default_header, fp)


def list_templates():
    """
    List all templates in the template dir
    :return: None
    """
    for file in os.listdir(TEMPLATE_DIR):
        print(os.path.splitext(file)[0])


def write_new_file(header_string, file_path, template_name=None):
    """
    Write the new file, and put the header and template in it
    :param header_string: The string to write to the header
    :param file_path: The path to the new file
    :param template_name: The name of the template to use, if any
    :return: None
    """

    if template_name is not None:
        copyfile(os.path.join(TEMPLATE_DIR, template_name), file_path)

        with open(file_path, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(header_string.rstrip('\r\n') + '\n\n' + content)
    else:
        with open(file_path, 'w') as f:
            f.write(header_string + "\n\n")

