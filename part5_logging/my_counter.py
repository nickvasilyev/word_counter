from collections import Counter
import logging

class MyCounter:
    def __init__(self, file_path, top_words):
        self.file_path = file_path
        self.top_words = top_words
        logging.info("Started My Counter")

    def get_top_words(self):
        self.counter = Counter()
        with open(self.file_path) as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                words = line.split(' ')
                logging.debug(f"Updating the counter with {str(words)}")
                self.counter.update(words)
        return self.counter.most_common(self.top_words)
