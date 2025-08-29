
import threading

class EventTimer:
    def __init__(self):
        self.event = threading.Event()
        self.threads = []

    def worker(self, i):
        print(f"Поток {i} ждет...")
        self.event.wait()
        print(f"Поток {i} начал!")

    def start_threads(self):
        for i in range(10):
            t = threading.Thread(target=self.worker, args=(i,))
            t.start()
            self.threads.append(t)

    def trigger(self):
        self.event.set()

    def wait_finish(self):
        for t in self.threads:
            t.join()
