from time import time

def performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')
    return wrapper_func

@performance
def count():
    for i in range(1, 1000000000):
        i * 5

count()
