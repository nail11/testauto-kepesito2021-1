 #...............................................................................................

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(url)

# elements