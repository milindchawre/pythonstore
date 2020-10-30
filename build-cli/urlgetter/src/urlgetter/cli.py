from argparse import ArgumentParser
import requests
import json
import sys

def create_parser():
    parser = ArgumentParser(description="CLI to downloads contents from a url to a given destination file")
    parser.add_argument("url", help="URL")
    parser.add_argument("--filename", "-f", required=True, help="destination file")
    parser.add_argument("--res", type=str.upper, choices=['HTML','JSON'], default="HTML", help="Response Type: {HTML/JSON}, Default: HTML")
    return parser

# get get contents
def get_contents(url, res):
    """
    Download contents from url
    """
    result = requests.get(url)
    if result.status_code >= 400:
        print(f"Error code received: {result.status_code}")
        sys.exit(1)
    if res == "HTML":
        return result.text
    else:
        try:
            content = json.dumps(result.json())
        except ValueError:
            print("Error: Content is not JSON")
            sys.exit(1)
        return result.json()

# write contents
def write_contents(content, filename, res):
    """
    Write contents downloaded from url to a destination file
    """
    with open(filename, 'w') as f:
        if res == "HTML":
            f.write(content)
        else:
            json.dump(content, f)

def main():
    """
    main function call for urlgetter
    """
    parser = create_parser()
    args = parser.parse_args()
    content = get_contents(args.url, args.res)
    write_contents(content, args.filename, args.res)

