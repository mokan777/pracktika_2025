
from multiprocessing import Process, Manager

class DictManager:
    def __init__(self):
        pass  

    def worker(self, shared_dict, key, value):
        shared_dict[key] = value

    def fill_dict(self):
        with Manager() as manager:
            shared_dict = manager.dict()
            processes = []
            for i in range(5):
                p = Process(target=self.worker, args=(shared_dict, f"key{i}", i))
                processes.append(p)

            for p in processes:
                p.start()
            for p in processes:
                p.join()

            return dict(shared_dict)
