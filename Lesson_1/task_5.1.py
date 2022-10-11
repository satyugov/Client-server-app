'''Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
'''
import chardet
import subprocess
import platform


# def ping_res(*args):
urls = ['yandex.ru', 'youtube.ru']
param = '-n' if platform.system().lower() == 'windows' else '-c'

for url in urls:
    args = ['ping', param, '2', url]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

# ping_res('ping', param, '2', 'yandex.ru')