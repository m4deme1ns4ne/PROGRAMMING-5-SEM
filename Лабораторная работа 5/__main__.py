import json
import time
import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def rate_limit(interval: float = 1.0):
    """Декоратор для ограничения частоты вызова функции."""

    def decorator(func):
        last_called = [0.0]

        def wrapper(*args, **kwargs):
            elapsed_time = time.time() - last_called[0]
            if elapsed_time < interval:
                time.sleep(interval - elapsed_time)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result

        return wrapper

    return decorator


class SingletonMeta(type):
    """
    Метакласс, для создания синглтона CurrencyRates
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CurrencyRates(metaclass=SingletonMeta):

    @rate_limit(1)  # Ограничение: не чаще 1 раз в секунду
    def get_currencies(self) -> list[dict[str : list[str, float]]]:
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

            for valute in root.findall("Valute"):
                char_code = valute.find("CharCode").text
                name = valute.find("Name").text
                value = valute.find("Value").text.replace(",", ".")

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

        # Подготовка данных для графика
        codes = [currency["code"] for currency in rates_list]
        values = [currency["rate"] for currency in rates_list]

        plt.figure(figsize=(10, 6))

        plt.bar(codes, values)

        plt.xlabel("Валюта")
        plt.ylabel("Курс")

        plt.title("Курсы валют по отношению к рублю")

        plt.xticks(rotation=45)

        plt.tight_layout()

        # Сохранение графика в файл currencies.jpg
        plt.savefig("currencies.jpg")


if __name__ == "__main__":
    # Вывод в консоль
    rates_instance = CurrencyRates()
    rates_list = rates_instance.get_currencies()
    rates_list = rates_instance.get_currencies()
    if rates_list:
        print(json.dumps(rates_list, ensure_ascii=False, indent=4))

    # Визуализация данных
    rates_instance.visualize_currencies(rates_list)
