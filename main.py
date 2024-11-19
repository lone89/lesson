# a = []
#
# for i in range(0, 100, 2):
#     a.append(i)
#
# print(a)

#list Comprehension

# a = [i for i in range(0, 100, 2) if i % 4 == 0 if i % 8 == 0]
#
# print(a)

# тернарный оператор

# a = 2
#
# b = a + 2 if a % 2 == 0 else a + 1
#
# print(b)

# Функции

# def sum_two_numbers(num1, num2):
#     return num1 + num2
#
#
# print(sum_two_numbers(5, 10))
# print(sum_two_numbers(1, 4))
# print(sum_two_numbers(5, 20))
# print(sum_two_numbers(5, 100))


# def filter_odd_numbers(list1):
#     result = [i for i in list1 if i % 2 == 0]
#
#     return result


# def filter_odd_numbers(list1):
#     result = []
#
#     for i in list1:
#         if i % 2 == 0:
#             result.append(i)
#
#     return result

# def filter_odd_numbers(list1):
#     return [i for i in list1 if i % 2 == 0]
#
# print(filter_odd_numbers([1, 2, 4, 6, 7, 5, 8, 10, 2]))  # [2, 4, 6, 8, 10, 2]
#

# def sum_v_2(list1, count):
#     result = 0
#     for i, v in enumerate(list1):
#         result += v
#
#         if i + 1 == count:
#             return result

# def sum_v_2(list1, count=5):
#     return sum(list1[:count])
#
# print(sum_v_2([1,2,3,4,5], 3))
# print(sum_v_2(count=3, list1=[6,7,8,9,10]))
# print(sum_v_2(list1=[6,7,8,9,10]))

# def sum_v_2(num1, num2, num3=4, *args, num4, num5=80, **kwargs):
#     return kwargs.get("c")
#
#
# a = sum_v_2(12,15,16,17, 100, 2, 35, num4=5, num5=4, a=10, b=20, c=30)
#
# print(a)

# a, *b, c = [1, 2,2,4,5,6, 5]
#
# print(a, b, c)

# def a(b,c,d):
#     print(b,c,d)

# a(*[1,2,3])



# def full_name(name, surname, *args, a, b, c, **kwargs):
#     return f"{name} {surname}", args
#
# nums = 1, 2, 3, 4, 5, 6
#
# print(full_name("Klimko", "Kirill", *nums, a=1, b=2, c=3, pasd=123, asdasd=1241))

# B: От A до B
# Даны два целых числа A и В (каждое в отдельной строке).
# Выведите все числа от A до B включительно,
# в порядке возрастания, если A < B, или в порядке убывания в противном случае.
#
# Ввод	Вывод
# 5
# 1
# 5 4 3 2 1

# def fibonacci(num, num2):
#     bigest = num if num > num2 else num2
#     lower = num if num < num2 else num2
#
#     if bigest == lower:
#         return
#
#     return fibonacci(bigest-1, lower)
#
#
# a = fibonacci(10, 6)
# print(" ".join(a))


# c = 5

# def b(num1):
#     def c(num1):
#         return a + num1
#
#     return c


# def b(num1):
#     def c(num2):
#         nonlocal num1
#         result = num2 * num1
#         if result == 45:
#             num1 = 1000
#         return result
#
#     return c
#
# nine = b(9)
#
# print(nine(1))
# print(nine(2))
# print(nine(3))
# print(nine(4))
# print(nine(5))
# print(nine(6))
# print(nine(7))
# print(nine(8))
# print(nine(9))


# import time
#
#
# def progress_time(show_print, to_do):
#     def inner(func):
#         result = None
#         def wrapper(*args, **kwargs):
#             nonlocal result
#             start = time.time()
#             if not to_do:
#                 result = func(*args, **kwargs)
#             finish = time.time()
#             if show_print:
#                 print(f'Функция - {func.__name__} отработала за', finish - start)
#             return result
#         return wrapper
#     return inner
#
# @progress_time(show_print=True, to_do=False)
# def medium(number):
#     time.sleep(number)
#     return "medium"
#
# medium(4)
#
# print(progress_time(show_print=True, to_do=False)(medium)(4))


# a = [i for i in range(100) if i % 2 == 0]
# b = {i for i in range(100)}
# c = {i: v for i, v in enumerate(range(100))}
# v = tuple([i for i in range(100)])
# h = frozenset([i for i in range(100)])
#
#
# print(h)

import sys

# a = (i for i in range(10000))
# print(a)
# print(sys.getsizeof(b))
# print(sys.getsizeof(a))
#
# for i in a:
#     print(i)
#     print("END")
# print(next(a))
#
# for i in a:
#     print(i)



# def gen():
#     for i in range(100):
#         yield i
#
# a = gen()
# print(next(a))
#
# for i in range(10):
#     print(i ** 2)
#
# b = "pes"
#
# print(next(a))


# def gen():
#     yield "1"
#     yield "2"
#     yield "3"
#     yield "4"
#     yield "5"
#     yield "6"
#
# a = gen()
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# def gen():  # (i for i in range(100) if i % 2 == 0)
#     for i in range(100):
#         if i % 2 == 0:
#             yield i

# def gen():  # (i if i % 2 == 0 else 10 for i in range(100))
#     for i in range(100):
#         if i % 2 == 0:
#             yield i
#         else:
#             yield 10
#
# print(list(gen()))


# def asd():
#     for i in range(100):
#         yield i
#
# def gen():
#     yield from asd()
#
#     for i in ["a", "b", "c"]:
#         yield i


# def gen():
#     n = 2
#     for i in range(1, 5):
#         b = yield i ** n
#         if b is not None:
#             print(b)
#
# a = gen()
#
# print(next(a))
# print(next(a))

# a = open("first.txt", "w")
#
# a.write("123123123123213")
# a.read()
#
# a.close()
#
# a = open("first.txt", "r")
#
# print(a.readline())
#
# a.close()

import json
import pickle

with open("first.json", "w+") as file:
    json.dump({1: 2, "asd": "asd"}, file)

with open("first.json", "r+") as file:
    a = json.load(file)
    print(a)


b = json.dumps({1: 2, "123": "123", 2: [1,23,34,7]})
print(type(b))
c = json.loads(b)
print(type(c))
