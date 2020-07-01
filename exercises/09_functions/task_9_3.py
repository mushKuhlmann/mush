# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
	f = open(config_filename)
	list_config_filename = f.read().rstrip().split('\n')
	list_trunk = []
	list_access = []
	list_vlan = []
	dict_trunk = {}
	dict_access = {}
	index_element = 0
	for element in list_config_filename:
		if element.startswith('interface FastEthernet'):
			index_element = list_config_filename.index(element)
			if list_config_filename[(index_element + 1)] == ' switchport trunk encapsulation dot1q':
				#list_trunk.append(element)
				vlan1 = list_config_filename[(index_element + 2)].strip(' switchport trunk allowed vlan ')
				#list_vlan.append(vlan)
				dict_trunk[element] = vlan1
				#dict_trunk.update(element = vlan)
			elif list_config_filename[(index_element + 1)] == ' switchport mode access':
				vlan2 = list_config_filename[(index_element + 2)].strip(' switchport access vlan ')
				dict_access[element] = vlan2
	print('словарь портов в режиме trunk \n', dict_trunk)
	print('словарь портов в режиме access \n', dict_access)

get_int_vlan_map('config_sw1.txt')
