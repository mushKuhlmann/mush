# -*- coding: utf-8 -*-
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
In [3]: mac = 'AAAA:BBBB:CCCC'
In [5]: mac.replace(':','.')
Out[5]: 'AAAA.BBBB.CCCC'

