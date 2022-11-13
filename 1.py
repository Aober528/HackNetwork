a = 1
for i in range(50):
	a *= (365 - i)
	b = 365 ** (i + 1)
	print(i + 1, str((1 - (a / b)) * 100) + '%')