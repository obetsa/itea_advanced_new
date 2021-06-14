'''1. Написать декоратор, который будет печатать на экран время работы функции. '''

# Fixed(hw1 branch)


import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start
        print(f"\nЧас виконання: {execution_time}\n")

        return result

    return wrapper


@time_decorator
def func():
    list_ = []
    for i in range(10 ** 5):
        list_.append(i)
    return list_

func()