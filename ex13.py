# ex13

from sys import argv

script, first, second, third = argv

age = input("Сколько вам лет ?")

print("Этот сценарий называется: ", script)
print("Моя первая переменная называется: ", first)
print("Моя вторая переменная называется: ", second)
print("Моя третья переменная называется: ", third)

print(f"Еще вам: {age} лет")