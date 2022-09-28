from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
PATH=Service('C:\sel\chromedriver.exe')
driver = webdriver.Chrome(service=PATH, options=options)


driver.get("https://www.google.com/")
print(driver.title)

consent_button = driver.find_element(By.ID, "L2AGLb")
time.sleep(3)
consent_button.click()


search = driver.find_element(By.CSS_SELECTOR, "input.gLFyf")
search.send_keys("knitting patterns")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements(By.TAG_NAME, "div")
    for art in articles:
        header = art.find_element(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md")
        print(header.text)

finally:
    driver.quit()



# time.sleep(5)
# driver.quit()