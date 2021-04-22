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

#Loop over db table
for i in range(len(db)):
    store = db[i][0]
    product = db[i][1]

    #Start chromedriver
    driver = webdriver.Chrome(executable_path="/Users/chaiwonpark/Downloads/chromedriver")
    driver.implicitly_wait(30)

    try:
        SCROLL_PAUSE_TIME = 1
        driver.get("https://shopping.naver.com/outlet/stores/" + store + "/products/" + product)
        # driver.get("https://shopping.naver.com/outlet/stores/1000023005/products/4884762266")
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        soup = BeautifulSoup(driver.page_source, "lxml")
        currPath = os.getcwd()

        """
        checkPath = currPath + "/text/" + store
    
        #Check if the directory is already made for contents file
        if not os.path.exists(checkPath):
            os.mkdir(currPath + "/text/" + store)
    
        #Saving contents as [storeId].txt file
        f = open("text/" + store + "/" + product + ".txt", "w+")
    
        #Check if there is blockquote text. If there is, save it to .txt file
        if soup.blockquote is None:
            pass
        else:
            f.write((soup.blockquote.text + "\n").encode('utf-8'))
            # print(soup.blockquote.text)
    
        for c in soup.find_all('span'):
            if c.parent.name == 'p' or c.parent.name == 'h4':
                f.write((c.text + "\n").encode('utf-8'))
    
        f.close()
        """


        #Check if the directory is already made for image file
        checkPath2 = currPath + "/image/" + store
        if os.path.exists(checkPath2):
            os.mkdir(currPath + "/image/" + store + "/" + product)
        else:
            os.mkdir(currPath + "/image/" + store)
            os.mkdir(currPath + "/image/" + store + "/" + product)
        checkPath3 = currPath + "/image/" + store + "/" + product

        #Saving images as [index e.g., 1,2 and so on].jpg
        i = 0
        for c in range(len(soup.find_all("img"))):
            alt = soup.find_all("img")[c].get('alt')
            img = soup.find_all("img")[c].get('src')
            if not alt or c == 3 or alt == '1' or alt == '2':
                if img[0:6] == "https:":
                    urllib.urlretrieve(img, 'image/' + store + "/" + product + "/" + str(i) + ".jpg")
                    urllib.urlretrieve(img, str(i) + ".jpg")
                    i += 1
            else:
                pass


    finally:

        driver.quit()
