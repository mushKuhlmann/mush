# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''
'''
from tabulate import tabulate
columns = ['Reachable', 'Unreachable']
tabl = [('8.8.8.8','1.1.1.1'), ('9.9.9.9','')]
print(tabulate(tabl, headers = columns))
'''
ip_list1 = ['10.1.1.1', '10.1.1.2', '10.1.1.10', '10.1.1.20']
ip_list2 = ['1.1.1.1','10.1.1.7']
from prettytable import PrettyTable
def print_ip_table(reachable, unreachable):
	table = PrettyTable(['Reachable', 'Unreachable'])
	k = 0
	lenght = abs(len(unreachable) - len(reachable))
	if len(reachable) < len(unreachable):
		while k != lenght:
			reachable.append('')
			k = k + 1
	elif len(reachable) > len(unreachable):
		while k != lenght:
			unreachable.append('')
			k = k + 1
	else:
		pass
	for i in range(len(reachable)):
		table.add_row([reachable[i],unreachable[i]])
	if '' in reachable:
		k = 0
		while k != lenght:
			reachable.remove('')
			k = k + 1
	elif '' in unreachable:
		k = 0
		while k != lenght:
			unreachable.remove('')
			k = k + 1
	return table
#print(print_ip_table(['10.1.1.1', '10.1.1.2'], ['10.1.1.7','10.1.1.8', '10.1.1.9']))
print(print_ip_table(ip_list1, ip_list2))
print(ip_list1, ip_list2)
