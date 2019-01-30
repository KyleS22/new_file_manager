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
    parser.add_argument("--remember", action="store_true", help="Remember the header to use for this directory and its children")
    parser.add_argument("--forget", action="store_true", help="Forget the header used for this directory and its children")
    
    

    args = parser.parse_args()

    nfm.set_up()

    if len(sys.argv) < 2:
        parser.print_help()

    if args.list_headers:
        nfm.list_headers()
        sys.exit(0)


    if args.list_templates:
        nfm.list_templates()
        sys.exit(0)

    if args.forget:
        nfm.forget_header(os.getcwd())

    if args.file_name is None:
        sys.exit(0)

    header_string = ""
    file_path, filetype = os.path.splitext(args.file_name)

    if args.header:
        header = nfm.load_header(args.header)
        comment_char = nfm.get_comment_char(filetype)
        header_string = nfm.get_header_string(header, comment_char)
    else:
        header_name = nfm.get_remembered_header(os.getcwd())
        if header_name is not None and header_name != "none":
            header = nfm.load_header(header_name)
            comment_char = nfm.get_comment_char(filetype)
            header_string = nfm.get_header_string(header, comment_char)

    if args.remember:
        nfm.remember_header(args.header, os.getcwd())
    
    

    if args.template:
        nfm.write_new_file(header_string, file_path + filetype, template_name=args.template)
    else:
        nfm.write_new_file(header_string, file_path + filetype)



if __name__ == "__main__":

    main()
