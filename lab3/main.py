import pandas as pd

class PaymentTerminal:
    def __init__(self, full_terminal_name, dataframe):
        self.full_terminal_name = full_terminal_name
        self.bank_name = full_terminal_name.split('-')[0]
        self.dataframe = dataframe

    def remove_duplicates(self):
        self.dataframe.drop_duplicates(inplace=True)
        return self


# Загружаем данные
df = pd.read_csv('var6.csv')

# Считаем количество дубликатов
total_duplicates = df.duplicated().sum()

# Группируем по банкам
bank_dataframes = {}

for terminal_name in df['Терминал оплаты'].unique():
    current_terminal = PaymentTerminal(terminal_name, df)

    if current_terminal.bank_name not in bank_dataframes:
        bank_df = df[df['Терминал оплаты'].str.startswith(current_terminal.bank_name)].copy()
        bank_dataframes[current_terminal.bank_name] = PaymentTerminal(current_terminal.bank_name, bank_df)

print("Обрабатываем и сохраняем датасеты по банкам в отдельные файлы...")
for bank_name, payment_terminal_obj in bank_dataframes.items():
    payment_terminal_obj.remove_duplicates()

    file_name = f"{bank_name}_terminal.csv"
    # Сохраняем прямо в текущую папку
    payment_terminal_obj.dataframe.to_csv(file_name, index=False)
    print(f"Файл '{file_name}' успешно создан.")

print("Готово! Все датасеты обработаны и сохранены.")
print(f"Количество повторяющихся строк в наборе данных: {total_duplicates}")
