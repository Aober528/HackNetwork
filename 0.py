a = 50
b = 365
for i in range(a-1):
	b *= 366 - i
c = 365 ** a
print(str((1 - (b / c)) * 100) + '%')