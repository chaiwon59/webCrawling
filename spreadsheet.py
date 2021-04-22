from __future__ import absolute_import
import time
import os

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="/Users/chaiwonpark/Downloads/chromedriver")
driver.implicitly_wait(100)


def main():

    driver.get("https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.smartstore.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.smartstore.naver.com%252F%2523")

    login()

    # Number of stores
    for i in range(0, 100):
        print(i)
        if i == 0:
            print("first store")
            pass
        else:
            storeChoiceButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                        "/html/body/ui-view[1]/div[3]/div/div[1]/nav/div/ul/li[2]/a")))
            print("storeChoiceButton made")
            storeChoiceButton.click()

            storeButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                        "/html/body/div[1]/div/div/div[2]/div/div/ul/li[" + str(i) + "]/div/div[1]/div/label")))
            storeButton.click()

        if is_popup():
            print("pop up")
            handlePopUp()
        else:
            pass

        """        
        product()
        saveProduct()

        time.sleep(3)
        
        if is_popup2():
            print("no data pop up")
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/span/button").click()
        else:
            print("no pop up")
            pass
        """

        order()
        saveOrder()

    driver.quit()
    fileName()

def login():

    username = driver.find_element_by_id("id")
    username.clear()
    username.send_keys("gangnamnw")

    password = driver.find_element_by_id("pw")
    password.clear()
    password.send_keys("rkdskawja!!11")

    submitButton = driver.find_element_by_id("log.login")
    submitButton.click()
    print("login done")

def saveProduct():

    downloadButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                        "/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div/ui-view[2]/div[1]/div[1]/div[2]/div/div[2]/button/span[1]")))
    time.sleep(3)
    downloadButton.click()
    # time.sleep(3)
    print("save product done")


def handlePopUp():
    closeButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                        "/html/body/div[1]/div/div/div[1]/button")))
    closeButton.click()
    confirmButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                        "/html/body/div[1]/div/div/div[2]/div/span[2]/button")))

    confirmButton.click()
    print("handling pop up done")


def product():
    productManageButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                "/html/body/ui-view[1]/div[3]/div/div[2]/div[1]/div/div[1]/ul/li[1]/a")))

    productManageButton.click()

    productSearchButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                "/html/body/ui-view[1]/div[3]/div/div[2]/div[1]/div/div[1]/ul/li[1]/ul/li[1]/a")))

    productSearchButton.click()
    print("product clicking done")


def order():
    orderManageButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                            "/html/body/ui-view[1]/div[3]/div/div[2]/div[1]/div/div[1]/ul/li[3]/a")))

    orderManageButton.click()

    orderSearchButton = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                            "/html/body/ui-view[1]/div[3]/div/div[2]/div[1]/div/div[1]/ul/li[3]/ul/li[1]/a")))
    orderSearchButton.click()
    print("order clicking done")

def saveOrder():
    print("save order starts")
    driver.switch_to.frame("__naverpay")
    time.sleep(1)
    print("switch to frame")
    button = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                "/html/body/div/div/div/div/div/div[2]/div[2]/div[1]/div/button[2]/span")))
    button.click()
    driver.switch_to.default_content()
    print("save order done")


def is_popup():
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    if soup.find("h3", {"class": "modal-title"}) or soup.find("body", {"div": "pace-done pace-done"}) or soup.find("body", class_="pace-done modal-open") or soup.find("body", {"class":" modal-open pace-done"}):
        print("popup")
        print(soup.prettify())
        # if soup.fiind("td", {"data-title":"ncdept"}):
        #     print("ncdept pop up")
        return True
    else:
        print("no popup")
        return False


def is_popup2():
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    if soup.find("body", {"class": "pace-done modal-open"}) or soup.find("div", {"class": "modal-body"}):
        print("popup")
        return True
    else:
        print("no popup")
        return False

def fileName():
    textFile = open("/Users/chaiwonpark/Desktop/excel/files.txt", "a+")
    for root, dirs, files in os.walk("/Users/chaiwonpark/Desktop/excel"):
        for file in files:
            if file.endswith(".xlsx"):
                # print(os.path.join(root, file))
                print(file)
                textFile.write(file + '\n')

if __name__ == "__main__":
    main()

if __name__ == "__saveProduct__":
    saveProduct()

if __name__ == "__product__":
    product()

if __name__ == "__order__":
    order()

if __name__ == "__handlePopUp__":
    handlePopUp()

if __name__ == "__login__":
    login()

if __name__ == "__is_popup__":
    is_popup()

if __name__ == "__fileName__":
    fileName()