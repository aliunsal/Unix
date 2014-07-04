__author__ = 'aliunsal'
from sys import argv
script, read_type, line_number, file_name = argv
file = open(file_name, 'r')
lines = file.readlines()
file.close()
for i in range(0, int(line_number)):
    print lines[i]