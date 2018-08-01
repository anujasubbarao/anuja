n=int(raw_input())
while True:
	print("Enter '0' for exit.")
	n = input("Enter any character: ")
	if n == '0':
		break
	else:
		if((n>='a' and n<='z') or (n>='A' and n<='Z')):
			print("Alphabet")
		else:
			print("Not")
