import pytest

from even_numbers_iterator import FibonacchiLst


# Предположим, что класс FibonacchiLst уже определен где-то в коде.
# from your_module import FibonacchiLst 

def test_fib_lst_with_fib_numbers():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    expected_output = [0, 1, 2, 3, 5, 8, 1]
    fib_iterator = FibonacchiLst(lst)
    assert list(fib_iterator) == expected_output

def test_fib_lst_with_no_fib_numbers():
    lst = [4, 6, 7]
    expected_output = []
    fib_iterator = FibonacchiLst(lst)
    assert list(fib_iterator) == expected_output

def test_fib_lst_with_all_zeroes():
    lst = [0] * 10
    expected_output = [0] * len(lst)
    fib_iterator = FibonacchiLst(lst)
    assert list(fib_iterator) == expected_output

def test_empty_list():
    lst = []
    expected_output = []
    fib_iterator = FibonacchiLst(lst)
    assert list(fib_iterator) == expected_output
