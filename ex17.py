# ex17

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Копирование данных из файла {from_file} в файл {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"Исходный размер файла {len(indata)} байт")

print(f"Целевой файл существует? {exists(to_file)}")
print("Готов, нажимай клавишу Enter для продолжения или CTRL+C для отмены.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Отлично, все сделано.")

out_file.close()
in_file.close()