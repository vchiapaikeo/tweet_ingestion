#!/usr/bin/env python

"""Module defines functions used to create a word frequency map from lines of 
tweets

The word freqeuncy map is created by reading words in a file (or lines in a file 
and words in a line), attempting to add that word to a general dictionary, 
and then upon completion sorting the dictionary and outputting it to a file in 
the form 'key\tvalue'

"""

import os
import sys


def get_word_freq(filein):
    """
    Produces a sorted word frequency map from filein to fileout

    Parameters:
        filein - source file to iterate through

    Returns:
        dict: hash map of words and associated frequencies
    """
    freq = {}

    # Open file handles with context manager
    with open(filein) as f:

        # Read a single line at a time so as not to crush memory
        for line in f:

            # Tokenize and iterate
            for word in line.split():

                # Use try/except instead of if/then for performance
                # Likely after the first 1M tweets that the key will be contained
                try:
                    freq[word] += 1
                except KeyError:
                    freq[word] = 1

    return freq


def sort_and_write_dict(dct, fileout, tab_space=28):
    """
    Outputs dictionary to fileout ordered by key

    Parameters:
        dict - source file to iterate through
        fileout - output file to write sorted map to
        tab_space - optional param to specify separation width between key and values

    Returns:
        void - writes output to fileout
    """
    with open(fileout, 'w') as f:

        # Iterate through dictionary post-sorting
        for key in sorted(dct):

            # Write key, values to dictionary and separate by specified spaces in tab_space
            f.write("{k}{v}\n".format(k=key.ljust(tab_space), v=dct[key]))


def main():
    if len(sys.argv) == 3:
        print('Accepting parameters from command line')
        script, FILE_INPUT, FILE_OUTPUT = sys.argv
    else:
        print('Accepting parameters from module')
        FILE_INPUT = os.path.join('..', 'tweet_input', 'tweets.txt')
        FILE_OUTPUT = os.path.join('..', 'tweet_output', 'ft1.txt')

    print('Generating dictionary from "{0}"'.format(FILE_INPUT))
    d = get_word_freq(FILE_INPUT)

    print('Writing results to "{0}"'.format(FILE_OUTPUT))
    sort_and_write_dict(d, FILE_OUTPUT)

    print('Script complete. File output to "{0}"\n'.format(FILE_OUTPUT))


if __name__ == "__main__":
    main()