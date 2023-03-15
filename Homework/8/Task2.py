"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».

Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""

def discount(point:int):
    if 0 <= point < 50:
        print("Скидка 10%")
    if 50 <= point < 100:
        print("Скидка 15%")
    if 100 <= point:
        print("Скидка 20%")

point = int(input("Type point: "))
discount(point)