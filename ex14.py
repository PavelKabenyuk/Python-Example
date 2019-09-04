# ex14

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Привет, {user_name}, я - сценарий {script}.")
print("Я хочу задать тебе несколько вопросов.")
print(f"Я нравлюсь, {user_name}?")
likes = input(prompt)

print(f"Где ты живешь, {user_name}?")
lives = input(prompt)

print(f"На каком компьютере ты работаешь?")
computer = input(prompt)

print(f"""
Итак, ты ответил {likes} на вопрос, нравлюсь ли я тебе.
Ты живешь {lives}. Не представляю, где это.
У тебя компьютер {computer}. Прекрасно!
""")