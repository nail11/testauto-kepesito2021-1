"""
## 3 Feladat: Alfanumerikus mező

Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Alfanumerikus mezőapp-ot az
[https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html]
(https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html) oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Alfanumerikus mező app tesztelését.

Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!

A cél a mező validáció tesztelése:

* Helyes kitöltés esete:
    * title: abcd1234
    * Nincs validációs hibazüzenet

* Illegális karakterek esete:
    * title: teszt233@
    * Only a-z and 0-9 characters allewed.

* Tul rövid bemenet esete:
    * title: abcd
    * Title should be at least 8 characters; you entered 4.
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

url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(url)


# elements

title_field = driver.find_element_by_id("title")
error_mess = driver.find_element_by_xpath('/html/body/form/span')

# data

test_data = ["abcd1234", "teszt233@", "abcd"]
messages = ["Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]

# TC 1

def test_valid_data():

    """
    * Helyes kitöltés esete:
    * title: abcd1234
    * Nincs validációs hibazüzenet

    """
    title_field.send_keys(test_data[0])
    time.sleep(1)

    assert title_field.text == ""

# TC 2
def test_invalid_data():

    """
    Illegális karakterek esete:
    * title: teszt233@
    * Only a-z and 0-9 characters allewed.
    """

    title_field.send_keys(test_data[1])
    time.sleep(1)
    assert error_mess.text == messages[0]

# TC 3

    """
    Tul rövid bemenet esete:
    * title: abcd
    * Title should be at least 8 characters; you entered 4.
    """

def test_short_data():

    title_field.clear()
    title_field.send_keys(test_data[2])
    time.sleep(1)
    assert error_mess.text == messages[1]

#test_valid_data()
#test_invalid_data()
#test_short_data()
