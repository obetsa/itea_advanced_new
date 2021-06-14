'''2. Написать функцию для вычислений очередного числа Фибоначчи (можно через цикл,
можно через рекурсию).'''

# Fixed(hw1 branch)


n = int(input("Номер елемента: "))


def fibonacchi(n):
    a = 1
    b = 1
    i = 0
    while i < n - 2:
        summa = a + b
        a = b
        b = summa
        i = i + 1
 
    print("Значення: ", b)


fibonacchi(n)