from googletrans import Translator

def tranlate():
    """"""
    translator = Translator()
    word = input('Введите слово: ')
    result = translator.translate(word, src='ru', dest='en')
    print(result.text)

if __name__ == "__main__":
    tranlate()