# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess
#ip = ['8.8.8.8', '192.183.1.1', '8.8.4.4']
result_well = []
result_bad = []
def ping_ip_addresses(ip_address):
	for ip in ip_address:
		ping =  subprocess.run(['ping', '-c', '1', ip],stdout=subprocess.DEVNULL)
		if ping.returncode == 0:
			result_well.append(ip)
		else:
			result_bad.append(ip)
	return result_well, result_bad
print(ping_ip_addresses(['8.8.8.8', '192.183.1.1', '8.8.4.4']))
