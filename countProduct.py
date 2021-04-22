
import time

from bs4 import BeautifulSoup
from selenium import webdriver

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

    counter = 0
    # for c in soup.find_all("a"):
    #     className = c.get('class')
    #     # print(className)
    #     if className is not None:
    #         print(className)
    #         if className[1] is not None:
    #             print(className[1])
    #             counter += 1

    for c in soup.find_all('a'):
        link = c.get('href')
        if 'products' in link:
            print(link)
            counter += 1

    print(counter)


finally:
    driver.quit()

