"""
factiva_sort.py

@author Jason L. Zhang
jason.zhang@berkeley.edu

Sorts a plaintext Factiva file into individual articles with corresponding
metadata.

sample usage
"""
#####################
# Customizable data #
#####################




#####################
# Necessary modules #
#####################
import fileinput
import re
import csv

#############
# Functions #
#############
def process_line(line):
    """ Reads the line and determines if it is data or a signature. """
    writer.writerow(line)


###################
# Local variables #
###################
file_name = None
writer = None



###############
# Main thread #
###############

file_name = str(raw_input(
"File name? Do not include '.csv'. All data will be written to one file. \n"))
file_name = file_name + ".csv"
output = open(file_name, 'wb')
writer = csv.writer(output)

for line in fileinput.input():
    process_line(line)
    print(line)






