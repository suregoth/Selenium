from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time



s = Service('C:\sel\chromedriver.exe')
driver = webdriver.Chrome(service=s)


driver.get("https://www.petiteknit.com/")
print(driver.title)

search = driver.find_element(By.ID, "search-input")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
finally:
    driver.quit()

print(main.text)

time.sleep(5)
driver.quit()