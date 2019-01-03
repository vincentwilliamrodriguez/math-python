from math import gcd

while True:
	inp=int(input("phi function of: "))

	n=1
	count=0

	while n<inp:
		if gcd(inp,n)==1:
			count+=1
		n+=1

	print(count,"\n")