def arithmetic_progression():
    inp = raw_input('enter the numbers: ').split(' ')
    if not len(inp) == 3:              
        return arithmetic_progression()

    a = float(inp[0])
    d = float(inp[1])
    n = float(inp[2])

    s = ( (2 * a) + ((n - 1) * d) ) * (n / 2)

    print('Sum to n terms of given AP')

arithmetic_progression()
