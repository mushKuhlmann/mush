# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import module11
def parse_cdp_neighbors (command_output):
	list_file = module11.read_file(command_output)
	equipment = list_file[0].strip('>show cdp neighbors')
	list_file.pop(0)
	list_file.pop(0)
	list_file.pop(0)
	list_file.pop(0)
	list_file.pop(0)
	list_file.pop(0)
	device_id = []
	local_interface = []
	port_id = []
	local_interface_string = ''
	port_id_string = ''
	for line in list_file:
		list_line = line.split()
		device_id.insert((len(list_file)-1), list_line[0])
		local_interface_string = list_line[1]+list_line[2]
		local_interface.insert((len(list_file)-1),local_interface_string)
		port_id_string = list_line[8]+list_line[9]
		port_id.insert((len(list_file)-1), port_id_string)
	int_tuple = ()
	cdp_dict = {}
	neighbor_list = list(zip(device_id, port_id))
	for interface in local_interface:
		int_tuple = (equipment, interface)
		cdp_dict[int_tuple] = ''
	cdp_dict_end = dict(zip(cdp_dict, neighbor_list))
	return cdp_dict_end

print(parse_cdp_neighbors('sh_cdp_n_sw1.txt'))
