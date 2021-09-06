""" # 1 Feladat: Pitagorasz-tétel

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Pitagorasz-tétel app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html]
(https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Pitagorasz-tétel appban:

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

* Helyesen jelenik meg az applikáció betöltéskor:
    * a: <üres>
    * b: <üres>
    * c: <nem látszik>

* Számítás helyes, megfelelő bemenettel
    * a: 2
    * b: 3
    * c: 10

* Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * c: NaN
"""
# ...............................................................................................

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(url)


# data

test_data1 = [2, 3, 10]
test_data2 = ["", "", "NaN"]


# functions

def find_by_id(id_sel):
    return driver.find_element_by_id(id_sel)


def calc_pith(data_set):
    find_by_id("a").clear()
    find_by_id("a").send_keys(data_set[0])
    find_by_id("b").clear()
    find_by_id("b").send_keys(data_set[1])
    find_by_id("submit").click()
    return find_by_id("result")


# TC 1

def test_empty_fields_at_start():
    """ * Helyesen jelenik meg az applikáció betöltéskor:
    * a: <üres>
    * b: <üres>
    * c: <nem látszik>"""

    assert find_by_id("a").text == ""
    assert find_by_id("b").text == ""
    assert find_by_id("result").text == ""


# TC 2

def test_pith_calc_valid():
    """
    * Számítás helyes, megfelelő bemenettel
    * a: 2
    * b: 3
    * c: 10
    """

    assert int(calc_pith(test_data1).text) == test_data1[2]


# TC 3


def test_pith_calc_invalid():
    """ Üres kitöltés:
       * a: <üres>
       * b: <üres>
       * c: NaN"""

    assert calc_pith(test_data2).text == test_data2[2]


#test_empty_fields_at_start()

#test_pith_calc_valid()

#test_pith_calc_invalid()
