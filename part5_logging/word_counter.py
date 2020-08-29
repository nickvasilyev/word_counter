#!/usr/bin/env python3
from my_counter import MyCounter
import argparse
import logging

parser = argparse.ArgumentParser(description='Word Counter Help')
parser.add_argument('-w', '--words', type=int, default=5, help='How many top words to print')
parser.add_argument('-f', '--file', type=str, required=True, help='File to read')
parser.add_argument('-v', action='store_true', default=False, help="Turn On Debug Logging")
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG if args.v else logging.INFO,
                    format='%(asctime)s %(levelname)s %(process)d %(funcName)s %(message)s')
logging.debug("TEST DEBUG MESSAGE")
logging.info("TEST INFO MESSAGE")
logging.info(args)

my_counter = MyCounter(args.file, args.words)
top_words = my_counter.get_top_words()

print(top_words)
