def convertVNDtoUSD():
    print('This program converts US dollars to VND ')
    print('')
    dollars = eval(input("Enter amount in dollars: "))
    convert_to_vnd = lambda dollars: dollars * 23735
    vnd = convert_to_vnd(dollars)
    print('That is ',vnd,'Vietnamese dong')
    
convertVNDtoUSD()

