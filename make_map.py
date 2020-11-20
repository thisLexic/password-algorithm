"""
generates the mapping between a hexadecimal of length two to a alphanumeric character
"""

lstr = "0123456789abcdef"
hex = []
for char in lstr:
	hex.append(char)

alphnumstr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789--"
alphanum = []
for char in alphnumstr:
	alphanum.append(char)
	
alphanumindex = 0

map = {}
count = 0
for h1 in hex:
	for h2 in hex:
		if count == 4:
			alphanumindex += 1
			count = 0
		map[h1 + h2] = alphanum[alphanumindex]
		count += 1
		
map['f8'] = "d"		
map['f9'] = "y"		
map['fa'] = "s"		
map['fb'] = "l"		
map['fc'] = "e"		
map['fd'] = "x"		
map['fe'] = "i"
map['ff'] = "c"

print(map)