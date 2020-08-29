#!/usr/bin/env python3
from collections import Counter

file_path = '../alice.txt'
counter = Counter()

with open(file_path) as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        words = line.split(' ')
        counter.update(words)

print(counter.most_common(5))
