"""1. Реализовать функцию, которая на вход принимает целое положительное число n и возвращает при вызове
 объект-генератор, который по запросу будет возвращать значение факториала всех чисел от 0 до n.
 5! = 1 * 2 * 3 * 4 * 5 
"""


def fact(n):
    count = 1
    for i in range(1, n + 1):
        count *= i
        yield count

f = fact(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

for i in fact(6):
    print(i)
