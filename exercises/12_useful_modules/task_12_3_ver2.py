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
2.вычисляем максимальную длину списков lenght_max, по ней будет счетчик итераций в цикле for. формируем с помощью цикла for таблицу построчно
3. если вылезет ошибка IndexError(проще говоря если один список будет короче другого), то выполняем код в блоке  except.
4. если список reachable короче, то добавляем в таблицу пустую строку вместо элемента из списка  reachable (СПИСОК ПРИ ЭТО ОСТАЕТСЯ НЕИЗМЕННЫМ), пустую строку добавляем столько раз, скольки равна разница в длине между списками difference.
5. аналогично поступаем, если список unreachable короче
6. в блоке else описываем что нужно сделать, если оба списка одинаковы по длине: вернуть готовую таблицу
'''

ip_list1 = ['10.1.1.1', '10.1.1.2', '10.1.1.10', '10.1.1.20']
ip_list2 = ['1.1.1.1','10.1.1.7']
from prettytable import PrettyTable
def print_ip_table(reachable, unreachable):
	table = PrettyTable(['Reachable', 'Unreachable'])
	k = 0
	difference = abs(len(unreachable) - len(reachable))
	lenght_max = max(len(reachable) , len(unreachable))
	try:
		for i in range(lenght_max):
			table.add_row([reachable[i], unreachable[i]])
	except IndexError:
		if len(reachable) < len(unreachable):
			while k != difference:
				table.add_row(['', unreachable[i]])
				k = k + 1
				i = i + 1
		elif len(reachable) > len(unreachable):
			while k != difference:
				table.add_row([reachable[i], ''])
				k = k + 1
				i = i + 1
		return table
	else:
		return table
print(print_ip_table(['10.1.1.1', '10.1.1.2'], ['10.1.1.7','10.1.1.8', '10.1.1.9', '10.1.1.99']))
#print(print_ip_table(ip_list1, ip_list2))
#print(ip_list1, ip_list2)
