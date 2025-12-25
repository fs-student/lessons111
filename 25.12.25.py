# a = True
# if a:
#     print(123)
# else:
#     print(456)
# значение if  условие else 345
# print(123 if a else 456)
# a = True
# #пока условие
# while a:
#     print("+")
from itertools import count

# num = 0
# is_running = True
# while is_running:
#     if num  < 10:
#         num += 1
#         print(num)
#     else:
#          break # завершение цикла
#     print("programme is over")

# num = 11
# while num > 0:
#     num -= 1
#     if num % 2 != 0:
#          continue
#     print(num)

# a = [1,2,3,4,5,6]
# i = 0
# while i < 5:
#     print(a[i])
#     i += 1

# a = int(input("Введите число:"))
# count = 0
# if a != 0:
#     while a != 0:
#         b = a % 10
#         print(b)
#         count+=1
#         a = a // 10
#         print(a)
# else:
#     count = 1
# print(count)
#
# a = int(input("Введите число:"))
# counter = 0
# while a != 0:
#     b = a % 10
#     summ += b
#     a = a // 10
# print(summ)
# a = 0
# s = True
# while a <= 10:
#     a += 1
#     if a ** 2 > 50:
#       s = False
#       break
#     print(a ** 2)
# if s:
# #     print("Все квадраты меньше 50")
# a = 0
# s = True
# while a <= 15:
#     print(a)
#     a += 1
#     if a == 10:
#         s = False
#         break
# if s:
#     print("Цикл завершен")
a = int(input())
i = 0
while i < 10:
    i += 1
    print(a,"*",i,"=",a*i)






