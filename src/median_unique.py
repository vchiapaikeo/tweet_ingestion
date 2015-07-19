"""Module defines functions used to efficiently calculate a streaming median

The streaming median is calculated by keeping two priority queues (using Python's
heapq module) and leveraging a property associated with heaps where the root is
always the smallest element.

One queue will contain all numbers less than or equal to the median (low) while
the other queue will contain all numbers greater than or equal to the median. 

To calculate a running median at any given point, we need to know at most two values.
In the case of an odd number of elements, the element at the 50th percentile is
the median whereas in the case of an even number of elements, the average of the 
two elements surrounding the 50th percentile is the effective median.

See heapq documentation for more details
https://docs.python.org/2/library/heapq.html

"""
import os
import sys
import heapq


def get_streaming_median(filein):
    """
    Produces a streaming median from file's unique word count per line

    Parameters:
        filein - source file to iterate through

    Yields:
        int: the next median value
    """
    with open(filein) as read_handle:

        # Initialize vars used to retain median calculation
        low = []        # Low numbers are stored in this list (as a priority queue)
        high = []       # High numbers are stored in this list (as a priority queue)
        low_i = 0       # Keep a counter of values in the low array
        high_i = 0      # Keep a counter of values in the high array

        for line in read_handle:
            # Split the tweet by \s, make unique by turning into a set, and count length
            num = len(set(line.split()))

            # Step 1: Push new values to priority queue based on low queue root
            # In priority queue, the zero index (root) will always be the min value in the array
            # Negate any values going to the low queue so that root is the median
            if not low or (num <= low[0]*-1):
                heapq.heappush(low, num*-1)
                low_i += 1
            else:
                heapq.heappush(high, num)
                high_i += 1

            # Step 2: Perform re-balancing
            # If high has more elements than low, move high root over to low and increment/decrement counters
            if low_i < high_i:
                heapq.heappush(low, heapq.heappop(high)*-1)
                low_i += 1
                high_i -= 1

            # If low has more elements than high+1, move low root over to high and increment/decrement counters
            elif low_i > high_i+1:
                heapq.heappush(high, heapq.heappop(low)*-1)
                low_i -= 1
                high_i += 1

            # Step 3: Calculate median
            # When sum of counters is even, median is equal to the avg of low and high root
            # Also, turn this into a float with precision 1 decimal
            if (low_i + high_i) % 2 == 0:
                median = (low[0]*-1 + high[0]) / float(2)
            # When sum of counters is odd or there is only one tweet, then median is equal to low root
            # Also, turn this into a float with precision 1 decimal
            else:
                median = low[0]*float(-1)

            # Generate medians one at a time
            yield median
            

def write_streaming_values(fileout, gen):
    """
    Output values from a generator to a file

    Parameters:
        fileout - output file to write generator series to
        gen - generator series of values

    Returns:
        void: file is created at fileout location
    """
    with open(fileout, 'a') as append_handle:

        # Iterate through values in generator
        for val in gen:

            # Append value to file
            append_handle.write("{0}\n".format(val))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print('Accepting parameters from command line')
        script, FILE_INPUT, FILE_OUTPUT = sys.argv
    else:
        print('Accepting parameters from module')
        FILE_INPUT = os.path.join('..', 'tweet_input', 'tweets.txt')
        FILE_OUTPUT = os.path.join('..', 'tweet_output', 'ft2.txt')

    print('Appending calculated median from "{0}" to "{1}"'.format(FILE_INPUT, FILE_OUTPUT))
    write_streaming_values(FILE_OUTPUT, get_streaming_median(FILE_INPUT))

    print('Script complete. File output to {0}\n'.format(FILE_OUTPUT))