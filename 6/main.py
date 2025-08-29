
import asyncio
from task1 import EventTimer
from task2 import DictManager
from task3 import PeriodicTask

if __name__ == "__main__":
    # Задание 1
    timer = EventTimer()
    timer.start_threads()
    
    timer.trigger()
    timer.wait_finish()

    # Задание 2
    manager = DictManager()
    result = manager.fill_dict()
    print("Словарь:", result)

    # Задание 3
    task = PeriodicTask()
    asyncio.run(task.run())
