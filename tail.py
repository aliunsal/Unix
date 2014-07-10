__author__ = 'aliunsal'
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", nargs="?")
parser.add_argument("-n", nargs="?", default="10")
parser.add_argument("-f", nargs="?")

args = parser.parse_args()

if not args.f:
    file = open(args.file_name, "r")
    lines = file.readlines()
    lines_count = len(lines) - 1
    for i in range(0, int(args.n)):
        print lines[lines_count - i]
    file.close()
else:
    file = open(args.f, "r")
    while 1:
        tell = file.tell()
        line = file.readline()
        if not line:
            file.seek(tell)
        else:
            print line
    file.close()