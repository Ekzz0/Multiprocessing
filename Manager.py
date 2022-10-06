import multiprocessing
import time
from multiprocessing import Process, Manager

def f1(m_dict, m_array):
    m_dict["name"] = "test"
    m_array.append(1)




if __name__ == '__main__':
    with Manager() as m:
        d = m.dict()
        l = m.list()
        p = Process(target=f1, args=(d,l,))
        p.start()
        p.join()
        print(d)
        print(l)