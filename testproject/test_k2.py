"""
# 2 Feladat: Színes reakció

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Színes reakció app-ot az
 [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html]
 (https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Színes reakció app tesztelését.

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

Az alábbi teszteseteket kell lefedned:

* Helyesen jelenik meg az applikáció betöltéskor:
    * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak
    a `[  ]` szimbólum látszik.
    <szín neve> [     ] == [     ]

* El lehet indítani a játékot a `start` gommbal.
    * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.

* Eltaláltam, vagy nem találtam el.
    * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
    amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
      ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.

"""
# ...............................................................................................
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(url)

# elements

id_s = ["randomColorName", "randomColor", "testColor", "testColorName", "start", "stop",
        "result", "Correct!", "Incorrect!"]


# functions

def find_by_id(id_sel):
    return driver.find_element_by_id(id_sel)


def color_pick():                           # elindítjuk és leállítjuk a szinválasztót
    find_by_id(id_s[4]).click()
    time.sleep(2)
    find_by_id(id_s[5]).click()


# TC 1

def test_at_start():
    """
        * Helyesen jelenik meg az applikáció betöltéskor:
        * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak
        a `[  ]` szimbólum látszik.
        <szín neve> [     ] == [     ]
        """

    assert find_by_id(id_s[1]).text == find_by_id(id_s[2]).text


def test_button_func():
    """
    * El lehet indítani a játékot a `start` gommbal.
    * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.

    """
    color_pick()

    assert find_by_id(id_s[6]).is_displayed()

    # TC 3

    """
    Eltaláltam, vagy nem találtam el.
    * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
    amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
      ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.
    """


def test_color_match():
    driver.get(url)
    color_pick()

    if find_by_id(id_s[0]) == find_by_id(id_s[3]):
        assert find_by_id(id_s[6]).text == id_s[7]
    else:
        assert find_by_id(id_s[6]).text == id_s[8]


#test_at_start()
#test_button_func()
#test_color_match()
