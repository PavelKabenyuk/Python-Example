# ex 21

def add(a, b):
	print(f"СЛОЖЕНИЕ {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"ВЫЧИТАНИЕ {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"УМНОЖЕНИЕ {a} * {b}")
	return a * b

def devide(a, b):
	print(f"ДЕЛЕНИЕ {a} / {b}")
	return a / b

print("Давайте выполним несколько вычислений с помощью функций!")

age = add(30, 5)
height = subtract(190, 4)
weight = multiply(35, 2)
iq = devide(250, 2)

print(f"Возраст: {age}, Рост: {height}, Вес: {weight}, IQ: {iq}")

print("Это головоломка.")

what = add(age, subtract(height, multiply(weight, devide(iq, 2))))

print("Получается", what, "Выможете вычислить вручную ?")