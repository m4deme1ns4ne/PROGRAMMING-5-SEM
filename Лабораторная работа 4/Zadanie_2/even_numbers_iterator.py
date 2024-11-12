from typing import Self


class FibonacchiLst:
    def __init__(self, lst) -> None:
        self.lst = lst
        self.idx = 0
        if self.lst:
            self.fib_set = self.generate_fib_set(max(self.lst))
        else:
            self.fib_set = set()

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int | StopIteration:
        """Выдаёт следующее значение из генератора

        Raises:
            StopIteration: Если индекс больше длины передаваемого списка, то возникает
            ошибка, которая останавливает итерацию

        Returns:
            int | StopIteration: Возвращает число, если оно есть в множестве fib_set
        """
        while True:
            if self.idx >= len(self.lst):
                raise StopIteration
            
            value = self.lst[self.idx]
            self.idx += 1
            
            if value in self.fib_set:
                return value

    def generate_fib_set(self, max_value: int) -> set[int]:
        """Создаёт множество с числами Фибоначчи

        Args:
            max_value (int): Максимальное значение в получаемом списке

        Returns:
            list[int]: Множество с числами фибоначчи, зависящее от
            максимального значения в передаваемом списке
        """
        fib_set = set()
        a, b = 0, 1
        
        while a <= max_value:
            fib_set.add(a)
            a, b = b, a + b
        
        return fib_set

# Пример использования:
lst = []
fib_iterator = FibonacchiLst(lst)
print(list(fib_iterator))
