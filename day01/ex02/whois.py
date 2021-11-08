import sys

if len(sys.argv[1:]) < 1 or sys.argv[2:] or not sys.argv[1].isdigit():
	print("ERROR")
	quit()

if (not int(sys.argv[1])):
	print("I'm Zero")
elif int(sys.argv[1]) % 2:
	print("I'm Odd")
else:
	print("I'm Even")
