import sys

str_temp = ''
if len(sys.argv[1:]) < 1:
	quit()
for i in sys.argv[1:]:
	if str_temp != '':
		str_temp += ' '
	str_temp += i

print(str_temp[:: -1].swapcase())