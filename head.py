__author__ = 'aliunsal'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_name", nargs="?")
parser.add_argument("-n", nargs="?", default="10")

args = parser.parse_args()
#print parser.parse_args()

file = open(args.file_name, "r")
lines = file.readlines()
for i in range(0, int(args.n)):
    print lines[i]
file.close()
