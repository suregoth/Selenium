from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time



s = Service('C:\sel\chromedriver.exe')
driver = webdriver.Chrome(service=s)


driver.get("https://www.google.com/")
print(driver.title)

consent_button = driver.find_element(By.ID, "L2AGLb")
time.sleep(3)
consent_button.click()


search = driver.find_element(By.CSS_SELECTOR, "input.gLFyf")
search.send_keys("ile nóg ma padalec")
search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
# finally:
#     driver.quit()

# print(main.text)

time.sleep(20)
driver.quit()