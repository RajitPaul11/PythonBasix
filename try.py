while True:
	a = input("Enter a number of your choice or press q to quit this game: ")
	if a == 'q':
		break
	try:
		a=int(a)
		if a>6:
			print(f"Entered value is greater than 6")
	except Exception as e:
		print(f"Your input resulted in an error: {e}")
print("Thanks for playing this game")

