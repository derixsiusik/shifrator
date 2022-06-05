import requests
import random
import turtle
import telebot

class Human:
    pass

class Employee(Human):
    pass

class Worker(Employee):
    pass


h = Human()
if random.randint(0, 1) == 0:
    h.name = '1'

h.w = 12
e = Employee()
w = Worker()


if hasattr(h, "name"):
    print(getattr(h, "name"))

isinstance()
issubclass()
hasattr()

dir()
help()