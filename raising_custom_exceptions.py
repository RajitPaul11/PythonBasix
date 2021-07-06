def increment(num):
	try:
		return int(num)+1
	except:
		raise ValueError

a = increment('fdf')
print(a)
