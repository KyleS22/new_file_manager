import argparse
import sys
import os

import new_file_manager.new_file_manager as nfm
from new_file_manager.new_file_manager import MAIN_DIR


def main():
    parser = argparse.ArgumentParser(description="Create a new file with a header and templates")

    parser.add_argument("file_name", nargs='?', default=None, help="The name of the new file including extension")
    parser.add_argument("--header", help="The name of the header to use")
    parser.add_argument("--list_headers", action="store_true", help="List header names")
    parser.add_argument("--template", help="The name of a template to use")
    parser.add_argument("--list_templates", action="store_true", help="List the possible template names")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()

    if args.list_headers:
        nfm.list_headers()
        sys.exit(0)


    if args.list_templates:
        nfm.list_templates()
        sys.exit(0)


    if args.file_name is None:
        sys.exit(0)

    header_string = ""
    file_path, filetype = os.path.splitext(args.file_name)

    if args.header:
        header = nfm.load_header(args.header)
        comment_char = nfm.get_comment_char(filetype)
        header_string = nfm.get_header_string(header, comment_char)



    nfm.set_up()

    if args.template:
        nfm.write_new_file(header_string, file_path + filetype, template_name=args.template)
    else:
        nfm.write_new_file(header_string, file_path + filetype)



if __name__ == "__main__":

    main()
