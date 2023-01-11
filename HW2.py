# Задача 1.

strg = 'Word {} has {} letters'
a = input()
res = strg.format(a, len(a))
print(res)

# Задача 2.

print('Enter your age, please:')
a = input()
if not a.isdigit():
    print('Incorrect value')
else:
    ia = int(a)
    if '7' in a:
        print('You are lucky today!')
    elif ia < 7:
        print('Where are your parents?')
    elif ia < 16:
        print('This is a movie for adults!')
    elif ia > 65:
        print('Show your pension certificate!')
    else:
        print('There are no tickets anymore!')




