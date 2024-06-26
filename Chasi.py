import time
import datetime

def chassi():
    minimenu = """Выбирите команду - 
    1 - Текущие время
    2 - Таймер
    3 - Обратно в Мини-Меню
    0 - Вернутся в обычное меню"""
    print(minimenu)

    Vibor = input('Выбери действие - ')
    print(Vibor)

    while Vibor != '0':
        if Vibor == "1":
            current_time = datetime.datetime.now().time()
            print(current_time)
        elif Vibor == "4":
            print(minimenu)
        elif Vibor == "2":
            poltime = int(input("Ввидите время в секундах таймер - "))
            time.sleep(poltime)
            for i in range(5):
                print("Таймер Истек!")
        elif Vibor == "3":
            current_time = datetime.datetime.now().time().hour
            polittime = "9"
            polittimee = "12"
            pollitime = "19"


            if current_time == polittime:
                for i in range(5):
                    print("Срочно! Утриние новости!")

            if current_time == polittimee:
                for i in range(5):
                    print("Срочно! Дневные новости!")

            if current_time == pollitime:
                for i in range(5):
                    print("Срочно! Вечерние новости начались!")
                else:
                    print("Ещё не скоро...")


        elif Vibor == "3":
            budilnik = int(input("Введи время в "))
            if budilnik == current_time:
                print("Get up!")
        else:
            print('Команда введена не правильно, попробуй ещё раз...')
        Vibor = input('Номер действия - ')
    print("До скорых встреч!")


if __name__ == "__main__":
    chassi()