ip_add = '10.20.30.20-30'
ip_add_new = ip_add.split('-')
ip_add_new_1 = ip_add_new[0].split('.')
i = int(ip_add_new_1[-1])
j = int(ip_add_new[-1])
ip_address = ip_add_new_1[0]+'.'+ip_add_new_1[1]+'.'+ip_add_new_1[2]+'.'
ip_address_list = []
for num in range(i,(j+1)):
	element = str(ip_address+'{}'.format(num))
	print(element)
