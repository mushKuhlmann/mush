# -*- coding: utf-8 -*-
'''
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

'''
import re
def parse_sh_ip_int_br(config_filename):
	regex = r'(\S+)\s+(\d+.\d+.\d+.\d+|unassigned)\s+YES (manual|unset\s)\s(up|down|\S+ down)\s+(up|down)'
	find_list = []
	f = open(config_filename)
	for line in f:
		find = re.search(regex, line)
		if find:
			find_list.append(find.group(1 , 2 , 4, 5))

	return find_list
print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
