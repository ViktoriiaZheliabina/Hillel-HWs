# Задача 1.

# strg = 'Word {} has {} letters'
# a = input()
# res = strg.format(a, len(a))
# print(res)

# Задача 2.

print('Enter your age, please:')
a = input()
if a.isdigit() == False:
    print('Incorrect value')
else:
    if '7' in a:
        print('You are lucky today!')
    elif int(a) < 7:
        print('Where are your parents?')
    elif int(a) < 16:
        print('This is a movie for adults!')
    elif int(a) > 65:
        print('Show your pension certificate!')
    else:
        print('There are no tickets anymore!')




