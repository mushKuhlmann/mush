# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
f = open('ospf.txt')
list_ospf = f.read().split('\n')
list_ospf0 = list_ospf[0]
list_ospf1 = list_ospf[1]
list_ospf2 = list_ospf[2]
list_ospf3 = list_ospf[3]
list_ospf4 = list_ospf[4]
list_ospf5 = list_ospf[5]
list_ospf6 = list_ospf[6]
list_ospf7 = list_ospf[7]

newstring0 = list_ospf0.split()
str1 = newstring0[0]
str2 = newstring0[1]
str3 = newstring0[2]
str4 = newstring0[4]
str5 = newstring0[5]
str6 = newstring0[6]

ospf_template = '''
Protocol:               {:<10}
Prefix:                 {:<10}
AD/Metric:              {:<10}
Next-Hop:               {:<10}
Last update:            {:<10}
Outbound Interface:     {:<10}
'''

print(ospf_template.format(str1, str2, str3, str4, str5, str6))


