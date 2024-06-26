import Wikiped
import calculator
import Chasi
import khb
import news
from Weather import check_weather

print("\n(◕‿◕) 𝕃𝕖𝕥𝕠𝕧 𝔹𝕠𝕥 (◕‿◕)\n")

print('Привет, я умный помощник Даниил')
menu = """Menu - 
1 = Калькулятор
2 = Часы
3 = Википедия
4 = Новости
5 = Камень ножницы бумага
6 = Погода
_________
0 = Конец
8 = Вернуться в меню    
"""
print(menu)

choise = input('Выбери действие - ')
print(choise)

while choise != '0':
    if choise == "1":
        calculator.run_calculator()
    elif choise == "9":
        print(menu)
    elif choise == "2":
        Chasi.chassi()
    elif choise == "5":
        khb.rockpaperscissors()
    elif choise == "4":
        news.neews()
    elif choise == "3":
        Wikiped.get_wiki()
    elif choise == "6":
        check_weather(input('Введи город - '))
    else:
        print('Команда введена не правильно, попробуй ещё раз...')
    choise = input(""" Menu - 
1 = Калькулятор
2 = Часы
3 = Википедия
4 = Новости
5 = Камень ножницы бумага
_________
0 = Конец
9 = Вернуться в меню

Номер действия - """)
print("До скорых встреч!")