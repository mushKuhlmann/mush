def read_file (file):
	f = open(file)
	string_file = f.read().lstrip().rstrip().split('\n')
	return string_file

#print(read_file('sh_cdp_n_sw1.txt'))
