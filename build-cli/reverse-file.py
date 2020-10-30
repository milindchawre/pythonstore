#!/usr/bin/env python3.9

"""
Building a CLI to Reverse Files

The tool need to do the following:

    Require a filename argument, so it knows what file to read.
    Print the contents of the file backward (bottom of the script first, each line printed backward)
    Provide help text and documentation when it receives the --help flag.
    Accept an optional --limit or -l flag to specify how many lines to read from the file.
    Accept a --version flag to print out the current version of the tool.

"""

import argparse
import sys

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit','-l', type=int, help='the number of lines to read')
parser.add_argument('--version','-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
#print(args)

try:
    f = open(args.filename, 'r')
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
#except:
#    print(f"Some err")
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
#finally:
#    print("finally")
