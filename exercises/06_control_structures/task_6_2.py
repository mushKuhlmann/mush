# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_address = input('введите ip address: ')
ip_address1 = ip_address.split('.')
octet1 = int(ip_address1[0])
if 1 <= octet1 <= 223:
    print('unicast')
elif 224 <= octet1 <= 239:
    print('multicast')
elif ip_address == '255.255.255.255':
    print('local broadcast')
elif ip_address == '0.0.0.0':
    print('unassigned')
else:
    print('unused')

