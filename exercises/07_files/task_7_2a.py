# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

f = open('config_sw1.txt')
k = len(ignore)
for line in f:
	if line.startswith('!') == False:
		if (ignore[0] not in line) and (ignore[1] not in line) and (ignore[2] not in line):	
		 print(line)

