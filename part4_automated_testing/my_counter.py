from collections import Counter

class MyCounter:
    def __init__(self, file_path, top_words):
        self.file_path = file_path
        self.top_words = top_words

    def get_top_words(self):
        self.counter = Counter()
        with open(self.file_path) as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                words = line.split(' ')
                self.counter.update(words)
        return self.counter.most_common(self.top_words)
