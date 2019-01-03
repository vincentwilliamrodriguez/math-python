def modexp(base,exp,mod):
	res=base%mod
	for i in range(exp-1):
		res=(res*base)%mod
	return res

while True:
	b=int(input("base: "))
	e=int(input("exponent: "))
	m=int(input("mod: "))

	print(modexp(b,e,m),"\n")