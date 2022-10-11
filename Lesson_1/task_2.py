'''Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.'''



import re
def byte_code(*args):
    str_list = [*args]

    for i in str_list:
        print(type(eval(f"b'{i}'")), i, len(i))


byte_code('class', 'function', 'method')
print('=' * 30)
byte_code('spam', 'eggs', 'pam')