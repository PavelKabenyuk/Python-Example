# v1
from colorama import Fore, Back, Style

# functions
def plus(a, b):
	print(f"Сложение: {a} + {b}")
	return a + b

def minus(a, b):
	print(f"Вычитание: {a} - {b}")
	return a - b

def multiplication(a, b):
	print(f"Умножение: {a} * {b}")
	return a * b

def division(a, b):
	print(f"Деление: {a} / {b}")
	return a / b

# user input
print(Back.YELLOW)
do = input("Выберите действие (+, -, *, /): ")

print(Fore.WHITE)
print(Back.BLUE)
a = float( input("Первое число: ") )
b = float( input("Второе число: ") )

print(Fore.BLACK)
print(Back.YELLOW)
if do == '+':
	make = plus(a, b)
	print(make)
elif do == '-':
	make = minus(a, b)
	print(make)
elif do == '*':
	make = multiplication(a, b)
	print(make)
elif do == '/':
	make = division(a, b)
	print(make)
else:
	print(Fore.WHITE)
	print(Back.RED)
	print('Не верное действие')

