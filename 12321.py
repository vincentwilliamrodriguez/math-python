def count(no,ind):
	global res

	if ind==20:
		res+=1
	else:
		if no+1<8:
			count(no+1,ind+1)
		if no-1>0:
			count(no-1,ind+1)

res=0
for i in range(7):
	count(i+1,1)

print(res)

while True:
	a=1