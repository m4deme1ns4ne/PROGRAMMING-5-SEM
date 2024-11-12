import pytest

from gen_fib import my_genn


# Тесты для my_genn
def test_fibonacci_sequence():
    gen = my_genn()
    
    # Проверка правильности последовательности из 5 элементов
    assert gen.send(5) == [0, 1, 1, 2, 3]

def test_zero_elements():
    gen = my_genn()
    
    with pytest.raises(ValueError) as excinfo:
        gen.send(0)
        
    assert "Количество элементов должно быть положительным числом" in str(excinfo.value)

def test_negative_elements():
    gen = my_genn()
    
    with pytest.raises(ValueError) as excinfo:
        gen.send(-5)
        
    assert "Количество элементов должно быть положительным числом" in str(excinfo.value)

def test_single_element():
    gen = my_genn()
    
    # Проверка последовательности из одного элемента
    assert gen.send(1) == [0]

def test_two_elements():
    gen = my_genn()
    
    # Проверка последовательности из двух элементов
    assert gen.send(2) == [0, 1]
