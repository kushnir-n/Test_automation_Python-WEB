from func import check_text

def test_step_1(incorrect_word, correct_word):
    assert correct_word in check_text(incorrect_word), "test1 SOAP FAIL"