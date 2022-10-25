"""
Лаба № 3
Выполнил Кодочигов Денис Андреевич
"""

a_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 2
a_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' * 2

# Ввод базы алфавитов
print("При вводе используйте только целые числа")

while True:
    try:
        # пробуем получить число
        s = int(input('Отступ шифровки: '))

    except TypeError as e:
        # обработка ошибки
        print("При вводе используйте только целые числа")
        print(e)

    else:
        # если всё корректно то нужно закончить цикл
        break


print("При написании используйте только заглавные буквы")
message_cipher = input("Сообщение для шифровки: ").upper()
message_decipher = input("Сообщение для дешифровки: ").upper()

# Ввод отступа, сообщений для шифровки или дешифровки
it = ''
ig = ''

# Ввод переменных для вывода зашифрованых и дешифрованых сообщений
while True:
    l = input('Выберите язык RU/EU: ')

    if l is "RU" or l is "EU":
        break

    print("Неизвестный язык, выберите либо RU либо EU")

a_selected = a_RU if l == "RU" else a_EU
s = s % (33 if l == "RU" else 26)

for i in message_cipher:
    m = a_selected.find(i)
    nm = m + s
    if i in a_selected:
        it += a_selected[nm]
    else:
        it += i

for i in message_decipher:
    m = a_selected.find(i)
    nm = m - s

    if i in a_selected:
        ig += a_selected[nm]

    else:
        ig += i

# Выбран английский язык происхдит шифровка(буква находится в алфавите, а после вычитается введённый отступ
print(it)
print(ig)
