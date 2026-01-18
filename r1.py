ball = int(input('введите балл'))
match ball:
    case _ if 90<= ball <= 100:
        print("Відмінно")
    case _ if 70<= ball <= 89:
        print('Добре')
    case _ if 50<= ball <= 69:
        print("Задовільно")
    case _ if 50 >= ball:
        print("Незадовільно")
    case _: print('помилка')