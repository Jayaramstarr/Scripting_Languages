def AtomicDictionary():
    d = {
        'C':'Carbon', 'B':'Boron', 'N':'Nitogen', 'S':'Sulphur'
    }
    print(f'\nAtomic Dictionary:\t{d}')
    print('\nEnter symbol of atomic element:')
    symb=input()
    print('\nEnter name of atomic element:')
    ele=input()
    if symb in d.keys():
        print('\nSymbol exists, name updated')
    else:
        print('\nNew element added')
    d[symb]=ele
    print(f'\nAtomic Dictionary:\t{d}')
    print(f'Length of dictionary is {len(d)}')
    print('\nEnter symbol of atomic element to be searched:')
    symb=input()
    if symb in d.keys():
        print('\nElement present in the list')
    else:
        print('\nElement not present in the list')