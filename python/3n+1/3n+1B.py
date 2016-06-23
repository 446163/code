m = 0
n = 1
while 1:
	temp = []
	#print(n)
	n=n+1
	t=n
	while t != 1:
		if t % 2 == 0:
			t=int(t/2)
			temp.append(t)
		else:
			t=(3*t)+1
			temp.append(t)
	if len(temp) > m:
		m=len(temp)
		print(str(n) + " : " + str(m))
		#print(temp)
	#print(n)



