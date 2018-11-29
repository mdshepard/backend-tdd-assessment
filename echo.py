#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text."
        )
    parser.add_argument(
        "text", help="text to be manipulated"
        )
    parser.add_argument(
        "-u", "--upper", help="convert text to uppercase", action="store_true"
        )
    parser.add_argument(
        "-l", "--lower", help="convert text to lowercase", action="store_true"
        )
    parser.add_argument(
        "-t", "--title", help="convert text to titlecase", action="store_true"
        )
    return parser


def main(args):
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit()

    args = parser.parse_args(args)
    text = args.text

    if args.upper:
        text = text.upper()

    if args.lower:
        text = text.lower()

    if args.title:
        text = text.title()

    return text


if __name__ == "__main__":
    res = main(sys.argv[1:])
    print res
