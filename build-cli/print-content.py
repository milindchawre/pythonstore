from argparse import ArgumentParser
import sys

"""
Write a script that does the following:
    Receives a file_name and line_number as command line parameters.
    Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.

Make sure that you handle the following error cases by presenting the user with a useful message:
    The file doesn’t exist.
    The file doesn’t contain the line_number specified (file is too short).
"""

def create_parser():
    parser = ArgumentParser(description="Utility to print content of specific line number from a given file.")
    parser.add_argument('filename', help='File Name')
    parser.add_argument('--line', '-l', type=int, required=True, help='Line number in given file')
    return parser

def print_contents(filename, line):
    if line <= 0:
        print(f"Line can't be negative or zero.")
        sys.exit(1)
    lines = []
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)
    if line > len(lines):
        print(f"File is too short. Line {line} doesn't exists in the file. Line number should be between 1 to {len(lines)}.")
        sys.exit(1)
    return lines[line -1]
    print(f"Contents of line {line} in {filename}:\n{lines[line -1]}")

def main():
    parser = create_parser()
    args = parser.parse_args()
    line = print_contents(args.filename.strip(),args.line)
    print(f"Contents of line {args.line} in {args.filename.strip()}:\n{line}")

if __name__ == "__main__":
    main()
