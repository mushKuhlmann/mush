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
i = 0
ospf_template = '''
Protocol:               {:<10}
Prefix:                 {:<10}
AD/Metric:              {:<10}
Next-Hop:               {:<10}
Last update:            {:<10}
Outbound Interface:     {:<10}
'''
len_list_ospf = len(list_ospf)
while i < (len_list_ospf - 1):
    list_ospf_new = list_ospf[i]
    i += 1
    newstring = list_ospf_new.split()
    newstring.pop(3)
    str1 = newstring[0]
    str2 = newstring[1]
    str3 = newstring[2]
    str4 = newstring[3]
    str5 = newstring[4]
    str6 = newstring[5]
    print(ospf_template.format(str1, str2, str3, str4, str5, str6))


