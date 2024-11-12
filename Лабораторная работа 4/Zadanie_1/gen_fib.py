import functools


def my_genn():
    """Сопрограмма, возвращающая список элементов ряда Фибоначчи"""
    number_of_fib_elem = yield []  # Изменяем первый yield, чтобы возвращать пустой список
    while True:
        if number_of_fib_elem <= 0:
            raise ValueError("Количество элементов должно быть положительным числом")
            
        a, b = 0, 1
        result = [a]
        
        for _ in range(number_of_fib_elem - 1):
            result.append(b)
            a, b = b, a + b
            
        number_of_fib_elem = yield result  # Возвращает список чисел Фибоначчи

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


my_genn = fib_coroutine(my_genn)
gen = my_genn()
print(gen.send(5))
