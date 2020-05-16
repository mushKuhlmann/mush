# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки config список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

In [17]: config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
In [18]: config = config.strip('switchport trunk allowed vlan ')
In [19]: config.split(',')
Out[19]: ['1', '3', '10', '20', '30', '100']

