import pytest

@pytest.fixture()
def incorrect_word():
    return "карова"

@pytest.fixture()
def correct_word():
    return "корова"