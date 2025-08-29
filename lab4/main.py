import pandas as pd

class CSVChek:
    def __init__(self, f, cols, types):
        self.f = f       # файл
        self.c = cols    # список колонок
        self.t = types   # словарь типов
        self.d = None    # датафрейм

    def run(self):
        try:
            self.d = pd.read_csv(self.f)

            if self.d.empty:
                raise ValueError("Файл пустой")

            self._chk()
            print("Чтение датафрейма завершено успешно")

        except FileNotFoundError:
            print(f"Файл '{self.f}' не найден")
        except pd.errors.EmptyDataError:
            print(f"Файл '{self.f}' пуст")
        except ValueError as e:
            print("Ошибка:", e)
        except Exception as e:
            print("Неожиданная ошибка:", e)

    def _chk(self):
        errs = []

        if list(self.d.columns) != self.c:
            errs.append(f"Колонки не совпадают.Ожидалось: {self.c}Факт: {list(self.d.columns)}")

        for col, tp in self.t.items():
            if col not in self.d.columns:
                errs.append(f"Нет колонки '{col}'")
            else:
                if str(self.d[col].dtype) != tp:
                    errs.append(f"Колонка '{col}' должна быть {tp}, а {self.d[col].dtype}")

        if errs:
            raise ValueError("Проблемы со структурой:- " + "- ".join(errs))



cols = [
    "Участники гражданского оборота", "Тип операции", "Сумма операции",
    "Вид расчета", "Место оплаты", "Терминал оплаты", "Дата оплаты",
    "Время оплаты", "Результат операции", "Cash-back", "Сумма cash-back"
]

types = {
    "Участники гражданского оборота": "object",
    "Тип операции": "object",
    "Сумма операции": "float64",
    "Вид расчета": "object",
    "Место оплаты": "object",
    "Терминал оплаты": "object",
    "Дата оплаты": "object",
    "Время оплаты": "object",
    "Результат операции": "object",
    "Cash-back": "object",
    "Сумма cash-back": "float64"
}

f = 'var6.csv'

chk = CSVChek(f, cols, types)
chk.run()

