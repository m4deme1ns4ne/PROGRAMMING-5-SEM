from src.get_the_weather import WeatherAPI


def main():
    """
    Основная функция приложения.
    
    Получает данные о погоде через WeatherAPI, выводит их в консоль.
    
    Raises:
        Exception: При возникновении ошибок в процессе работы
    """
    try:
        # Получаем данные о погоде
        weather_api = WeatherAPI()
        weather_data = weather_api.get_forecast()
        
        # Выводим прогноз в консоль
        weather_api.print_forecast(weather_data)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
