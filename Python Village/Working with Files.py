f = open('input.txt', 'r')
c = open('output.txt', 'w')

i = 0
while i < 1000:
	if i % 2 == 1:
		c.write(f.readline())
	else:
		print(f.readline())
	i = i + 1

f.close()
c.close()
