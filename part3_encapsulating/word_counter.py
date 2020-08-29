#!/usr/bin/env python3
import argparse
from my_counter import MyCounter

parser = argparse.ArgumentParser(description='Word Counter Help')
parser.add_argument('-w', '--words', type=int, default=5, help='Number of top terms to extract')
parser.add_argument('-f', '--file', type=str, required=True, help='File to Read')
args = parser.parse_args()
print(args)

counter = MyCounter(args.file, args.words)
top_words = counter.get_top_words()
print(top_words)
