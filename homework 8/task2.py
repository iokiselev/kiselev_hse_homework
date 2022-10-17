import re

some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений'


def delete_replay(string):
    while re.findall(r'(\b\w+\b)\W*\1+', string):
        string = re.sub(r'(\b\w+\b)\W*\1+', r'\1', string)
    print(string)

delete_replay(some_string)