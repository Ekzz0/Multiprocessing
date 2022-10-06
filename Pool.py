import multiprocessing

def end_func(response):
    print("End!")
    print(response)

def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}] value: {value}")
    return value

def get_value1(x,y):
    print(f"{x}, {y}")

if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()*3) as p:
        p.starmap(get_value1, [(1, 1), (2, 2)])
        p.map_async(get_value, list(range(10)), callback=end_func)
        p.close()
        p.join()