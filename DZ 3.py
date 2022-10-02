# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# number = int(input('Введите размер списка '))
# list = []
# sum = 0
# for i in range(number):
#     list_number = int(input(f'Введите число {i+1} '))
#     list.append(list_number)
#     if i % 2 != 0:
#         sum += list[i]

# print(list)
# print(f'Сумма нечетных чисел равна {sum}')



# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: 
# [2, 3, 4, 5, 6] => [12, 15, 16]; 
# [2, 3, 5, 6] => [12, 15]

# from random import randint


# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#    list.append(randint(0, 9))

# for i in range(len(list)):
#    while i < len(list)/2 and number > len(list)/2:
#        number = number - 1
#        a = list[i] * list[number]
#        list2.append(a)
#        i += 1

# print(list)
# print(list2)



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# fib = int(input('5# введите число for fib = '))
# res_5 = []
# for i in range(fib+1):
#    if i==0:
#         res_5.append(i)
#     elif i==1:
#         res_5.append(i)
#         res_5.insert(0, i)
#     else:
#         res_5.append(res_5[len(res_5)-1]+res_5[len(res_5)-2])
#         res_5.insert(0, (-1)**(i-1)*res_5[len(res_5)-1])
# print(res_5)