import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def process(self):
        try:
            df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print("Файл не найден")
            return
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return

        if df.empty:
            print("Датасет пуст")
            return

        print("Чтение датафрейма завершено успешно.")
