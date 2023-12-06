import pytest

import main as main

def test_addition():
    result = main.addition(2, 2)
    assert result == 4


def test_upper_case():
    result = main.upper_case("hello")
    assert result == "HELLO"

def test_addition():
    result = main.addition(4, 2)
    assert result == 6