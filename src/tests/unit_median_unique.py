"""
Test core functions in median_unique module

Given input string from a text file...

pop tarts i like pop tarts pop pop tarts
flintstones vitamins primeday flintstones vitamins primeday
deal deal deal deal

get_streaming_median will yield iterable: [4.0, 3.5, 3.0]

Given a generator with these values: [4.0, 3.5, 3.0]

write_streaming_median will write to file this string: '4.0\n3.5\n3.0\n'

"""

import os
import unittest
from .. import median_unique

# Set input and output constants
WORKINGDIR = os.path.dirname(os.path.abspath(__file__))
TESTDATADIR = 'data'
TESTDATAFILE = 'tweets_test.txt'
TESTOUTFILE = 'median_unique_output.txt'
INPUTSTR = 'pop tarts i like pop tarts pop pop tarts\nflintstones vitamins primeday flintstones vitamins primeday\ndeal deal deal deal'
OUTPUTARRAY = [4.0, 3.5, 3.0]
OUTPUTSTR = '4.0\n3.5\n3.0\n'


class MedianUniqueTest(unittest.TestCase):
    """Test median_unique module"""

    test_infile = os.path.join(WORKINGDIR, TESTDATADIR, TESTDATAFILE)
    test_outfile = os.path.join(WORKINGDIR, TESTDATADIR, TESTOUTFILE)

    def test_get_streaming_median(self):
        """Test get_streaming_median() for correct median values"""

        # Create list to store median values generated from function call
        test_answer = [median for median in median_unique.get_streaming_median(self.test_infile)]

        # Expect equality between produced array and OUTPUTARRAY
        self.assertEqual(test_answer, OUTPUTARRAY)

    def test_write_streaming_values(self):
        """Test write_streaming_values() to accept generator and write its values to outfile"""

        # Remove the output file if it exists from a prev test
        try:
            os.remove(self.test_outfile)
        except OSError:
            pass

        # Define generic generator
        def median_gen():
            return (i for i in OUTPUTARRAY)

        # Call function with passed generator and output to test_outfile
        median_unique.write_streaming_values(self.test_outfile, median_gen())

        # Expect equality between produced str and OUTPUTSTR
        with open(self.test_outfile, 'r') as f:
            self.assertEqual(f.read(), OUTPUTSTR)


if __name__ == "__main__":
    unittest.main()
