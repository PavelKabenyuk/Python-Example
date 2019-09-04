# ex15

from sys import argv

script, filename = argv

text = open(filename)

print(f"Содержимое файла {filename}:\n")
print(text.read())

text.close()

print("\nСнова введите имя файла:\n")
file_again = input("> ")

text_again = open(file_again)

print(text_again.read())

text_again.close()

