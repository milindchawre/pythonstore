from argparse import ArgumentParser
import sys
import subprocess
import os


def create_parser():
    parser = ArgumentParser(description="CLI utility for killing processes listening of specific port")
    parser.add_argument("port_number", type=int, help="port number")
    return parser


def is_valid_port(port):
    """
    Check whether port number is valid (not < 0)
    """
    if port < 0:
        print("Port can't be negative number.")
        sys.exit(1)


def main():
    parser = create_parser()
    args = parser.parse_args()
    is_valid_port(args.port_number)
    s = subprocess.run(
        ["lsof", "-n", "-i4TCP:" + str(args.port_number)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    # lsof -n -i4TCP:port_number
    if s.stdout.decode() != b"":
        process_out = s.stdout.decode().split("\n")
        process_out.pop(0)
        flag = 0
        for i in range(0, len(process_out)-1):
            if process_out[i].split()[-1] == "(LISTEN)":
                os.kill(int(process_out[i].split()[1]), 9)
                print(f"Killed process {process_out[i].split()[0]} with pid {process_out[i].split()[1]}.")
                flag = 1
        if flag == 0:
            print(f"There is no any process listening on port {args.port_number}.")
    else:
        print(f"There is no any process running on port {args.port_number}.")
