__author__ = 'aliunsal'
from  sys import  argv
from optparse import OptionParser

print(argv)

script, read_type, line_number, file_name = argv

file = open(file_name, 'r')
lines = file.readlines()
line_count = len(lines) - 1
file.close()
x = 0
for i in range(0, int(line_number)):
    print lines[line_count - i]
