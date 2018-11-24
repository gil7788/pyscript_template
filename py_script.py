#!/bin/python

import argparse


class Parser:
    # Description: general parser template

    def __init__(self):
        # init parser
        self.parser = argparse.ArgumentParser()

    def abort(self, error, status):
        # Description: Abort function
        # Input: error, exit status
        # Output: terminate script

        print(error)
        self.parser.print_help()
        exit(status)

    def argument_parsing(self):
        # Description: Parse arguments
        # Input: None
        # Output: set self.parser.args

        # self.parser.add_argument("-h", "--hash", help="Hash to crack")
        args = self.parser.parse_args()

        # Mandatory params:
        #if args.hash is None:
        #    self.abort("Invalid params. -h/--hash option is mandatory", 1)


if __name__ == '__main__':
    p = Parser()
    p.argument_parsing()
