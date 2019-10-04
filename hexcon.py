#dechexbin.py jb
def hexcon(num):
	key = "-1234567890abcdef" # hex key
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = key[h16]+ key(h1)
	return h
	
def main():
	hs = ""
	for  i in range(9,10):
		hs = hexcon(i)
		print(i,hs)

main()
