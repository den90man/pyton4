#1
# def my_print():
#     try:
#         time = float(input('Выработка в часах '))
#         salary = int(input('Ставка в у.е. '))
#         bonus = int(input('Премия в у.е. '))
#         res = time * salary + bonus
#         print(f'заработная плата сотрудника  {res}')
#     except ValueError:
#         return print('Not a number')
# my_print()
# #2
# m_li = [23, 35, 5, 5453, 34, 23, 3, 9]
# my_li = [el for num, el in enumerate(m_li) if m_li[num - 1] < m_li[num]]
# print(f'Исходный список {m_li}')
# print(f'Новый список {my_li}')

# 3

# n = range(20, 241)
# list = [el for el in n if el%20==0 or el%21==0]
# print(list)
# 4
# m_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# # b = [el for el in m_list if m_list.count(el)==1]
# # print(b)


#5
# from functools import reduce
# c = [el for el in range(100, 1001) if el % 2 == 0]
# def b(a, el):
#     return a * el
# print(reduce(b, c))
#6
# from itertools import count
# for el in count(int(input('Введите число '))):
#     print(el)
#     if el == 50:
#         break
# from itertools import cycle
# s = [False, 'EEQ', 'dlfkr', None]
# for el in cycle(s):
#     print(el)
#     if el==None:
#         break
