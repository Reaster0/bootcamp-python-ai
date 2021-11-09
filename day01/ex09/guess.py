import random

nbr = random.randint(1, 99)

print("let's test your luck and see if you can fin the random number between 1 and 99\nOr you cant type exit to well...exit")

#print("HACKING IN THE MATRIX\n\n\n\n\n\nthe number is", nbr)

def loop(nbr_try):
	nbr_try += 1
	usr_nbr = input("Input your number: ")
	if usr_nbr == 'exit':
		quit()
	elif not usr_nbr.isdigit() or int(usr_nbr) > 99 or int(usr_nbr) < 1:
		print("Please put a number between 1 and 99")
	elif int(usr_nbr) == nbr:
		if nbr == 42:
			print("make a reference to Douglas Adams lol")
		print("Waw well play! you're really lucky!")
		if nbr_try == 1:
			print("And on the first try!... did you've cheat?")
		quit()
	else:
		print("nope this isn't the number to gess, but maybe the number is", random.randint(1, 99), '?')
	loop(nbr_try)

loop(0)