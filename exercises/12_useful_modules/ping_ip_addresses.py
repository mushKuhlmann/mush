import subprocess
''' stdout=subprocess.DEVNULL - позволяет  не выводить сам процесс пинга на экран, дальнейший IF помогает понять успешен ли пинг
stdout = subprocess.PIPE, stderr=subprocess.PIPE - выводит на экран, .decode('utf-8') - декодирует'''
#ip_address = str(input('Введите ip адрес: ', ))
ip_address = ['8.8.8.8', '192.183.1.1']
result_well = []
result_bad = []
def ping_ip_addresses(*ip_address):
	for ip in ip_address:
		ping =  subprocess.run(['ping', '-c', '3', ip],stdout=subprocess.DEVNULL)
		if ping.returncode == 0:
			result_well.append(ip)
#			return tuple(result_well)
			print( 'хорошо', tuple(result_well))
		else:
			result_bad.append(ip)
			print('плохо', tuple(result_bad))

ping_ip_addresses(*ip_address)
