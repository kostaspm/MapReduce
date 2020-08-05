#!/usr/bin/env python3

from operator import itemgetter
import sys

current_author = None
current_count = 0
author = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    author, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_author == author:
        current_count += count
    else:
        if current_author:
            # write result to STDOUT
            print('%s\t%s' % (current_author, current_count))
        current_count = count
        current_author = author

# do not forget to output the last author if needed!
if current_author == author:
    print('%s\t%s' % (current_author, current_count))

