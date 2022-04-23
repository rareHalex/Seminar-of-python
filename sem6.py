# 6
"""
Декораторы и паттерны питона
"""


#1 удаление пробелов у , у заменять --
import functools
import sre_parse
import re


def dicorator(f): # не вмешиваясь в код огромной программы функции изменяем ее отдельно т е не мешаем код
    def wrapper_d():
        s = f()
        s = re.sub(r'\s+([\,\.\:\!\?])', r'\1', s) # \s+ - любой проебльный символ () - группирующие скобки заменяем все что нашли на то что в скобках [] - любой сивол из этих
        s = s.replace('--', '-')
        return s
    wrapper_d.old_f = f # к функции всегда можно обавить новый метод так
    print('decoretor 1')
    return wrapper_d

def decorator_2(f):
    def wrapper_d():
        s = f()
        s = re.sub(r'\s+', r' ', s)
        return s
    wrapper_d.old_f = f
    print('decorator 2')
    return wrapper_d

@dicorator # автоматички декоратирует
@decorator_2 # выполниться первее чем декоратор 1
def my_func():
    return """   -- Я думаю, -- сказал князб улыбаясь, -- что ежели
     вместо нашего милого Винц , вы бы взяли приступом согласия
     короля.Вы так красноречивы.Дадите чаю?"""
#print(dicorator(my_func)())
#my_func = dicorator(my_func)
print(my_func())
# декоратор сохраняет старую функцию
print(my_func.old_f())

#-----------------------------------------------------------------------------------------------------------------------
#защита сайта от парссинга построим декоратор сокрытия данных

def encrypt(s):
    new_s = bytes(s, encoding='utf8')
    ans = ' '
    for i in new_s:
        ans += hex(i)
    return ans.replace('0x','%').upper()

# тож самое ток декоратор
def decorator_bytes(function):
    def wraper():
        s = function()
        return encrypt(function(s))
    return wraper

@decorator_bytes
def function(string):
    return string

#print(encrypt('abcd'))
print(function("абв"))
