# ex18

def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_tow_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
	print(f"arg1: {arg1}")

def print_none():
	print("Аргументов нет")

print_two("Михаил", "Райтман")
print_tow_again("Михаил", "Райтман")
print_one("Привет")
print_none()
