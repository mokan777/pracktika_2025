import pandas as pd
import matplotlib.pyplot as plt
from logger import log_decorator

class GraphicStatistics:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    @log_decorator
    def show_histogram(self):
        # Фильтруем последнюю дату (чтобы не смешивать года)
        last_date = self.df['date'].max()
        filtered = self.df[self.df['date'] == last_date]

        # Строим гистограмму по странам
        plt.figure(figsize=(12, 6))
        plt.bar(filtered['name'], filtered['dollar_price'], color='orange')
        plt.xticks(rotation=90)
        plt.xlabel("Страна")
        plt.ylabel("Цена (USD)")
        plt.title(f"Стоимость бигмака по странам ({last_date})")
        plt.tight_layout()
        plt.show()
