# ex32

the_count = [1, 2, 3, 4, 5]
fruits = ['яблоко', 'апельсин', 'персик', 'абрикос']
change = [1, 'червонец', 2, 'плотинник', 3, 'сотня']

for number in the_count:
	print(f"Счетсик {number}")

for i in change:
	print(f"Я получил {i}")

elements = []

for i in range(0, 6):
	print(f"Добавление {i} в список.")
	elements.append(i)

for i in elements:
	print(f"Номер элемента: {i}")

