'''Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.'''

words = ['attribute', 'класс', 'функция', 'type']

for el in words:
    try:
        print(f'{el.encode("ascii")} - Возможно записать в байтовом типе')
    except:
        print(f'{el} - Невозможно записать в байтовом типе')