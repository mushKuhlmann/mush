while  True:
    ip_address = input('введите ip address: ')
    ip_address1 = ip_address.split('.')
    if len(ip_address1) != 4:
        print('Неправильный IP-адрес')
        continue
    else:
        octet1 = int(ip_address1[0])
        octet2 = int(ip_address1[1])
        octet3 = int(ip_address1[2])
        octet4 = int(ip_address1[3])
        if (octet1 in range(256)) and (octet2 in range(256)) and (octet3 in range(256)) and (octet4 in range(256)):
            if 1 <= octet1 <= 223:
                print('unicast')
                break
            elif 224 <= octet1 <= 239:
                print('multicast')
                break
            elif ip_address == '255.255.255.255':
                print('local broadcast')
                break
            elif ip_address == '0.0.0.0':
                print('unassigned')
                break
            else:
                print('unused')
                break
        else:
            print('Неправильный IP-адрес')
            continue

