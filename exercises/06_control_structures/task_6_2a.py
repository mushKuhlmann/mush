# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip_address = input('введите ip address: ')
ip_address1 = ip_address.split('.')
if len(ip_address1) != 4:
    print('Неправильный IP-адрес')
else:
    octet1 = int(ip_address1[0])
    octet2 = int(ip_address1[1])
    octet3 = int(ip_address1[2])
    octet4 = int(ip_address1[3])
    if (octet1 in range(256)) and (octet2 in range(256)) and (octet3 in range(256)) and (octet4 in range(256)):
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
    else:
        print('Неправильный IP-адрес')

