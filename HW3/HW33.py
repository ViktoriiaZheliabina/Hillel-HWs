# Задача 3.

# Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на "о"
# (враховуються як великі так і маленькі).

print('Enter the text, please:')
str1 = input()
str2 = str1.split()
dl = len(str2)
qnt = 0
for i in range(dl):
    if str2[i][-1] == 'o' or str2[i][-1] == 'O':
        qnt += 1
print(qnt)

