from my_counter import MyCounter
sample_file = './tests/short_alice.txt'

def test_MyCounter_returns_proper_count_of_words_10():
    top_words = MyCounter(sample_file, 10).get_top_words()
    assert len(top_words) == 10

def test_MyCounter_returns_proper_count_of_words_20():
    top_words = MyCounter(sample_file, 20).get_top_words()
    assert len(top_words) == 20

def test_MyCounter_returns_top_words():
    top_words = MyCounter(sample_file, 5).get_top_words()
    assert top_words == [('the', 14), ('to', 11), ('a', 11), ('she', 9), ('of', 8)]
