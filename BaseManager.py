import multiprocessing
import time
from multiprocessing.managers import BaseManager

def f1(m_dict, m_array):
    return time.time()




if __name__ == '__main__':
    BaseManager.register("Base", callable=f1)
    manager = BaseManager(address=('', 4444), authkey=b'abc')
    server = manager.get_server()
    server.serve_forever()
