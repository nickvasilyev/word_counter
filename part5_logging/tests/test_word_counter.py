from my_counter import MyCounter
test_file = './tests/short_alice.txt'

def test_MyCounter_returns_proper_count_of_words_10():
    top_ten_words = MyCounter(test_file, 10).get_top_words()
    assert len(top_ten_words) == 10

def test_MyCounter_returns_top_words():
    top_five_words = MyCounter(test_file, 5).get_top_words()
    assert top_five_words == [('', 84), ('the', 77), ('of', 55), ('to', 46), ('and', 43)]
