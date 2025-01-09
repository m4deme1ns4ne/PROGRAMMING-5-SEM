import json
import time
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import functools
from typing import Callable


class rate_limit:
    """
    Класс-декоратор для ограничения частоты вызова функции.
    """
    def __init__(self, interval: float = 1.0):
        self.interval = interval
        self.last_called = 0.0

    def __call__(self, func: Callable):
        def wrapper(*args, **kwargs):
            elapsed_time = time.time() - self.last_called
            if elapsed_time < self.interval:
                time.sleep(self.interval - elapsed_time)
            result = func(*args, **kwargs)
            self.last_called = time.time()
            return result
        return wrapper

class CurrencyRates:

    @rate_limit(1)  # Ограничение: не чаще 1 раза в секунду
    def get_currencies(self) -> list[
                                    dict[str: list[str, float]]
                                    ]:
        """Получает значения в формате xml и форматирует их

        Returns:
            rates: Возврает список со словарями в формате:
                [{'GBP': ('Фунт стерлингов Соединенного королевства', '113,2069')}, 
                {'KZT': ('Казахстанских тенге', '19,8264')},
                {'TRY': ('Турецких лир', '33,1224')}]
        """
        # URL для получения XML с курсами валют от ЦБ РФ
        url = "http://www.cbr.ru/scripts/XML_daily.asp"

        # Загружаем данные
        response = requests.get(url)
        
        if response.status_code == 200:
            # Парсим XML
            tree = ET.ElementTree(ET.fromstring(response.content))
            root = tree.getroot()

            # Список для хранения курсов валют
            rates = []

            for valute in root.findall('Valute'):
                char_code = valute.find('CharCode').text
                name = valute.find('Name').text
                value = valute.find('Value').text.replace(',', '.')

                currency_rate = {"code": char_code, "name": name, "rate": float(value)}

                rates.append(currency_rate)

            return rates

        else:
            print("Ошибка при получении данных")
            return None
        
    def visualize_currencies(self, rates_list: list) -> None:
        """Визуализирует данные полученные из функции get_currencies

        Args:
            rates_list (list): Список с данными и курсе
        """
        
        if not rates_list:
            print("Нет данных для визуализации.")
            return
        
        codes = [currency['code'] for currency in rates_list]
        values = [currency['rate'] for currency in rates_list]

        plt.figure(figsize=(10, 6))
        
        plt.bar(codes, values)
        
        plt.xlabel('Валюта')
        plt.ylabel('Курс')
        
        plt.title('Курсы валют по отношению к рублю')
        
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        
        # Сохранение графика в файл currencies.jpg
        plt.savefig('currencies.jpg')


# Вывод в консоль
rates_instance = CurrencyRates()
rates_list = rates_instance.get_currencies()
if rates_list:
    print(json.dumps(rates_list, ensure_ascii=False, indent=4))

# Визуализация данных
rates_instance.visualize_currencies(rates_list)
