# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_address = input('введите ip address: ')
ip_address_correct = False
while not ip_address_correct:
    ip_address1 = ip_address.split('.')
    if len(ip_address1) != 4:
        print('Неправильный IP-адрес')
        ip_address = input('\n введите еще раз: ')
    else:
        octet1 = int(ip_address1[0])
        octet2 = int(ip_address1[1])
        octet3 = int(ip_address1[2])
        octet4 = int(ip_address1[3])
        if (octet1 in range(256)) and (octet2 in range(256)) and (octet3 in range(256)) and (octet4 in range(256)):
            if 1 <= octet1 <= 223:
                print('unicast')
                ip_address_correct = True
            elif 224 <= octet1 <= 239:
                print('multicast')
                ip_address_correct = True
            elif ip_address == '255.255.255.255':
                print('local broadcast')
                ip_address_correct = True
            elif ip_address == '0.0.0.0':
                print('unassigned')
                ip_address_correct = True
            else:
                print('unused')
                ip_address_correct = True
        else:
             print('Неправильный IP-адрес')
             ip_address = input('\n введите еще раз: ')

