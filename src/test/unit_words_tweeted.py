"""
Test core functions in words_tweeted module

Given input string from a text file,

pop tarts i like pop tarts pop pop tarts
flintstones vitamins primeday flintstones vitamins primeday
deal deal deal deal

get_word_freq() will return a dictionary as follows:


Given a dictionary of above key/values,

sort_and_write_dict() will write sorted output to file as follows:

deal                        4
flintstones                 2
i                           1
like                        1
pop                         4
primeday                    2
tarts                       3
vitamins                    2

"""

import os
import unittest
import src.words_tweeted

# Set input and output constants
TESTDATADIR = 'data'
TESTDATAFILE = 'tweets_test.txt'
TESTOUTFILE = 'words_tweeted_output.txt'
INPUTSTR = 'pop tarts i like pop tarts pop pop tarts\nflintstones vitamins primeday flintstones vitamins primeday\ndeal deal deal deal'
OUTPUTDICT = {'vitamins': 2, 'deal': 4, 'tarts': 3, 'i': 1, 'pop': 4, 'primeday': 2, 'flintstones': 2, 'like': 1}
OUTPUTSTR = """deal                        4
flintstones                 2
i                           1
like                        1
pop                         4
primeday                    2
tarts                       3
vitamins                    2
"""

class WordsTweetedTest(unittest.TestCase):
    """ Test words_tweeted module"""

    test_infile = os.path.join(TESTDATADIR, TESTDATAFILE)
    test_outfile = os.path.join(TESTDATADIR, TESTOUTFILE)

    def test_get_word_freq(self):
        """Test get_word_freq() for correct key/value pairs"""

        # Set test_answer to function call on test_infile
        test_answer = src.words_tweeted.get_word_freq(self.test_infile)

        # Expect equality between test_answer and OUTPUTDICT
        self.assertEqual(test_answer, OUTPUTDICT)

    def test_sort_and_write_dict(self):
        """Test sort_and_write_dict to accept dict, sort, and write key/values to outfile"""

        # Remove the output file if it exists from a prev test
        try:
            os.remove(self.test_outfile)
        except OSError:
            pass

        # Call function with passed dict and output to test_outfile
        src.words_tweeted.sort_and_write_dict(OUTPUTDICT, self.test_outfile)

        # Expect equality between test_outfile and OUTPUTSTR
        with open(self.test_outfile) as f:
            self.assertEqual(f.read(), OUTPUTSTR)


if __name__ == "__main__":
    unittest.main()