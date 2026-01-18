ages = int (input('введите стаж роботи'))
salary = int (input('введите заробитну плату'))
match ages:
    case _ if ages<1:
        print('Премія не передбачена')
    case _ if 1< ages <3:
        bonus = salary * 5 / 100
        print("Премія:",bonus)
    case _ if 3 <= ages < 5:
        bonus = salary * 10 / 100
        print("Премія:", bonus)

    case _:
        bonus = salary * 15 / 100
        print("Премія:", bonus)