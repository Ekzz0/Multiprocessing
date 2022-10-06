import multiprocessing
import time
from multiprocessing import Process, Barrier

def f1(b):
    name= multiprocessing.current_process().name
    b.wait()
    print(f"[{name}] - запущено")




if __name__ == '__main__':
    b = Barrier()
    for _ in range(5):
        Process(target=f1, args=(b,)).start()
    #Process(target=f2, args=(b,)).start()