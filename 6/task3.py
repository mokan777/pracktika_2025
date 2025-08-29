
import asyncio

class PeriodicTask:
    async def run(self):
        for _ in range(10):  # 10 раз по 2 секунды = 20 секунд
            print("Периодическая задача выполняется")
            await asyncio.sleep(2)
