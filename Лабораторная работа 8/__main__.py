from utils.get_the_weather import WeatherAPI
from utils.plot_graph import WeatherPlotter


def main():
    """
    Основная функция приложения.

    Получает данные о погоде через WeatherAPI, выводит их в консоль
    и создает визуализацию с помощью WeatherPlotter.

    Raises:
        Exception: При возникновении ошибок в процессе работы
    """
    try:
        # Получаем данные о погоде
        weather_api = WeatherAPI()
        weather_data = weather_api.get_forecast()

        # Выводим прогноз в консоль
        weather_api.print_forecast(weather_data)

        # Создаем визуализацию
        plotter = WeatherPlotter()
        plotter.plot_weather_data(weather_data)
        print("Графики сохранены в файл 'weather_analysis.png'")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
