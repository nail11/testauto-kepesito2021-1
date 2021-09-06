"""

# 4 Feladat: Műveletek karakterekkel

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Műveletek karakterekkel app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html]
(https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Műveletek karakterekkel app tesztelését.

Az applikáció minden frissítésnél véletlenszerűen változik!

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

Az alábbi teszt eseteket kell kidolgozzad:

* Helyesen betöltődik az applikáció:
    * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
      * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

* Megjelenik egy érvényes művelet:
    * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
    * `op` mező vagy + vagy - karaktert tartlamaz
    * `num` mező egy egész számot tartalamaz

* Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
    * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
    * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
    * A `num` mezőben megjelenő mennyiségű karaktert
    * az `result` mező helyes karaktert fog mutatni
"""

# ...............................................................................................

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(url)

# elements

char_table = driver.find_element_by_xpath("/html/body/div/div/p[3]")

id_s = ["chr", "op", "num"]

# data

test_data = ["!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"]


# functions

def find_by_id(id_sel):
    return driver.find_element_by_id(id_sel)


# TC 1

def test_at_start():
    """
    Helyesen betöltődik az applikáció:
    * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
      * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
    """

    assert char_table.text == test_data[0]


# TC 2

def test_valid_op():
    """
    Megjelenik egy érvényes művelet:
    * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
    * `op` mező vagy + vagy - karaktert tartlamaz
    * `num` mező egy egész számot tartalamaz

    """

    assert find_by_id(id_s[0]).text in test_data[0]
    assert find_by_id(id_s[1]).text == ("+" or "-")
    assert find_by_id(id_s[2]).text in "1234567890"


#test_at_start()
#test_valid_op()
