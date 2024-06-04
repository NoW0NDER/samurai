import pickle

from multiprocessing import shared_memory
class Samurai():
    def __init__(self, name = None, obj = None):
        if name is None:
            raise ValueError("Name is required")
        else:
            self.name = name
        try:
            self.shm = shared_memory.SharedMemory(name = self.name, create = False)
            self.is_created = True
        except FileNotFoundError:
            self.is_created = False
        if self.is_created:
            self.obj = pickle.loads(self.shm.buf)
        else:
            to_share = pickle.dumps(obj)       
            self.shm = shared_memory.SharedMemory(name = self.name, create = True, size = to_share.__sizeof__())
            self.shm.buf[:len(to_share)] = to_share
    def get_spirit(self):
        if self.is_created:
            return self.obj
        else:
            return pickle.loads(self.shm.buf)
    
    def __del__(self):
        self.shm.close()
        self.shm.unlink()