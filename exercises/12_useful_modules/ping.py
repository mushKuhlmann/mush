import subprocess
''' stdout=subprocess.DEVNULL - позволяет  не выводить сам процесс пинга на экран, дальнейший IF помогает понять успешен ли пинг
stdout = subprocess.PIPE, stderr=subprocess.PIPE - выводит на экран, .decode('utf-8') - декодирует'''
ip_address = str(input('Введите ip адрес: ', ))
def ping_ip(ip_address):
	result =  subprocess.run(['ping', '-c', '3', ip_address],stdout = subprocess.PIPE, stderr=subprocess.PIPE)
	if result.returncode == 0:
		return True, result.stdout.decode('utf-8')
	else:
		return False, result.stderr.decode('utf-8')

print(ping_ip(ip_address))
