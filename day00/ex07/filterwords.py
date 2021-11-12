import sys

if sys.argv[3:] or not sys.argv[1:] or not sys.argv[2:] or not sys.argv[2].isnumeric():
	print ("ERROR")
	quit()

words = sys.argv[1].split()
final_list = []

for word in words:
	if len(word) > int(sys.argv[2]):
		final_list.append(word)
print(final_list)