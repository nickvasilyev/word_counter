#!/usr/bin/env python3
from my_counter import MyCounter
import argparse

parser = argparse.ArgumentParser(description='Word Counter Help')
parser.add_argument('-w', '--words', type=int, default=5, help='How many top words to print')
parser.add_argument('-f', '--file', type=str, required=True, help='File to read')
args = parser.parse_args()
print(args)

my_counter = MyCounter(args.file, args.words)
top_words = my_counter.get_top_words()

print(top_words)
