from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2 - t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1 - Generator')
    for i in range(10000000):
        i*5

long_time()

@performance
def long_time2():
    print('2 - list')
    for i in list(range(10000000)):
        i*5

long_time2()

