# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''



def get_int_vlan_map(config_filename):
	f = open(config_filename)
	list_config_filename = f.read().rstrip().split('\n')
	dict_trunk = {}
	dict_access = {}
	for element in list_config_filename:
		if element.startswith('interface FastEthernet'):
			index_element = list_config_filename.index(element)
			if list_config_filename[(index_element + 1)] == ' switchport trunk encapsulation dot1q':
				vlan1 = list_config_filename[(index_element + 2)].strip(' switchport trunk allowed vlan ')
				dict_trunk[element] = vlan1
			elif list_config_filename[(index_element + 1)] == ' switchport mode access':
				if ' switchport access vlan' in (list_config_filename[(index_element + 2)]):
					vlan2 = list_config_filename[(index_element + 2)].strip(' switchport access vlan ')
					dict_access[element] = vlan2
				else:
					dict_access[element] = 'VLAN 1'
	tuple_vlan = ('{}'.format(dict_trunk), '{}'.format(dict_access))
	print('\nРЕЗУЛЬТАТ: ', tuple_vlan)
get_int_vlan_map('config_sw2.txt')
