a_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
a_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
s = int(input('Отступ шифровки: '))
print("При написании используйте только заглавные буквы")
message = input("Сообщение для шифровки: ").upper()
message1 = input("Сообщение для дешифровки: ").upper()
it = ''
ig = ''
l = input('Выберите язык RU/EU: ')
if l == 'RU':
    s = s % 33
    for i in message:
        m = a_RU.find(i)
        nm = m + s
        if i in a_RU:
            it += a_RU[nm]
        else:
            it += i
else:
    s = s % 26
    for i in message:
        m = a_EU.find(i)
        nm = m + s
        if i in a_EU:
            it += a_EU[nm]
        else:
            it += i
if l == 'RU':
    s = s % 33
    for g in message1:
        m = a_RU.find(g)
        nm = m - s
        if g in a_RU:
            ig += a_RU[nm]
        else:
            ig += g
else:
    s = s % 26
    for i in message1:
        m = a_EU.find(i)
        nm = m - s
        if i in a_EU:
            ig += a_EU[nm]
        else:
            ig += i
print(it)
print(ig)
