'''Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''

import locale

from chardet import detect

f = open('test.txt', 'w', encoding='utf-8')
f.write('тест тест тест')
f.close()

'''узнаем кодировку файла'''
with open('test.txt', 'rb') as f:
    content = f.read()

encoding = detect(content)['encoding']
print('encoding: ', encoding)

'''Читаем из файла'''
with open('test.txt', 'r', encoding=encoding) as f:
    for i in f:
        print(i, end='')
    f.seek(0)