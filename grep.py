import argparse

parser = argparse.ArgumentParser()
parser.add_argument("string", nargs='?')
parser.add_argument("file", nargs='?')

args = parser.parse_args()

file = open(args.file, "r")

for line in file:
    if args.string in line.split():
        print line

print args.string