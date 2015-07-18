Tweet Ingestion - Insights Coding Challenge Submitted by Victor Chiapaikeo
==========================================================================

## Overview

Tweet Ingestion application designed to efficiently ingest a high volume of tweets and perform processing which includes the following:

- Produce a file that groups words from tweets and counts their frequency. Example output is as follows:
```
	analytics  		    		1
	bigdata 					3
	kdn 						1
	smb 						1
```

- Produce a running median of unique word counts from tweets. Example output is as follows:
```
	11.0
	12.5
	14.0
```

## Setup

Scripts were written using Python 2.7 and have not been tested for portability to Python 3.X.

You are encouraged to use a python virtual environment using virtualenv and pip. NOTE (2015-07-18): As of now, the requirements file is empty because no modules outside the default build are used.

```sh
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements
```

## Description of modules imported and application

- os - operating system interface related and used to port-ably join paths, remove files, etc.
- sys - interpreter-related and used to parse parameters from the commandline
- heapq - priority queue algorithm used to efficiently obtain root from an array
- unittest - framework used to create and employ unit tests

## Check out and run

Applications can be run separately or together from a shell script.

**To run separately:**

Both words_tweeted.py and median_unique.py accepts the same two parameters:

1. Input file: this is the file containing tweets separated by newlines and located in
2. Output file: this is the file that is produced and located

```sh
$ git clone https://github.com/vchiapaikeo/tweet_ingestion.git
$ cd tweet_ingestion
$ python words_tweeted.py tweet_input/tweets.txt tweet_output/ft1.txt
$ python median_unique.py tweet_input/tweets.txt tweet_output/ft1.txt
```

**To run from shell script:**

This scenario is simpler and will execute both scripts back to back.
```sh
$ ./run.sh
```

## Test
Unit tests have been created to test functions within the app.

Test should be executed on the commandline at the top-level dir like below

```sh
$ cd tweet_ingestion
$ python -m src.tests.unit_words_tweeeted
$ python -m src.tests.unit_median_unique
```

The following output should return:
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK

```
