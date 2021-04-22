
import time

# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from webdriver_manager.chrome from ChromeDriverManager

print('Beginning file download with urllib2...')

driver = webdriver.Chrome(executable_path="/Users/chaiwonpark/Downloads/chromedriver")
driver.implicitly_wait(30)

try:
    SCROLL_PAUSE_TIME = 1
    driver.get("https://shopping.naver.com/outlet/branch/10009004")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for c in soup.find_all("a"):
        print(c.get('href'))



finally:
    driver.quit()

# url = 'https://shopping.naver.com/outlet/branch/10009004'
# html_content = requests.get(url).text
# soup = BeautifulSoup(html_content, 'html')
# print(soup.prettify())
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html,'html.parser')

# for link in soup.find_all('a'):
#     print(link.get('href'))
# brand = soup.find_all("a", class_="_1c_DmOMzze")
# print(html)
# print(soup.prettify())
# print(brand)
# print(soup.find_all("a", class_="_1c_DmOMzze"))








