#!/usr/bin/env python3
import sys

"""
This is a mapper that reads json files of a specific schema ( https://aminer.org/citation V10).
Its purpose is to keep track of the authors and their position on each published paper.
"""

if __name__ == "__main__":
    # input comes from the STDIN (standard input).
    # Read each line as a string.
    for line in sys.stdin:
        # Keep tracks of the index that author list starts in each line.
        start_index = line.find('"authors": [')
        # From each line it saves everything after the start index, where our useful data are.
        temp_string = line[start_index + 12:]
        # From what it saves it sets an end index to where the author list ends according to json schema.
        end_index = temp_string.find("]")
        # Saves the only useful part of the string line which are the author list.
        authors_string = temp_string[:end_index]
        # Transform the string to a list by replacing the quotes and splitting it where commas are available
        # in order to be ready for the map job.
        authors = authors_string.replace('"', "").split(",")

        for author in authors:
            # With strip it removes some whitespaces between some names in order to look more elegant
            # and prints the full name and the position in published paper
            # Write the results to STDOUT (standard output)
            # This is the input for the reducer.py
            print('%s\t%s' % (author.strip() + "," + str(authors.index(author) + 1), 1))
