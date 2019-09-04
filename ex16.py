# ex16

from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename}")
print("Если вы не хотите стирать его, нажмите сочитание CTRL+C (^C).")
print("Если хотите стареть файл, нажмите клавишу Enter.")

input("?")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла. До свидания!")

print("Теперь я запрашиваю три строки.")

line1 = input("Строка 1: ")
line2 = input("Строка 2: ")
line3 = input("Строка 3: ")

print("Это я запишу в файл.")

target.write("{}\n{}\n{}\n".format(line1,line2,line3))

print("И наконец, я закрою файл.")
target.close()