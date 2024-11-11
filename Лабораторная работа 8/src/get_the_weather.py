import requests
import os
from typing import Any


class WeatherAPI:
    """
    Класс для получения данных о погоде.
    """
    def __init__(self):
        """
        Raises:
            ValueError: Нужно установить API ключ, читать README.md
        """
        self.api_key = os.getenv("WEATHER_API")
        if not self.api_key:
            raise ValueError("Не установлен API ключ. Установите переменную окружения WEATHER_API")
        
        self.headers = {
            "X-Yandex-API-Key": self.api_key
        }
        
        # Координаты Санкт-Петербурга
        self.lat = 59.937500
        self.lon = 30.308611

    def get_forecast(self) -> dict[str, Any]:
        """Получает данные о погоде через API pogoda.yandex.ru

        Raises:
            Exception: Ошибка связанная с ключом API
            Exception: Ошибка при получении погоды

        Returns:
            dict[str, Any]: Возвращает json c погодой
        """
        url = f"https://api.weather.yandex.ru/v2/forecast?lat={self.lat}&lon={self.lon}&lang=ru_RU&limit=5"
        
        try:
            response = requests.get(url, headers=self.headers)
            data = response.json()
            
            if response.status_code == 200:
                return data
            else:
                raise Exception(f"Ошибка {response.status_code}: {response.text}")
                
        except Exception as e:
            raise Exception(f"Ошибка при получении прогноза погоды: {e}")
    
    def print_forecast(self, data: dict[str, Any]) -> None:
        """Печатает данные о дате и и температуре

        Args:
            data (dict[str, Any]):
                Пример:
                    Дата: 2024-11-12
                    Средняя температура: 4°C
                    ------------------------------
                    ...
                    ------------------------------
                    Дата: 2024-11-16
                    Средняя температура: 8°C
                    ------------------------------
        """
        for forecast in data['forecasts']:
            date = forecast['date']
            temp = forecast['parts']['day']['temp_avg']
            
            print(f"Дата: {date}")
            print(f"Средняя температура: {temp}°C")
            print("-" * 30)
