import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

class WeatherPlotter:
    """
    Класс для визуализации погодных данных.
    """

    def __init__(self):
        self.output_file = 'weather_analysis.png'
    
    def plot_weather_data(self, data):
        """
        Создает и сохраняет визуализацию погодных данных.
        """
        
        # Подготовка данных
        weather_data = [
            {
                'date': datetime.strptime(forecast['date'], '%Y-%m-%d'),
                'temperature': forecast['parts']['day']['temp_avg']
            }
            for forecast in data['forecasts']
        ]
        
        df = pd.DataFrame(weather_data)
        
        # Построение графиков
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # График рассеяния
        sns.scatterplot(data=df, x='date', y='temperature', ax=ax1, s=100, color='blue')
        ax1.set_title('График температуры по дням')
        ax1.set_xlabel('Дата')
        ax1.set_ylabel('Температура (°C)')
        
        # Ящик с усами
        sns.boxplot(y=df['temperature'], ax=ax2, color='lightblue')
        ax2.set_title('Распределение температуры')
        ax2.set_ylabel('Температура (°C)')
        
        plt.tight_layout()
        plt.savefig(self.output_file)
