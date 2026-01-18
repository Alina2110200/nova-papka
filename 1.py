#login = input('enter login')
#display_name = login if login else 'guest'
#print(f'hello, {display_name}')


#age = 15
#if age < 18:
#    pass
#else:
#    print('full access granted')


day = int(input('enter'))

match day:
    case 1: print('monday')
    case 2: print('tuesday')
    case 3: print('wensday')
    case 4: print('thursday')
    case 5: print('friday')
    case 6: print('saturday')
    case 7: print('sunday')
    case _: print('incorect day')

month = int(input('enter number of month'))
match month:
    case 12 | 1 | 2 :print('winter')
    case 3 | 4 | 5 :print('spring')
    case 6 | 7 | 8 :print('summer')
    case 9 | 10 | 11 :print('autumm')
    case _:print('not right answer')

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 12:
        print('work day in december')
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print('work day in january') 
    case 7 | 6 | if month == 12:
        print('free day in december')   
