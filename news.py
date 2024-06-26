
import requests
from bs4 import BeautifulSoup


def neews():
    print("\n ¯\_(ツ)_/¯ 𝕃𝔼𝕋𝕆𝕍 ℕ𝔼𝕎𝕊 𝕍.𝟙.𝟘 ¯\_(ツ)_/¯\n")
    bweq = 'https://ptzgovorit.ru/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    fllpage = requests.get(bweq, headers=headers)

    sup = BeautifulSoup(fllpage.content, 'html.parser')

    wetrx = sup.findAll("div", {"class": "views-field-title big-card-title"})

    print("1 = " + wetrx[0].text)
    print("2 = " + wetrx[1].text)
    print("3 = " + wetrx[2].text)
    print("4 = " + wetrx[3].text)
    print("5 = " + wetrx[4].text)
    print("6 = " + wetrx[5].text)
    print("7 = " + wetrx[6].text)
    print("8 = " + wetrx[7].text)
    print("9 = " + wetrx[8].text)
    print("10 = " + wetrx[9].text)


if __name__ == "__main__":
    neews()
