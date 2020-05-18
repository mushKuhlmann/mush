# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


network = raw_input('Введите ip адрес и маску подсети: ')

network = network.split('/')
ip, mask = network
ip1 = ip.split('.')
oct1, oct2, oct3, oct4 = ip1
oct1 = int(oct1)
oct2 = int(oct2)
oct3 = int(oct3)
oct4 = int(oct4)
mask = int(mask)
ip_template = '''
Network:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
'''
print(ip_template.format(oct1, oct2, oct3, oct4, oct1, oct2, oct3, oct4))
