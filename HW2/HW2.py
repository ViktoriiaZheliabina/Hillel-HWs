# Задача 1.

# Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters",
# наприклад "Word 'Python' has 6 letters". Для отримання слова для аналізу скористайтеся
# константою або функцією input().

strg = 'Word {} has {} letters'
slv = input()
res = strg.format(slv, len(slv))
print(res)

# Задача 2.

# Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свій вік
# (можно використати константу або функцію input(), на екран має бути виведено лише одне повідомлення,
# також подумайте над варіантами, коли введені невірні дані).
#           якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
#           якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
#           якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
#           якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
#           у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"

print('Enter your age, please:')
age = input()
if age.isdigit():
    iage = int(age)
    if '7' in age:
        print('You are lucky today!')
    elif iage < 7:
        print('Where are your parents?')
    elif iage < 16:
        print('This is a movie for adults!')
    elif iage > 65:
        print('Show your pension certificate!')
    else:
        print('There are no tickets anymore!')
else:
    print('Incorrect value')




