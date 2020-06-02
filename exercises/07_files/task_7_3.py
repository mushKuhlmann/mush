# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
f = open('CAM_table.txt')
cam_table = f.read().rstrip().split('\n')
cam_template = '''{:<8} {:<8}       {:<8}'''
cam_table.pop(0)
cam_table.pop(0)
cam_table.pop(0)
cam_table.pop(0)
cam_table.pop(0)
cam_table.pop(0)
i = 0
len_cam_table = len(cam_table)
while i < len_cam_table:
	list_cam_table = cam_table[i]
	i +=1
	string_cam_table = list_cam_table.split()
	string_cam_table.pop(2)
	vlan = string_cam_table[0]
	mac = string_cam_table[1]
	interface = string_cam_table[2]
	print(cam_template.format(vlan, mac, interface))

