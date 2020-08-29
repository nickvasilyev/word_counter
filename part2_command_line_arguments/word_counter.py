#!/usr/bin/env python3
from collections import Counter
import argparse

parser = argparse.ArgumentParser(description='Word Counter Help')
parser.add_argument('-w', '--words', type=int, default=5, help='Number of top terms to extract')
parser.add_argument('-f', '--file', type=str, required=True, help='File to Read')
args = parser.parse_args()
print(args)

counter = Counter()

with open(args.file) as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        words = line.split(' ')
        counter.update(words)

print(counter.most_common(args.words))
