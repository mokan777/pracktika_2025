import pandas as pd
import getpass
from datetime import datetime

LOG_FILE = "logs.csv"

def log_decorator(func):
    def wrapper(*args, **kwargs):
        # Пытаемся загрузить существующий лог
        try:
            df_log = pd.read_csv(LOG_FILE)
        except FileNotFoundError:
            df_log = pd.DataFrame(columns=["id", "pc_username", "function_name", "Date", "Time"])

        # Определяем id
        log_id = len(df_log) + 1
        username = getpass.getuser()  # имя пользователя системы
        func_name = func.__name__
        now = datetime.now()
        date = now.strftime("%d.%m.%Y")
        time = now.strftime("%H:%M:%S")

        # Новая запись
        new_log = pd.DataFrame({
            "id": [log_id],
            "pc_username": [username],
            "function_name": [func_name],
            "Date": [date],
            "Time": [time]
        })

        # Обновляем лог
        df_log = pd.concat([df_log, new_log], ignore_index=True)
        df_log.to_csv(LOG_FILE, index=False)

        return func(*args, **kwargs)
    return wrapper
