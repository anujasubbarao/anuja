def do_stuff(raw_input):
	x, op, y = [x for x in raw_input.split(" ")]
	if op == '/':
		print(int(x) / int(y))
	else:
		print(int(x) % int(y))
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
