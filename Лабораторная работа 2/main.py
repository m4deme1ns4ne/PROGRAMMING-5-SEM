import requests

def get_weather_by_city_id(city_id, api_key):
    # URL для отправки запроса
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Создаем полный URL запрос с параметрами
    complete_url = f"{base_url}id={city_id}&appid={api_key}&units=metric"

    try:
        # Выполняем HTTP GET запрос
        response = requests.get(complete_url)

        # Если запрос прошел успешно (статус код 200)
        if response.status_code == 200:
            # Парсим ответ в формате JSON
            data = response.json()

            # Извлечение нужной информации
            city_name = data['name']
            main = data['main']
            wind = data['wind']
            weather_description = data['weather'][0]['description']

            # Формируем результирующую строку
            weather_info = (
                f"City: {city_name}\n"
                f"City ID: {city_id}\n"
                f"Temperature: {main['temp']}°C\n"
                f"Humidity: {main['humidity']}%\n"
                f"Pressure: {main['pressure']} hPa\n"
                f"Wind Speed: {wind['speed']} m/s\n"
                f"Weather Description: {weather_description}"
            )

            return weather_info
        else:
            # Если город не найден или произошла ошибка
            return f"Error: Unable to fetch weather data for city_id {city_id}. Response Code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        # Обработка исключений, связанных с сетью
        return f"Error: Unable to connect to the OpenWeatherMap service. Details: {str(e)}"

# Использование функции
api_key = "01a1bb505794b1ea19682f14392255f9"
city_id = 524901  # Пример ID города Москвы
weather_report = get_weather_by_city_id(city_id, api_key)
print(weather_report)
