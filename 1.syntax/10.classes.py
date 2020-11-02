# до этого было 131 строка на предыдущем уроке

# *** Полиморфизм *** - оставшиеся три принципа объектно - ориентированного программирования. Посмотрели до этого наследование - этот урок я пропустил. 
# поли + морф = разные формы чего-то одного

# 1 вид полиморфизма - методы у разных классов переопределяются,
# т.е. методы имеют одинаковое название, но могут иметь различные поведения
# родительский класс 

# class A:
#     """
#     docstring
#     """
#     def func(self, arg):
#         """
#         docstring
#         """
#         res = arg * 2
#         print(f"Данные: {res}")


# # дочерний класс, у которого метод переопределен  

# class A_1(A):
#     """
#     docstring
#     """
#     def func(self, arg):
#         res = arg ** 3
#         print(f"Result: {res}")


# # экземпляры классов

# a = A()
# a_1 = A_1()

# вызов методв с одинаковым названием, но с разным поведением 
# a.func(10)
# a_1.func(10)

# 2 вид полиморфизма - применение "магических" методов (методы перегрузки операторов)

# метод, который делает из экземпляра класса функцию

# class Sum(object):
#     """
#     docstring
#     """
#     def __init__(self, param):
#         self.coeff = param


#     def __call__(self, a, b):
#         res = (a + b) * self.coeff
#         print(f"Result: {res}")

#     def __str__(self): 
#         return f"Sum {self.coeff}"




# s_1 = Sum(0.5)
# s_2 = Sum(3.14)

# объект ведет себя как функция
# s_1(10,20)
# s_2(10,20)

# объект при передаче в функцию print возвращает строку
# print(s_1)

# **** Инкапсуляция ****
# инкапсуляция - скрытие атрибутов или методов (обычно применяемых только внутри класса )



# # инкапсуляция не строгая
# class B: 
#     def __init__(self, arg):
#         self._attr = arg

#     def _method(self):
#         print("Hello!")


# b = B(100)

# # print(b._attr)
# # b._method()


# # инкапсуляция  строгая
# class C:
#     def __init__(self, arg):
#         self.__attr = arg

#     def method_2(self):
#         return self.__attr

#     def __method(self):
#         print("Hello!")

# c = C(200)
# c._C__method()

# print(c.method_2())



# **** Композиция (Агрегация?) ****
# использование экземпляров одного класса внутри другого 


class D:
    def __call__(self, a):
        return a ** 2 

class E: 
    def m(self, b):
        d = D() # создается объект класса D
        res = b + 2 
        return d(res) # используется объект класса D в качестве функции

e = E()

res = e.m(10)
# print(res)

# статический метод , метод класса 

class Person:
    counter = 0
    def __init__(self, name, age):
        self.__n = name
        self.__a = age
        Person.counter += 1
        self.id = Person.counter


    # метод экземпляра
    def info(self):
        print(f"Name: {self.__n}, Age: {self.__a}")

# метод класса
@classmethod
def count_control(cls):
    cls.counter += 1



# статический метод
@staticmethod
def method(x, y):
    print(f"Res: {x + y}")


john = Person("John", 20)
john.info()
# john.count_control()


bob = Person('Bob', 35)
bob.info()


bob.method(10, 20)
Person.method(10, 20)