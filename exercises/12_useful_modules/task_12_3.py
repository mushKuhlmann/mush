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
1.создаем таблицу с заголовками 'Reachable', 'Unreachable' с помощью модуля  prettytable.
2.тк по заданию нельзя изменять списки,которые приходят как аргументы, то использем функцию sorted, которая отсортирует входящие списки  и выдаст НОВЫЕ СПИСКИ, которые мы будем изменять.
3. вычислим длину каждого списка. если один из списков короче , то добавим в конец списка пустой элемент '' до тех пор, пока длина обоих списков будет одинакова( с помощью цикла while).
4.когда оба списка равны по длине, добавим элементы списка в таблицу построчно с помощью цикла for
'''

ip_list1 = ['10.1.1.1', '10.1.1.2', '10.1.1.10', '10.1.1.20']
ip_list2 = ['1.1.1.1','10.1.1.7']
from prettytable import PrettyTable
def print_ip_table(reachable, unreachable):
	table = PrettyTable(['Reachable', 'Unreachable'])
	k = 0
	lenght = abs(len(unreachable) - len(reachable))
	unreachable_use = sorted(unreachable)
	reachable_use = sorted(reachable)
	if len(reachable) < len(unreachable):
		while k != lenght:
			reachable_use.append('')
			k = k + 1
	elif len(reachable) > len(unreachable):
		while k != lenght:
			unreachable_use.append('')
			k = k + 1
	for i in range(len(reachable_use)):
		table.add_row([reachable_use[i],unreachable_use[i]])
	return table
print(print_ip_table(['10.1.1.1', '10.1.1.2'], ['10.1.1.7','10.1.1.8', '10.1.1.9']))
#print(print_ip_table(ip_list1, ip_list2))
#print(ip_list1, ip_list2)
