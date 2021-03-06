# *** Циклы (операторы циклов) ***

# *** Оператор цикла while ***

number = 0

# while number <= 10:
#       print(number)

    # number += 1      #   number = number + 1

    # если нами запущен бесконечный цикл то его состановить можно ctrl+c

# отступ для интерпретатора очень важен, оно говорит, что внутри чего. чтобы такого не было, не используйте пробел, используйте табуляцию Tab. Если далеко отступили, то нажимает shift+tab 

# прерывание цикла по дополнительному условию
# while number < 10:
#     if number == 5:  # Если значение number станет равной 5, 
#         break   # то вызывыаем инструкцию break, которая прерывает цикл 
#     print(number)
#     number += 1 

# оператор break выключает любой цикл. 
# закоментировать и раскоментировать строки ctr + /

# пример прерывания бесконечного цикла с использованием break

# while True: # while True - это бесконечный цикл
#     s = input("Введите команду: ")
#     print(f"Вы ввели команду: {s}")
#     if s == "стоп":
#         break


# while True: # while True - это бесконечный цикл
#     s = input("Введите команду: ")
#     print(f"Вы ввели команду: {s}")
#     if s.lower() == "стоп":  # lower - переводит буквы из верхнего регистра в нижний. то есть делает заглавные буквы прописными 
#         break


# *** Если бесконечный цикл не вырубается,
# *** то нужно нажать сочетание клавишь  "Ctrl + C"  и потом нажать Enter


# пропуск куска кода цикла 

# while True:
#     s = input("Введите слово 'YES': ")
#     if s != "YES":
#         print("Вы не ввели слово 'YES'!!! :((")
#         continue # если вызывается иснтрукция continue, то цикл возвращается в начало, то есть пропускается кусок кода который ниже расположен
#     print(f"Вы ввели команду: {s}")
#     break


# *** Оператор цикла for ***

# 1. читает элемент по порядку
# 2. присваивает значение  элемента в свою переменную
# 3. выполняет блок кода своего тела 

# for n in [1,2,3,4,5,6]:  # для каждого объекта внутри переменной n из [] - выполнить print
#     print(n) 


my_tuple = (100,200,300)

# for n in my_tuple:  
#     print(n) 

# for n in my_tuple[::-1]:  
#     print(n) 

# for n in my_tuple:  
#     if n == 200:
#         break
#     print(n) 

# for inx in range(5,10):
#     print(inx)


# for inx in range(5,20,2):
#     print(inx)

# for inx in range(5,20,2):
#     res = inx + 1
#     print(res)



# *** Генераторы списков ***  новое занятие от 08.10.2020

# создание списка с числами в диапазоне от 0 до 9
# my_list = [num for num in range(10)]

# создание списка с числами в диапазоне от 50 до 90 с шагом 10
# my_list = [num for num in range(50, 100, 10)]

# создание списка с числами в диапазоне от 0 до 9, возведенные в степень 2
# my_list = [num ** 2 for num in range(10)]

# создание списка с числами в диапазоне от 0 до 9, которые больше 5 
# my_list = [num for num in range(10) if num > 5]


# *** генератор словаря ***


# создание словаря из списка символов
# my_dict = {symbol : symbol for symbol in ["a", "b", "c"]}

# создание словаря из списка символов

list_1 = [('a', 10),('b', 20),('c', 30)] 

# my_dict = {key : val for key, val in list_1}

#  *** практическое использование цикла ***

# *** калькулятор ***


commands = {"stop", "+", "-", "*", "/"}

while True: # это бесконечный цикл

    # ввод чисел
    num_list = []
    for _ in range(2):
        num = int(input("Введите число: "))
        num_list.append(num)

    # ввод команды
    cmd = None
    while True:
        cmd = input("Введите команду: ")
        if cmd not in commands: 
            print("Вы ввели неправильную команду!!!")
            continue 
        else:
            break

    # вычисление
1

    if cmd == 'stop':
        print("До свидания!!!")
        break 
    elif cmd == "+":
        res = num_list[0] + num_list[1] 
    elif cmd == "-":
        res = num_list[0] - num_list[1]  
    elif cmd == "*":
        res = num_list[0] * num_list[1]
    elif cmd == "/":
        res = num_list[0] / num_list[1]    
    
    # вывод результата
    print(f"Результат: {res}")