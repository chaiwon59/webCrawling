import time
from bs4 import BeautifulSoup
from selenium import webdriver
import mysql.connector
import os
import urllib


#Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Fltek0509?",
    database="MySQL",
    auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT storeId, productId, brandname FROM naver")

db = mycursor.fetchall()



#Start chromedriver
driver = webdriver.Chrome(executable_path="/Users/chaiwonpark/Downloads/chromedriver")
driver.implicitly_wait(30)

try:
    SCROLL_PAUSE_TIME = 1
    driver.get("https://shopping.naver.com/outlet/stores/1000022985/products/4908836212")
    # driver.get("https://shopping.naver.com/outlet/stores/" + store + "/products/" + product)
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "lxml")

    #Saving contents as [storeId].txt file
    # f = open("text/" + store + "/" + product + ".txt", "w+")
    for c in soup.find_all('span'):
        if c.parent.name == 'p' or c.parent.name == 'h4' or c.parent.name == 'blockquote':
            # f.write((c.text + "\n").encode('utf-8'))
            print(c.text)

finally:

    driver.quit()
