import urllib
import time
from bs4 import BeautifulSoup
from selenium import webdriver

print('Beginning file download with urllib2...')

driver = webdriver.Chrome(executable_path="/Users/chaiwonpark/Downloads/chromedriver")
driver.implicitly_wait(30)

try:
    SCROLL_PAUSE_TIME = 1
    driver.get("https://shopping.naver.com/outlet/stores/100061970/products/4905282984")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")
    for c in range(len(soup.find_all("img"))):
        alt = soup.find_all("img")[c].get('alt')
        img = soup.find_all("img")[c].get('src')
        if not alt:
            print(img)
            if img[0:6] == "https:":
                # urllib.urlretrieve(img, 'download/'+(img.split("/")[-1]).split("?")[-2])
                urllib.urlretrieve(img, 'image/' + str(c) + ".jpg")
                # print((img.split("/")[-1]).split("?")[-2])
        else:
            pass



finally:

    driver.quit()
