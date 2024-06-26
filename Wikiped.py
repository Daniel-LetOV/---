import wikipedia


def get_wiki():
    """"""
    wikipedia.set_lang("ru")
    page_name = input("Введите,что вам нужно - ")
    result = wikipedia.page(page_name)
    print(result.url)
    print(result.content)


if __name__ == "__main__":
    get_wiki()
