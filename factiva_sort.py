#!/usr/bin/env python
# encoding utf-8
"""
factiva_sort.py

Sorts a plaintext Factiva file into individual articles with corresponding
metadata.

sample usage:
$ python factiva_sort.py *.txt
File name? Do not include '.csv'. All data will be written to one file.
output
Data written to output.csv.
"""
import fileinput
import re
import csv

__author__ = "Jason L. Zhang"

__maintainer__ = "Jason L. Zhang"
__email__ = "jason.zhang@berkeley.edu"
__status__ = "Prototype"

##################
# Input Specific #
##################

categories = ["SE", "HD", "BY", "CR", "WC", "PD", "SN", "SC", "PG", 
             "LA", "CY", "LP", "TD", "RF", "CO", "RE", "PUB", "AN"]
article_template = {k : "" for k in category_titles}
format_body = False
format_spacer = "\n" if format_body else " "


#Do not modify.
category_titles = ["SE", "HD", "BY", "CR", "WC", "PD", "SN", "SC", "PG",   
                  "LA", "CY", "LP", "TD", "RF", "CO", "RE", "PUB", "AN"]

#############
# Functions #
#############
def csv_setup():
    """Sets up a new csv file with user input for the name, returns a writer
    for the new file."""
    file_name = str(raw_input(
    "File name? Do not include '.csv', leave blank for default " + \
    "'output.csv'.  All data will be written to one file. \n"))
    if file_name == '':
        file_name = 'output'
    file_name = file_name + ".csv"
    output = open(file_name, 'wb')
    writer = csv.writer(output)
    writer.writerow(categories)
    return writer, file_name

def process_line(line, writer, header):
    """Reads the LINE using WRITER and determines if it is data or a 
    signature. Returns a two element list with the old or new HEADER category 
    and line."""
    pattern = re.compile("[A-Z]{2,3}\Z")
    line = line.strip()
    tokens = line.split(" ", 1)
    match = re.match(pattern, tokens[0])
    if match and match.group(0) in categories:
        if len(tokens) > 1:
            return match.group(0), tokens[1].strip()
        elif len(tokens) == 1:
            return match.group(0), ""
    else:
        return header, line
        
def write_data(article_dict, writer):
    """Writes the collected data to the csv file on a new row. Loops through
    the dictionary and list CATEGORIES to concatenate strings and write the 
    categories in order."""
    output = []
    for section in categories:
        output.append(article_dict[section])
    writer.writerow(output)    

###############
# Main thread #
###############
def main():
    """Reads each line of standard input and assigns it to a dictionary of
    category values to strings, concatenating each new line to the old string
    under the matching category if there is not a change in category. When a
    change in article is detected, data is written to the CSV file and article
    is reset."""
    writer, file_name = csv_setup()
    article = article_template.copy()
    sorted_line = (None, None)
    grouped_lines = ""
    header = categories[0]
    for line in fileinput.input():
        sorted_line = process_line(line, writer, header)
        if sorted_line[0] != header:
            article[header] = grouped_lines
            if categories.index(header) > categories.index(sorted_line[0]):
                write_data(article, writer)
                article = article_template.copy()
            header = sorted_line[0]
            grouped_lines = ""
        if sorted_line[1]:
            grouped_lines += sorted_line[1] + format_spacer
    write_data(article, writer)
    print("Written to " + file_name + ".")         

if __name__ == '__main__':
    main()
