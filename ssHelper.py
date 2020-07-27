
def get_data(fileName):
    f = open(fileName,'r')
    lines = f.readlines()
    f.close()
    return lines

def get_symbols(lines):
	symbols = []
	for line in lines:
		if "  Code  " in lines:
			symbols.append(line)
		elif "  Data  " in line:
			symbols.append(line)
		else:
			symbols.append('Empty')
	return symbols

def clean_address(address):
	address = address.replace("'","")
	address = address.replace(" ","")

	if len(address) == 7: 
		address = address.replace("0x","000")
	elif len(address) == 10: 
		address = address.replace("0x","")
	else:
		address = address.replace("0x","0000")

	return address
		
def clean_data(lines,symbols):
	
	clean_symbols = []
	strings = ''
	clean_string = ''
	address = ''
	info = ''
	entry = ''

	for c in range(len(symbols)):
		strings = symbols[c].split(' ')
		new_string = [x for x in strings if x]
		print(c,new_string)
		if len(new_string) == 6:
			address = clean_address(new_string[0])
			entry = lines[c-1].replace("\n","")
			info = new_string[len(new_string)-5] + " " + new_string[len(new_string)-4] + " " + new_string[len(new_string)-3] + " " + new_string[len(new_string)-2] + " " + new_string[len(new_string)-1]
			clean_string = address + "\t" + entry + "\t" + info + "\n"
			#print("6 items, ADDRESS,ENTRY,INFO: ",address,',',entry,',',info) 
			clean_symbols.append(clean_string)
			print(clean_symbols[len(clean_symbols)-1])
		elif len(new_string) == 7:
			address = clean_address(new_string[1])
			entry = new_string[0]
			info = new_string[len(new_string)-5] + " " + new_string[len(new_string)-4] + " " + new_string[len(new_string)-3] + " " + new_string[len(new_string)-2] + " " + new_string[len(new_string)-1]
			clean_string = address + "\t" + entry + "\t" + info + "\n"
			#print("ADDRESS,ENTRY,INFO: ",address,',',entry,',',info) 
			clean_symbols.append(clean_string)
			print(clean_symbols[len(clean_symbols)-1])
		else: 
			info = ''
			print("HIT ELSE\n")

		
	return clean_symbols

def sort_data(clean_symbols):
	sorted_symbols = clean_symbols.sort()
	for x in sorted_symbols: print(x)
	return sorted_symbols