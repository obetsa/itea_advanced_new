'''3. Реализовать функцию, которая принимает три позиционных аргумента и возвращает
сумму наибольших двух из них.'''

# Fixed(hw1 branch)

# a = int(input("First: "))
# b = int(input("Second: "))
# c = int(input("Third: "))


# def summax(a, b, c):
#     if a < b:
#         minimal = a
#     else:
#         minimal = b
#     if c < minimal:
#         minimal = c
#     res = a + b + c - minimal

#     print("Summa: ", res)

# summax(a, b, c)


x = int(input("First: "))
y = int(input("Second: "))
z = int(input("Third: "))


def my_func():
    numbers = [x, y, z]
    result = []
    max1 = max(numbers)
    result.append(max1)
    numbers.remove(max1)
    max2 = max(numbers)
    result.append(max2)
    print(sum(result))

my_func()