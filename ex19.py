# ex 19

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"У нас есть {cheese_count} сырков!")
	print(f"У нас есть {boxes_of_crackers} пачек чипсов!")
	print("Это достаточно для вечеринки!")
	print("Погнали\n")

print("Мы можем непосредственно передать числа в функции:")
cheese_and_crackers(20, 30)

print("ИЛИ, можно использовать переменные из нашего сценария:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Мы даже можем выполнить вычисления в нутри функции:")
cheese_and_crackers(10 + 20, 5 + 6)

print("И объеденить переменные с вычислениями:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)