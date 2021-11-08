import sys

if sys.argv[3:]:
	print("InputError: too many arguments\nUsage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
	quit()
if len(sys.argv[1:]) < 1 or len(sys.argv[2:]) < 1:
	print("Usage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
	quit()
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
	print("InputError: only numbers\nUsage: python operations.py <number1> <number2>\nExample:\npython operations.py 10 3")
	quit()

sum = int(sys.argv[1]) + int(sys.argv[2])
diff = int(sys.argv[1]) - int(sys.argv[2])
prod = int(sys.argv[1]) * int(sys.argv[2])
if not int(sys.argv[2]):
	quoti = "ERROR (div by zero)"
else:
	quoti = int(sys.argv[1]) / int(sys.argv[2])
if not int(sys.argv[2]):
	rem = "ERROR (modulo by zero)"
else:
	rem = int(sys.argv[1]) % int(sys.argv[2])

print(
"Sum:       ", sum,
"\nDifference:", diff,
"\nProduct:   ", prod,
"\nQuotient:  ", quoti,
"\nRemainder: ", rem)
