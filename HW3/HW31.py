# Задача 1
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".

while True:
    slv = input()
    if 'o' in slv.lower():
        break
    print('Write another word:')
