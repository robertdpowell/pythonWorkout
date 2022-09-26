def hex_output():
    decnum = 0
    hexnum = input('Please enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        print(f'{digit}: * 16  ** {power}')
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

hex_output()